#!/usr/bin/env python3
"""
Generate the site's figures from the HarmoniCore source of truth.

The point of this script is that nothing on the site is drawn by hand. Every
figure comes out of the same code and the same data that the project itself
runs on, styled to match the site so the plots look like they belong.

Figures are written to public/figures/<name>.png and referenced from a
project's markdown as:

    figure: "/figures/harmonicore-ringmod.png"

Usage
-----
    python scripts/make_figures.py --harmonicore ~/Projects/harmonicore

    # just one of them
    python scripts/make_figures.py --harmonicore ~/Projects/harmonicore --only ringmod

Requirements
------------
    pip install matplotlib numpy
    # for the pitch figure only:
    pip install librosa soundfile
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
except ImportError:
    sys.exit("matplotlib is required:  pip install matplotlib numpy")


# --------------------------------------------------------------------------
# Site theme. These values are the design tokens from src/styles/global.css.
# If you change the site palette, change it here too.
# --------------------------------------------------------------------------

THEMES = {
    "light": {
        "paper": "#FBFAF8",
        "card": "#F3F1EC",
        "ink": "#1A1815",
        "ink2": "#55504A",
        "ink3": "#8A8377",
        "rule": "#DDD8D0",
        "accent": "#1E4D3C",
        "flag": "#8A6710",
    },
}

# Matches the 4:3 figure slot on the site at 2x for retina.
FIGSIZE = (6.4, 4.8)
DPI = 160

MONO = ["JetBrains Mono", "DejaVu Sans Mono", "Consolas", "monospace"]
SANS = ["Public Sans", "DejaVu Sans", "Segoe UI", "sans-serif"]


def style(ax, t, *, xlabel=None, ylabel=None, title=None):
    """Apply the site's look to an axes."""
    ax.set_facecolor(t["card"])
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(t["rule"])
        ax.spines[side].set_linewidth(1.0)
    ax.tick_params(colors=t["ink3"], labelsize=8, length=3, width=0.8)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_fontfamily(MONO)
    ax.grid(True, color=t["rule"], linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    if xlabel:
        ax.set_xlabel(xlabel, color=t["ink3"], fontsize=8.5, fontfamily=MONO, labelpad=8)
    if ylabel:
        ax.set_ylabel(ylabel, color=t["ink3"], fontsize=8.5, fontfamily=MONO, labelpad=8)
    if title:
        ax.set_title(title, color=t["ink"], fontsize=11, fontfamily=SANS,
                     fontweight="600", loc="left", pad=12)


def save(fig, out_dir: Path, name: str, theme: str, t):
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.png"
    fig.savefig(path, dpi=DPI, facecolor=t["paper"], bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"  wrote {path}")


# --------------------------------------------------------------------------
# Figure 1 — ring modulator: hardware against the Python reference
# --------------------------------------------------------------------------

def ringmod_figure(hc_root: Path, out_dir: Path) -> bool:
    """Plot the SV ring modulator output against the Python reference.

    Reads v2-effects/ring_mod_output.csv, which the testbench writes. Run
    `make ring_mod_verify` in v2-effects/sv first if it is missing or stale.
    """
    csv_path = hc_root / "v2-effects" / "ring_mod_output.csv"
    if not csv_path.exists():
        print(f"  skip ringmod: {csv_path} not found")
        print("  (run `make ring_mod_verify` in v2-effects/sv to generate it)")
        return False

    rows = []
    with csv_path.open(newline="") as f:
        for row in csv.reader(f):
            if not row or row[0].strip().startswith("#"):
                continue
            try:
                rows.append([float(x) for x in row])
            except ValueError:
                continue  # header line

    if not rows:
        print(f"  skip ringmod: no numeric rows in {csv_path}")
        return False

    data = np.array(rows)
    n = np.arange(len(data))

    # The testbench's column order can drift as the CSV evolves. Take the
    # last two numeric columns as (expected, actual) unless told otherwise.
    if data.shape[1] >= 3:
        hw = data[:, -1]
        ref = data[:, -2]
    else:
        print(f"  skip ringmod: expected >=3 columns, got {data.shape[1]}")
        return False

    err = hw - ref

    for theme, t in THEMES.items():
        fig, (ax1, ax2) = plt.subplots(
            2, 1, figsize=FIGSIZE, sharex=True,
            gridspec_kw={"height_ratios": [2.6, 1], "hspace": 0.18},
        )
        fig.patch.set_facecolor(t["paper"])

        ax1.step(n, ref, where="mid", color=t["ink3"], linewidth=2.4,
                 alpha=0.55, label="Python reference")
        ax1.step(n, hw, where="mid", color=t["accent"], linewidth=1.3,
                 label="SystemVerilog")
        style(ax1, t, ylabel="output (LSB)",
              title="Ring modulator: hardware vs reference")
        leg = ax1.legend(loc="upper right", frameon=False, fontsize=8)
        for text in leg.get_texts():
            text.set_color(t["ink2"])
            text.set_fontfamily(MONO)

        ax2.axhline(0, color=t["rule"], linewidth=1)
        ax2.bar(n, err, color=t["flag"], width=0.9)
        style(ax2, t, xlabel="sample", ylabel="error (LSB)")
        ax2.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))

        peak = int(np.max(np.abs(err))) if len(err) else 0
        rms = float(np.sqrt(np.mean(err ** 2))) if len(err) else 0.0
        ax2.text(
            0.008, 1.18, f"max |err| {peak} LSB    rms {rms:.3f} LSB",
            transform=ax2.transAxes, ha="left", va="bottom",
            color=t["ink3"], fontsize=8, fontfamily=MONO,
        )

        save(fig, out_dir, "harmonicore-ringmod", theme, t)
    return True


# --------------------------------------------------------------------------
# Figure 2 — v1 autotuner: detected pitch against corrected pitch
# --------------------------------------------------------------------------

def pitch_figure(hc_root: Path, out_dir: Path, wav_name: str | None) -> bool:
    """Run the v1 reference model over a wav and plot both pitch tracks."""
    try:
        import librosa
    except ImportError:
        print("  skip pitch: librosa not installed  (pip install librosa soundfile)")
        return False

    v1 = hc_root / "v1-autotune"
    wav_dir = v1 / "wav"
    if not wav_dir.exists():
        print(f"  skip pitch: {wav_dir} not found")
        return False

    if wav_name:
        wav = wav_dir / wav_name
    else:
        candidates = [w for w in sorted(wav_dir.glob("*.wav"))
                      if "_pitch_corrected" not in w.name]
        if not candidates:
            print(f"  skip pitch: no source wavs in {wav_dir}")
            return False
        wav = candidates[0]

    print(f"  using {wav.name}")
    sys.path.insert(0, str(v1 / "32bitPython"))
    try:
        from HarmoniCore import aclosest_pitch_from_scale, SCALE  # noqa: E402
        from yin import yin  # noqa: E402
    except Exception as exc:  # pragma: no cover
        print(f"  skip pitch: could not import the v1 model ({exc})")
        return False

    y, sr = librosa.load(str(wav), sr=None, mono=True)
    frame_length, hop_length = 2048, 512
    fmin, fmax = librosa.note_to_hz("C2"), librosa.note_to_hz("C7")

    f0 = yin(y, frame_length=frame_length, hop_length=hop_length,
             sr=sr, fmin=fmin, fmax=fmax, center=True)
    corrected = aclosest_pitch_from_scale(f0, SCALE)
    times = librosa.times_like(f0, sr=sr, hop_length=hop_length)

    for theme, t in THEMES.items():
        fig, ax = plt.subplots(figsize=FIGSIZE)
        fig.patch.set_facecolor(t["paper"])

        ax.plot(times, f0, color=t["ink3"], linewidth=2.2, alpha=0.6,
                label="detected pitch")
        ax.plot(times, corrected, color=t["accent"], linewidth=1.3,
                label=f"corrected to {SCALE}")
        ax.set_yscale("log")
        ax.set_ylim(max(fmin, 60), min(fmax, 1200))
        style(ax, t, xlabel="time (s)", ylabel="f0 (Hz)",
              title="Pitch detection and scale correction")
        leg = ax.legend(loc="upper right", frameon=False, fontsize=8)
        for text in leg.get_texts():
            text.set_color(t["ink2"])
            text.set_fontfamily(MONO)

        save(fig, out_dir, "harmonicore-pitch", theme, t)
    return True


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--harmonicore", type=Path, required=True,
                    help="Path to the consolidated harmonicore folder")
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "public" / "figures",
                    help="Where to write the PNGs (default: public/figures)")
    ap.add_argument("--wav", default=None, help="Which wav to use for the pitch figure")
    ap.add_argument("--only", choices=["ringmod", "pitch"], default=None)
    args = ap.parse_args()

    hc = args.harmonicore.expanduser().resolve()
    if not hc.exists():
        return print(f"No such folder: {hc}") or 1

    out = args.out.expanduser().resolve()
    print(f"HarmoniCore: {hc}")
    print(f"Output:      {out}\n")

    made = 0
    if args.only in (None, "ringmod"):
        print("ring modulator verification")
        made += ringmod_figure(hc, out)
    if args.only in (None, "pitch"):
        print("pitch detection")
        made += pitch_figure(hc, out, args.wav)

    print()
    if made:
        print(f"{made} figure(s) written. Reference them as:")
        print('  figure: "/figures/harmonicore-ringmod.png"')
    else:
        print("Nothing generated. See the skip reasons above.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

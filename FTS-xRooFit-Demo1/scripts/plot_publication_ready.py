#!/usr/bin/env python3
"""
Plot publication-ready dual-panel (LRS, FTS) figures from NPZ arrays.

This script does NOT compute statistics. It only loads arrays you've computed
with your own pipeline and renders the figure in the requested style.

Expected NPZ keys (example, adapt as needed):
    mu_grid
    T_lrs_obs, T_fts_obs
    C_lrs_68, C_lrs_95
    C_fts_68, C_fts_95

Usage:
    python scripts/plot_publication_ready.py \
        --npz path/to/arrays.npz \
        --out results/physically_correct_fts_gaussian_sanity.png \
        --mu-asimov 1.0 \
        --xlim 0 4
"""

import argparse
import numpy as np
from pathlib import Path

from publication_plotting import plot_fts_lrs_paper_style


def main():
    ap = argparse.ArgumentParser(description="Render publication-ready FTS/LRS figure from NPZ arrays")
    ap.add_argument('--npz', required=True, help='Path to NPZ file containing arrays')
    ap.add_argument('--out', required=True, help='Output PNG path')
    ap.add_argument('--mu-asimov', type=float, default=1.0)
    ap.add_argument('--xlim', nargs=2, type=float, default=None, help='Optional x-axis limits: lo hi')
    ap.add_argument('--focus-center', type=float, default=None)
    ap.add_argument('--focus-sigma', type=float, default=None)
    ap.add_argument('--focus-nsigma', type=float, default=1.0)
    args = ap.parse_args()

    data = np.load(args.npz)

    required = [
        'mu_grid', 'T_lrs_obs', 'T_fts_obs',
        'C_lrs_68', 'C_lrs_95', 'C_fts_68', 'C_fts_95'
    ]
    missing = [k for k in required if k not in data]
    if missing:
        raise KeyError(f"NPZ missing keys: {missing}")

    mu = data['mu_grid']
    Tl = data['T_lrs_obs']
    Tf = data['T_fts_obs']
    L68 = data['C_lrs_68']
    L95 = data['C_lrs_95']
    F68 = data['C_fts_68']
    F95 = data['C_fts_95']

    focus_region = None
    if args.focus_center is not None and args.focus_sigma is not None:
        focus_region = (args.focus_center, args.focus_sigma, args.focus_nsigma)

    xlim = tuple(args.xlim) if args.xlim is not None else None

    Path(Path(args.out).parent).mkdir(parents=True, exist_ok=True)
    plot_fts_lrs_paper_style(
        mu, Tl, Tf, L68, L95, F68, F95,
        mu_asimov=args.mu_asimov,
        focus_region=focus_region,
        xlim=xlim,
        savepath=args.out,
        dpi=300,
    )
    print(f"Saved: {args.out}")


if __name__ == '__main__':
    main()


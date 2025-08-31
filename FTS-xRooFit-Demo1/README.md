# FTS-xRooFit-Demo: Focused Test Statistics Implementation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![ROOT](https://img.shields.io/badge/ROOT-6.24%2B-orange)](https://root.cern)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

## Overview

This repository implements **Focused Test Statistics (FTS)** as a statistical method for enhancing sensitivity in parameter estimation and hypothesis testing in particle physics analyses. FTS incorporates physics-motivated "focus functions" to concentrate statistical power in specific parameter regions of interest.

## Project Structure

### 📁 Core Implementation
```
src/
├── fts_core.py                 # Main FTS algorithm and optimization classes
├── publication_plotting.py     # Professional plotting utilities
├── asimov_utils.py            # Asimov dataset generation tools
├── config.py                  # Environment configuration
├── demo_replacement_guide.py  # Integration guide for existing analyses
└── setup_environment.py       # Automated environment setup
```

### 📓 Interactive Notebooks
```
notebooks/
├── FTS_plus.ipynb            # 🎯 MAIN DEMO: Complete FTS implementation
├── validation_plots.ipynb    # Validation analysis and comparison plots
└── fts_core.py               # Core algorithms (notebook copy)
```

### 📋 Examples & Scripts
```
examples/
├── simple_integration.py     # Minimal standalone FTS example
└── html_exact_compat.py      # xRooFit environment compatibility layer

scripts/
├── plot_publication_ready.py # Generate publication-quality figures
└── validate_optimization.py  # Performance validation and testing
```

### 📊 Output Directory
```
results/                       # Auto-generated analysis outputs
├── *.png                     # Generated plots and figures
├── *.json                    # Analysis results and validation reports
└── validation_summary.json   # Overall validation metrics
```

## File Execution Guide

### 🚀 Main Demonstrations

#### `notebooks/FTS_plus.ipynb` → Complete Analysis Suite
**Execution:** Jupyter notebook interface
```bash
jupyter notebook notebooks/FTS_plus.ipynb
```
**Generates:**
- Statistical model setup and validation
- FTS vs LRT comparison analysis
- Performance benchmarks and timing metrics
- Interactive plots with hypothesis testing results
- Comprehensive analysis summary

#### `notebooks/validation_plots.ipynb` → Validation Analysis
**Execution:** Jupyter notebook interface
**Generates:**
- `results/fts_validation_verified.png` - Three-panel validation plots
- `results/fts_validation_report.json` - Detailed validation metrics
- Constant offset verification (FTS = LRT + C)
- Focus function normalization checks
- Statistical property validation

### 🔧 Command-Line Tools

#### `examples/simple_integration.py` → Basic FTS Demo
**Execution:**
```bash
python examples/simple_integration.py
```
**Output:**
```
Simple FTS Integration Example
=====================================
Mock Statistical Model Setup Complete
Focus Function: Gaussian(μ=1.0, σ=0.5)
FTS Test Statistic: 2.847
Traditional LRT: 3.496
Enhancement Factor: 18.6% improvement in focus region
```

#### `scripts/validate_optimization.py` → Performance Testing
**Execution:**
```bash
python scripts/validate_optimization.py [--quick]
```
**Generates:**
- Performance benchmark results
- Cache efficiency metrics
- Numerical accuracy validation
- Error handling verification
- Console report with PASS/FAIL status

#### `scripts/plot_publication_ready.py` → Publication Figures
**Execution:**
```bash
python scripts/plot_publication_ready.py \
    --npz results/analysis_data.npz \
    --out results/publication_figure.png \
    --mu-asimov 1.0
```
**Generates:**
- High-resolution publication-quality figures
- Dual-panel FTS vs LRT comparison
- Professional styling with confidence intervals
- Customizable output formats (PNG, PDF, SVG)

### 🔗 Environment Setup

#### `examples/html_exact_compat.py` → Auto-Configuration
**Usage:** Import in Python scripts/notebooks
```python
import sys
sys.path.insert(0, 'examples')
import html_exact_compat  # Automatically configures xRooFit environment
```
**Functions:**
- Detects ROOT and xRooFit installations
- Configures library paths (macOS/Linux)
- Sets up Python module paths
- Validates environment readiness

## Installation & Dependencies

### Prerequisites
- **Python 3.8+** with scientific computing stack
- **ROOT 6.24+** with Python bindings
- **xRooFit** (build from CERN GitLab)

### Quick Setup
```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install ROOT (macOS)
brew install root

# 3. Build xRooFit
git clone https://gitlab.cern.ch/will/xroofit.git
cmake -S xroofit -B xroofit_build
cmake --build xroofit_build

# 4. Verify installation
python examples/simple_integration.py
```

## Core Algorithm Features

### FTS Test Statistic
```
T_f(D; μ₀) = -2 log[L(μ₀|D) / ∫ L(μ|D) f(μ) dμ]
```

**Key Properties:**
- **Constant Offset**: FTS = LRT + C (C ≈ -0.649)
- **Focus Enhancement**: Higher sensitivity in focus regions
- **Numerical Stability**: Log-sum-exp implementation
- **Optimized Caching**: Eliminates redundant calculations

### Focus Functions

#### Gaussian Focus (Recommended)
```python
from src.fts_core import ProductionFocusFunction

focus = ProductionFocusFunction(
    mu_focus=1.0,      # Center of interest
    sigma_focus=0.5,   # Width of focus region
    normalize=True     # Ensure ∫f(μ)dμ = 1
)
```

#### Top-Hat Focus
```python
focus = ProductionFocusFunction(
    mu_focus=1.0,
    sigma_focus=1.0,
    weight_type='tophat'
)
```

## Usage Examples

### Basic FTS Calculation
```python
from src.fts_core import fts_ts_obs, ProductionFocusFunction

# Setup focus function
focus = ProductionFocusFunction(mu_focus=1.0, sigma_focus=0.5)

# Calculate FTS test statistic
fts_value = fts_ts_obs(
    nll_calc=your_nll_calculator,
    dataset="observed_data",
    mu0=1.0,
    focus_obj=focus,
    n_grid=101
)
```

### Publication Plotting
```python
from src.publication_plotting import plot_fts_lrs_paper_style

fig, axes = plot_fts_lrs_paper_style(
    mu_grid, T_fts_obs, T_lrt_obs,
    C_fts_68, C_fts_95, C_lrt_68, C_lrt_95,
    savepath='results/my_analysis.png'
)
```

## Validation Metrics

The implementation includes comprehensive validation:

| Test | Expected Result | Interpretation |
|------|----------------|----------------|
| **Constant Offset** | C = -0.649 ± 0.1 | FTS-LRT offset consistency |
| **Focus Normalization** | ∫f(μ)dμ = 1 ± 1e-6 | Proper probability weighting |
| **Cache Efficiency** | Hit rate > 50% | Performance optimization |
| **Error Handling** | Proper exceptions | Robust implementation |

## Mathematical Background

**FTS Theory**: Enhances statistical power by incorporating Bayesian-style weighting through focus functions, concentrating sensitivity in physically motivated parameter regions.

**Relationship to LRT**: FTS maintains the asymptotic properties of traditional likelihood ratio tests while providing enhanced power in focus regions.

## Troubleshooting

### Common Issues

**ROOT/xRooFit not found:**
```bash
# Verify ROOT installation
root --version
python -c "import ROOT; print('ROOT OK')"

# Check xRooFit build
ls -la xroofit_build/libxRooFit.*
```

**Import errors:**
```bash
# Ensure correct working directory
cd FTS-xRooFit-Demo1
python examples/simple_integration.py
```

## References

- **FTS Paper**: [arXiv:2507.17831](https://arxiv.org/abs/2507.17831)
- **xRooFit**: [GitLab Repository](https://gitlab.cern.ch/will/xroofit)
- **ROOT**: [Official Documentation](https://root.cern/)

## License

MIT License - See [LICENSE](./LICENSE) for details.

---

**Quick Start**: Run `python examples/simple_integration.py` for a basic demonstration, then explore `notebooks/FTS_plus.ipynb` for the complete interactive experience.
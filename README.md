# <div align="center">City Landscape In Sight: A Crowdsourced Framework for Unlocking Urban-Scale Window View Perceptions from Real Estate Imagery</div>

<div align="center">

**[Chucai Peng](https://ual.sg/author/chucai-peng/)**<sup>1,2,†</sup>, **[Sijie Yang](https://sijie-yang.com)**<sup>1,3,†</sup>, **Ang Liu**<sup>4</sup>, **Yang Xiang**<sup>5</sup>, **Zhixiang Zhou**<sup>2</sup>, **[Filip Biljecki](https://filipbiljecki.com)**<sup>1,6,*</sup>

<sup>1</sup> Department of Architecture, National University of Singapore  
<sup>2</sup> College of Horticulture and Forestry Sciences, Huazhong Agricultural University, Wuhan, China  
<sup>3</sup> School of Engineering and Applied Science, University of Pennsylvania, Philadelphia, USA  
<sup>4</sup> Department of Political Science, Rutgers University, Newark, USA  
<sup>5</sup> School of Arts and Communication, China University of Geosciences, Wuhan, China  
<sup>6</sup> Department of Real Estate, National University of Singapore  
<sup>†</sup> Co-first authors &nbsp;|&nbsp; <sup>*</sup> Corresponding author: filip@nus.edu.sg

</div>

<div align="center">

[![Paper](https://img.shields.io/badge/Landscape%20%26%20Urban%20Planning-105734-green.svg)](https://doi.org/10.1016/j.landurbplan.2026.105734)
[![arXiv](https://img.shields.io/badge/arXiv-2606.15198-b31b1b.svg)](https://arxiv.org/abs/2606.15198)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow.svg)](https://huggingface.co/datasets/sijiey/City-Landscape-In-Sight)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

</div>

<div align="center">
<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
<img src="assets/DoA Logo.jpg" alt="DoA Logo" width="120"/>
<img src="assets/UAL Logo.jpg" alt="UAL Logo" width="120"/>
</div>
<a href="https://ual.sg">Urban Analytics Lab</a> | National University of Singapore
</div>

---

<div align="center">
<img src="assets/fig_abstract.jpg" width="800" alt="Abstract">
</div>

## Overview

This repository contains the code and data for a crowdsourced framework that leverages real estate imagery to capture urban-scale window view perceptions (WVI). The framework combines crowdsourced perception surveys, machine learning models, and geospatial analytics to quantify and analyze how people perceive urban window views across a city.

## Repository structure

```
├── code_1_wvi_perception_survey_results.ipynb       # Crowdsourced survey + TrueSkill ranking
├── code_2_wvi_preprocess_visual_features.ipynb      # Mask/crop/resize + visual feature extraction
├── code_3_wvi_dataset_sampling.ipynb                # Hexagon_ID & Complex_ID for spatial sampling
├── code_4_wvi_perception_model_train_predict.ipynb  # ResNet-50 + tabular regression; spatial K-fold CV; citywide inference
├── code_5_wvi_perception_data_analytics.ipynb       # Urban-scale perception analytics (distribution, clustering, autocorrelation, hot/cold spots, floor)
├── code_6_wvi_perception_inference_analytics.ipynb  # Inference modelling (built-environment → perception), VIF, SHAP
├── code_7_wvi_perception_design_mapping.ipynb       # Window-view-driven urban design-support mapping
├── assets/                                          # Logos and abstract figure
├── data/
│   ├── data.csv                                     # Scores + geospatial features + Hexagon/Complex ID
│   ├── data_final_rescaled.csv                      # Rescaled (0–5, top 5% capped) for analytics
│   ├── metadata/                                    # Lon/Lat → Hexagon_ID / Complex_ID lookups
│   ├── perception_survey/
│   │   ├── raw/{dimension}.csv                      # Pairwise comparisons (input to Code 1)
│   │   └── ranked/ranked_{dimension}.csv            # TrueSkill ratings (written by Code 1)
│   ├── training_features/
│   │   ├── Features.csv                             # Training visual + structural features (Code 2)
│   │   ├── TrainingFeatures_{dimension}.csv         # Features + TrueSkill score (Code 1 → Code 3)
│   │   ├── kfold_splits/                            # Frozen 5-fold splits (random stratified)
│   │   └── kfold_splits_spatial/                    # Frozen 5-fold splits (spatial block; primary)
│   ├── inference_features/Features.csv              # City-scale visual features (Code 2)
│   ├── training_images/  | inference_images/        # WVIs — hosted on Hugging Face (see below), not in git
│   │   └── WVI_Processed/ | WVI_Segmentation/       # (WVI_Original raw images are NOT redistributed)
├── figures/                                         # Generated figures (PNG/SVG)
└── model_outputs/                                   # CV / ablation metrics (CSV); trained weights (*.pth) hosted on Hugging Face
```

**Perception dimensions** (used consistently across notebooks): `prefer`, `monotonous`, `quiet`, `extensive`, `vivid`, `oppressive`.

> **Images and trained weights** are hosted on the companion Hugging Face dataset — [`sijiey/City-Landscape-In-Sight`](https://huggingface.co/datasets/sijiey/City-Landscape-In-Sight) — because of their size. The **raw** window view images (`WVI_Original`) are **not** redistributed owing to real-estate-platform licensing; the processing scripts in Code 2 regenerate the processed imagery from source.

## Usage

Each `.ipynb` notebook can be run independently. For a full reproduction, run them in order **1 → 2 → … → 6**:

| Step | Notebook | Role |
|------|----------|------|
| 1 | `code_1_wvi_perception_survey_results.ipynb` | Load pairwise records from `raw/`, run TrueSkill, write `ranked/` and `TrainingFeatures_*.csv` |
| 2 | `code_2_wvi_preprocess_visual_features.ipynb` | Pre-process images and extract colour/semantic features for training and inference sets |
| 3 | `code_3_wvi_dataset_sampling.ipynb` | Assign `Hexagon_ID` and `Complex_ID`; build nested spatial units and K-fold splits |
| 4 | `code_4_wvi_perception_model_train_predict.ipynb` | Train ResNet-50 + tabular regression; spatial-block 5-fold CV; citywide inference on 12,334 WVIs |
| 5 | `code_5_wvi_perception_data_analytics.ipynb` | Distribution, clustering, spatial autocorrelation, hot/cold-spot, and floor-level analysis |
| 6 | `code_6_wvi_perception_inference_analytics.ipynb` | Inference modelling (built-environment → perception): regressor benchmark, VIF, SHAP |
| 7 | `code_7_wvi_perception_design_mapping.ipynb` | Window-view-perception-driven urban design-support mapping |

**Suggested path after Code 2:** Code 1 (labels) → Code 3 (splits) → Code 4 (train + predict) → Code 5 / 6 / 7 (analytics, inference, mapping).

> **Citywide maps note:** the perception surfaces are produced by a *single retained model per dimension* — the best-performing spatial-block fold checkpoint applied to all 12,334 WVIs — not by aggregating cross-validated predictions or retraining on all labelled samples. The 5-fold spatial CV is used only to estimate out-of-sample accuracy.

### Requirements

Python 3.10+ recommended. Core dependencies used across notebooks:

`numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `trueskill`, `torch`, `torchvision`, `Pillow`, `tqdm`

Install example:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn trueskill torch torchvision pillow tqdm
```

Code 2 invokes helper scripts under `scripts/` when run locally (`masked.py`, `masked_cut.py`, `data_mini.py`). Those scripts are not part of the public release (see `.gitignore`); equivalent steps are documented in the Code 2 notebook.

### Model checkpoints

Training (Code 4) writes `model_outputs/kfold_spatial/best_model_{dimension}.pth` (and `kfold_random/`, ~94 MB each). These weights are excluded from git because of GitHub size limits and are instead hosted on the [Hugging Face dataset](https://huggingface.co/datasets/sijiey/City-Landscape-In-Sight) under `model_outputs/`. You can either download them from there or **re-run Code 4** to regenerate them.

## Data

| Path | Description |
|------|-------------|
| `data/data.csv` | Main analytics table: predicted perception scores and geospatial features per WVI |
| `data/data_final_rescaled.csv` | Rescaled scores (0–5, top 5% capped); written/used by Code 4 |
| `data/perception_survey/raw/{dimension}.csv` | Pairwise survey records |
| `data/perception_survey/ranked/ranked_{dimension}.csv` | Per-image TrueSkill ratings (μ, σ, 0–10 score) |
| `data/training_features/Features.csv` | Training-set visual features |
| `data/inference_features/Features.csv` | City-scale inference visual features |
| `data/training_features/TrainingFeatures_{dimension}.csv` | Features merged with TrueSkill scores for training |
| `data/data.csv` / `data_final_rescaled.csv` | Citywide predicted perception scores per WVI (regenerated by Code 4) |
| `data/training_images/WVI_Processed/`, `WVI_Segmentation/` | Processed (256 px) training images + masks — **on Hugging Face** |
| `data/inference_images/WVI_Processed.zip` | Processed citywide WVIs (12,334; zipped) — **on Hugging Face** |
| `model_outputs/**/best_model_{dimension}.pth` | Trained weights — **on Hugging Face** |

## Data and model availability

To support reproducibility, the project is released across two repositories:

- **Code repository (this GitHub repo)** — the full pipeline (Code 1–7) and pre-processing scripts; the image-derived **feature tables** (training and citywide); the nested **H3 spatial units** (`metadata/`) and **cross-validation fold assignments**; and the **anonymised perception data** (pairwise responses, TrueSkill scores, and citywide predicted scores).
- **Dataset repository on Hugging Face** — [`sijiey/City-Landscape-In-Sight`](https://huggingface.co/datasets/sijiey/City-Landscape-In-Sight) — the larger binary artefacts: the **processed window view images** (499 surveyed as individual files + masks; the 12,334 citywide as `inference_images/WVI_Processed.zip`) and the **trained model weights** for all six perceptual dimensions.
- **Not redistributed** — the **raw** window view images (`WVI_Original`) obtained from the listing platform, owing to platform licensing restrictions. The Code 2 processing scripts regenerate the processed imagery from source.

## Citation

If you use this code, data, or models, please cite:

Peng C, Yang S, Liu A, Xiang Y, Zhou Z, Biljecki F (2026): City landscape in sight: A crowdsourced framework for unlocking urban-scale window view perceptions from real estate imagery. *Landscape and Urban Planning* 275: 105734. https://doi.org/10.1016/j.landurbplan.2026.105734

```bibtex
@article{peng2026citylandscape,
	author = {Peng, Chucai and Yang, Sijie and Liu, Ang and Xiang, Yang and Zhou, Zhixiang and Biljecki, Filip},
	doi = {10.1016/j.landurbplan.2026.105734},
	journal = {Landscape and Urban Planning},
	pages = {105734},
	title = {City landscape in sight: A crowdsourced framework for unlocking urban-scale window view perceptions from real estate imagery},
	volume = {275},
	year = {2026}
}
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

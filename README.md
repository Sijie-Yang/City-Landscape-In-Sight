<div align="center">

# City Landscape In Sight

**A Crowdsourced Framework for Unlocking Urban-Scale Window View Perceptions from Real Estate Imagery**

**Authors:** [Chucai Peng](https://ual.sg/author/chucai-peng/)†, [Sijie Yang](https://sijie-yang.com)†, Ang Liu, Yang Xiang, Zhixiang Zhou, [Filip Biljecki](https://filipbiljecki.com)*

by [Urban Analytics Lab](https://ual.sg), Department of Architecture, College of Design and Engineering, National University of Singapore

(† co-first authors, * corresponding author)

</div>

---


<img src="figures/fig_abstract.jpg" width="800" alt="Abstract">

## Overview

This repository contains the code and data for a crowdsourced framework that leverages real estate imagery to capture urban-scale window view perceptions (WVI). The framework combines crowdsourced perception surveys, machine learning models, and geospatial analytics to quantify and analyze how people perceive urban window views across a city.

## Repository Structure

```
├── code_1_perception_survey_results.ipynb   # Analysis of crowdsourced perception survey results
├── code_2_perception_model_train_predict.ipynb  # Perception model training and prediction
├── code_3_wvi_perception_data_analytics.ipynb   # Urban-scale WVI perception data analytics
├── code_4_inference_analytics.ipynb         # Inference and downstream analytics
├── data/
│   └── data_final.csv                       # Final perception and geospatial data for each WVI
├── figures/
│   └── fig_abstract.jpg                     # Abstract figure
└── perception_prediction/                   # Model outputs and prediction results
```

## Usage

Each `.ipynb` notebook can be run independently. Run them in order (1 → 4) for a full reproduction of the analysis pipeline:

1. **Code 1** — Survey results: processes and visualizes the crowdsourced perception survey data.
2. **Code 2** — Model training: trains and evaluates the window view perception prediction model.
3. **Code 3** — Data analytics: runs urban-scale analytics on the WVI perception dataset.
4. **Code 4** — Inference analytics: applies the model for city-wide inference and downstream analysis.

## Data

- `data/data_final.csv`: The main dataset containing final perception scores and geospatial attributes for each Window View Image (WVI).

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

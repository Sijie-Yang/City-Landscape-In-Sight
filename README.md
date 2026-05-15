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

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

</div>

<div align="center">
<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
<img src="figures/DoA Logo.jpg" alt="DoA Logo" width="120"/>
<img src="figures/UAL Logo.jpg" alt="UAL Logo" width="120"/>
</div>
<a href="https://ual.sg">Urban Analytics Lab</a> | National University of Singapore
</div>

---

<div align="center">
<img src="figures/fig_abstract.jpg" width="800" alt="Abstract">
</div>

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

# Spatial block K-fold (primary)

Full hybrid model (ResNet-50 + all tabular features) trained on **hexagon-level** frozen splits from `data/training_features/kfold_splits_spatial/` (Code 3).

- Checkpoints: `best_model_{dim}.pth`, `aux_scaler_{dim}.joblib`
- K-fold logs: `kfold_cv_{dim}.csv`, `kfold_cv_summary.csv`
- Multi-model benchmark tables: `model_comparison_kfold_*`

Used for inference (Code 4 §9) and city-scale scoring.

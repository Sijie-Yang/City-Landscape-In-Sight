# Pathway ablation (spatial folds)

Same **spatial block** K-fold splits as `../kfold_spatial/` (`KFOLD_SPLITS_SPATIAL`).

## Configs

| Subfolder | Model | Backend | Floor |
|-----------|--------|---------|-------|
| `resnet50_only/` | ResNet-50 only | PyTorch | — |
| `semantic_only/` | Semantic ratios | **Ridge** | ✓ |
| `colour_only/` | Colour/texture | **Ridge** | ✓ |
| `semantic_colour/` | Semantic + colour | **Ridge** | ✓ |
| `resnet50_semantic/` | ResNet-50 + semantic | PyTorch | ✓ |
| `resnet50_colour/` | ResNet-50 + colour | PyTorch | ✓ |
| `resnet50_semantic_colour_no_floor/` | ResNet-50 + semantic + colour | PyTorch | ✗ |
| `full` | See `../kfold_spatial/` (not duplicated here) | PyTorch | ✓ |

Tabular-only rows use Ridge (`alpha=1.0`, same as §7 benchmark). CSVs include `backend=ridge`.

`SKIP_ABLATION_IF_EXISTS=True` in Code 4 §6 skips configs with complete Ridge CSVs; legacy MLP outputs (no `backend` column) are re-trained automatically.

Summary: `ablation_spatial_summary.csv`

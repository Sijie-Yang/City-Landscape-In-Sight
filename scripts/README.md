# Local scripts (not part of public code_1–4 pipeline)

Run from **repository root**:

| Script | Purpose |
|--------|---------|
| `masked.py` | Apply window mask → `_work_masked/` |
| `masked_cut.py` | Crop non-black bbox → `_work_masked_cut/` |
| `data_mini.py` | Thumbnail to 256 px → `WVI_Processed/` |
| `perception_iteration.py` | Core: flip → TrueSkill → K-fold retrain loop (local tooling) |
| `run_auto_iteration.py` | CLI wrapper for automated label-adjustment rounds |

```bash
# Frozen k-fold manifests: export in Code 3 (`kfold_splits/` + `kfold_splits_spatial/`)

# Automated label adjustment (optional local workflow)
python scripts/run_auto_iteration.py --iteration 2
```

`perception_iteration.py` can also be run directly (`python scripts/perception_iteration.py`) after Code 2 checkpoints exist in `model_outputs/`.

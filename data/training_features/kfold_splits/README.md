# Frozen k-fold splits (iteration_02 / Code 3)

Exported by `scripts/export_kfold_splits.py` from stratification scores in:

`data/training_features/TrainingFeatures_{dim}.csv`

- **seed** = 42, **n_folds** = 5
- Score bins: [0,1), [1,2), [2,3), [3,4), [4,5]

## Files

| File | Purpose |
|------|---------|
| `kfold_split_{dim}.json` | Full manifest: row indices + **ID lists** + per-sample scores |
| `kfold_split_{dim}.csv` | Long table: fold, split (train/val/test), ID |

## After you change `raw/`

Regenerating `training_features/` changes **labels** (y) but these folds stay valid if you:

1. Keep the same 499 image **IDs**, and
2. Still stratify on the **frozen** Code 1 scores in this export (or the same `stratify_source` CSV).

In training code:

```python
import sys
sys.path.insert(0, "scripts")
from export_kfold_splits import align_folds_to_dataframe
import pandas as pd

df = pd.read_csv("path/to/TrainingFeatures_prefer.csv")
folds = align_folds_to_dataframe(df, "prefer")  # indices for this df's row order
```

Do **not** re-run StratifiedKFold on adjusted scores if you want comparable test R² to iteration_02.

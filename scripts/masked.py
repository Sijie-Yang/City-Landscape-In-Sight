"""Apply window-glass masks to original listing photos (mask → black background)."""

from __future__ import annotations

import os
from pathlib import Path

import cv2
import numpy as np
from tqdm.auto import tqdm


def resolve_mask_path(mask_dir: str | os.PathLike, image_filename: str) -> Path:
    """Return mask path ``{id}_mask.png`` (or ``{id}_mask.jpg``) under ``mask_dir``."""
    stem = Path(image_filename).stem
    if stem.endswith("_mask"):
        stem = stem[: -len("_mask")]
    mask_dir = Path(mask_dir)
    for ext in (".png", ".jpg", ".jpeg"):
        path = mask_dir / f"{stem}_mask{ext}"
        if path.exists():
            return path
    raise FileNotFoundError(f"No mask for {stem} (expected {stem}_mask.png) in {mask_dir}")


def apply_masked(original_path: str | os.PathLike, mask_path: str | os.PathLike, output_path: str | os.PathLike) -> None:
    """Keep pixels where the binary mask is 0 (outdoor view); zero out the rest."""
    original_path = Path(original_path)
    mask_path = Path(mask_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    original_img = cv2.imread(str(original_path))
    mask_img = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)
    if original_img is None:
        raise FileNotFoundError(f"Error reading original image: {original_path}")
    if mask_img is None:
        raise FileNotFoundError(f"Error reading mask image: {mask_path}")

    h, w = original_img.shape[:2]
    if mask_img.shape[:2] != (h, w):
        mask_img = cv2.resize(mask_img, (w, h), interpolation=cv2.INTER_NEAREST)

    _, mask_img = cv2.threshold(mask_img, 127, 255, cv2.THRESH_BINARY)
    black_background = np.zeros_like(original_img)
    masked_img = np.where(mask_img[..., None] == 0, original_img, black_background)
    cv2.imwrite(str(output_path), masked_img)


def _list_images(directory: Path, suffixes: tuple[str, ...]) -> list[Path]:
    return sorted(
        p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in suffixes
    )


def process_masked_directory(
    original_dir: str | os.PathLike,
    mask_dir: str | os.PathLike,
    output_dir: str | os.PathLike,
    *,
    suffixes: tuple[str, ...] = (".jpg", ".jpeg", ".png"),
    desc: str = "masked",
) -> int:
    """Mask every image in ``original_dir``; return count written."""
    original_dir = Path(original_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = _list_images(original_dir, suffixes)
    for path in tqdm(paths, desc=desc, unit="img"):
        mask_path = resolve_mask_path(mask_dir, path.name)
        out_name = path.stem + ".jpg"
        apply_masked(path, mask_path, output_dir / out_name)
    return len(paths)


if __name__ == "__main__":
    _original = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data2"
    _mask = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/mask"
    _output = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data_masked"
    count = process_masked_directory(_original, _mask, _output)
    print(f"Masked {count} images → {_output}")

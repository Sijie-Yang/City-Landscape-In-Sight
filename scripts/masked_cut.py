"""Crop to the bounding box of non-black pixels and resize back to the original canvas size."""

from __future__ import annotations

import os
from pathlib import Path

import cv2
import numpy as np
from tqdm.auto import tqdm


def fill_black_areas(image_path: str | os.PathLike, save_path: str | os.PathLike) -> None:
    """Crop non-black region, then resize back to the input image dimensions."""
    image_path = Path(image_path)
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coords = np.column_stack(np.where(gray != 0))
    if coords.size == 0:
        cv2.imwrite(str(save_path), image)
        return

    (x0, y0), (x1, y1) = coords.min(axis=0), coords.max(axis=0)
    cropped_image = image[x0 : x1 + 1, y0 : y1 + 1]
    filled_image = cv2.resize(
        cropped_image, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_LINEAR
    )
    cv2.imwrite(str(save_path), filled_image)


def _list_images(directory: Path, suffixes: tuple[str, ...]) -> list[Path]:
    return sorted(
        p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in suffixes
    )


def process_masked_cut_directory(
    input_dir: str | os.PathLike,
    output_dir: str | os.PathLike,
    *,
    suffixes: tuple[str, ...] = (".jpg", ".jpeg", ".png"),
    desc: str = "masked_cut",
) -> int:
    """Run ``fill_black_areas`` on every image in ``input_dir``; return count written."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = _list_images(input_dir, suffixes)
    for path in tqdm(paths, desc=desc, unit="img"):
        fill_black_areas(path, output_dir / path.name)
    return len(paths)


if __name__ == "__main__":
    _input = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data_masked"
    _output = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data_masked_cut"
    count = process_masked_cut_directory(_input, _output)
    print(f"Cropped {count} images → {_output}")

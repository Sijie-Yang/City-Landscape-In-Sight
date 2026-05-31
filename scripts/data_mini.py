"""Thumbnail images to a maximum side length (default 256 px) with aspect ratio preserved."""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image
from tqdm.auto import tqdm

try:
    _RESAMPLE = Image.Resampling.LANCZOS
except AttributeError:
    _RESAMPLE = Image.LANCZOS


def resize_image(image: Image.Image, max_size: tuple[int, int] = (256, 256)) -> Image.Image:
    """Return a copy thumbnail-resized to fit within ``max_size``."""
    out = image.copy()
    out.thumbnail(max_size, _RESAMPLE)
    return out


def mini_image_file(
    image_path: str | os.PathLike,
    save_path: str | os.PathLike,
    max_size: tuple[int, int] = (256, 256),
) -> None:
    """Load, thumbnail, and save one image."""
    image_path = Path(image_path)
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(image_path) as img:
        resize_image(img.convert("RGB"), max_size).save(save_path)


def _list_images(directory: Path, suffixes: tuple[str, ...]) -> list[Path]:
    return sorted(
        p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in suffixes
    )


def process_mini_directory(
    input_dir: str | os.PathLike,
    output_dir: str | os.PathLike,
    max_size: tuple[int, int] = (256, 256),
    *,
    suffixes: tuple[str, ...] = (".jpg", ".jpeg", ".png"),
    desc: str = "data_mini",
) -> int:
    """Thumbnail every image in ``input_dir``; return count written."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = _list_images(input_dir, suffixes)
    for path in tqdm(paths, desc=desc, unit="img"):
        out_name = path.stem + ".jpg"
        mini_image_file(path, output_dir / out_name, max_size=max_size)
    return len(paths)


if __name__ == "__main__":
    _input = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data_masked_cut"
    _output = "G:/My Drive/Research/2024_Chucai_Windowscape/ConvNeXt-WindowScenes/data_mini_masked_cut"
    count = process_mini_directory(_input, _output)
    print(f"Thumbnailed {count} images → {_output}")

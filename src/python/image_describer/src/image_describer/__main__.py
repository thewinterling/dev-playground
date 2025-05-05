import logging
from pathlib import Path

import click

from image_describer.describer import Describer


@click.group()
def cli():
    """Describe one or many images."""
    pass


@cli.command()
@click.option(
    "--images_folder",
    type=Path,
    help="Path to the data folder containing the image(s).",
)
def describe(images_folder: Path):
    """Generate detailed captions for one given image."""
    image_paths = list(images_folder.glob("*.jpg"))
    describer = Describer(images=image_paths)
    captions = describer.describe_images()
    for image_name, caption in captions.items():
        print(f"{image_name}: \t{caption}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    cli()

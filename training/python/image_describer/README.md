# Image describer

The package bundles a few files to have an easy-to-use image describer.

## Install

Everything handeled by the top-level `pyproject.toml` already.

## How to use

```bash
$ python -m image_describer describe --help
Usage: python -m image_describer describe [OPTIONS]

  Generate detailed captions for one given image.

Options:
  --images_folder PATH  Path to the data folder containing the image(s).
  --help                Show this message and exit.
```

You can pass any folder to the describer. If you wish to have the images
close to the script, put them in `image_describer/data` - there is a `.gitignore`
for that folder such that the images do not per accident get added to git.

```bash
$ python -m image_describer describe --images_folder image_describer/data/
image_describer/data/test_001.jpg:   a police car is parked on the side of the road
image_describer/data/test_002.jpg:   a white and blue sky
```

Run the tests via `pytest`:

```bash
pytest tests
```

TODO: bazelize the module to make its usage/test easier (i.e. executable from everywhere, tests integrated to CI)
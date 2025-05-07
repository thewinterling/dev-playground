import pytest
from image_describer.describer import Describer


@pytest.fixture
def image_url():
    return "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"


def test_describer_instantiation_works_without_errors(image_url: str):
    images = [image_url]
    describer = Describer(images=images)

    # Check if it is properly instantiated, mostly a dummy check since otherwise we would not get here.
    assert isinstance(describer, Describer)

    # Ensure that the model is actually loaded correctly (either cpu or cuda).
    # Note that we access the (private) model attribute here. We do not want to expose the model
    # in the public API, but we want to check here if it is loaded correctly.
    assert describer._model.device.type == describer.runs_on


def test_describer_describe_images_works_without_errors(image_url: str):
    images = [image_url]
    describer = Describer(images=images)
    captions = describer.describe_images()

    # By testing that we got something back, we know that the model inference did not fail.
    assert isinstance(captions, dict)

    # We only have one image, so we should only get one caption back.
    assert len(captions) == 1


def test_describer_describe_images_does_not_fail_on_empty_image_list():
    # Not providing any images is certainly semantically not a use-case, however, we do not want the program to fail.
    images = []
    describer = Describer(images=images)
    captions = describer.describe_images()

    # No images, no captions.
    assert len(captions) == 0

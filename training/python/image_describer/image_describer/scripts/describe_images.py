import torch
import click
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image

# Load the BLIP-2 model and processor
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b").to(
    device
)


def describe_image(image_path):
    """Generate a detailed caption for an image using BLIP-2 and OpenCV"""
    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        images=image, text="Describe this image in detail.", return_tensors="pt"
    ).to(device)
    with torch.no_grad():
        caption = model.generate(**inputs, max_new_tokens=50)

    description = processor.tokenizer.decode(caption[0], skip_special_tokens=True)
    return description


@click.command()
@click.option(
    "--image_path", type=click.Path(exists=True), help="Path to the image to describe."
)
@click.option(
    "--prompt",
    default="Describe this image in detail.",
    help="Prompt for the image description.",
)
def single_image(image_path, prompt):
    """Generate a detailed caption for the given image."""
    caption = describe_image(image_path, prompt)
    print("Generated Description:", caption)


if __name__ == "__main__":
    single_image()

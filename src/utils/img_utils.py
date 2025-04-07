from io import BytesIO

from PIL import Image


def reduce_image_size(
    image: Image.Image, quality: int = 100, max_size=(1200, 1200)
) -> Image.Image:
    """
    Resize an image while preserving the aspect ratio, using a thumbnail method.
    The resized image is then saved to an in-memory buffer (JPEG) using the provided quality.
    """
    img = image.copy()
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    buffer = BytesIO()
    img = img.convert("RGB")
    img.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    return Image.open(buffer)


def convert_alpha_to_white(image: Image.Image) -> Image.Image:
    # Create a white background image the same size as the original image
    white_background = Image.new("RGBA", image.size, "WHITE")

    # Paste the image on top of the white background image, using itself as the mask
    white_background.paste(image, (0, 0), image)

    # Convert to RGB mode (to remove alpha channel)
    white_background = white_background.convert("RGB")

    return white_background

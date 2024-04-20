from PIL import Image


def add_images_mod256(image1_path, image2_path, output_path):
    """
    This function reads two images, adds their corresponding pixels element-wise,
    performs modulo 256 operation, and saves the result as a new image.

    Args:
        image1_path (str): Path to the first image file.
        image2_path (str): Path to the second image file.
        output_path (str): Path to save the resulting image.
    """
    # Open images
    image1 = Image.open(image1_path).convert('L')  # Convert to grayscale
    image2 = Image.open(image2_path).convert('L')  # Convert to grayscale

    # Ensure images have the same dimensions
    if image1.size != image2.size:
        raise ValueError("Images must have the same dimensions")

    # Add corresponding pixels and perform modulo 256
    result_image = Image.new("L", image1.size)
    for x in range(image1.width):
        for y in range(image1.height):
            pixel_value = (image1.getpixel((x, y)) + image2.getpixel((x, y))) % 256
            result_image.putpixel((x, y), pixel_value)

    # Save the result
    result_image.save(output_path)


# Example usage
image1_path = "first.png"
image2_path = "second.png"
output_path = "result.png"
add_images_mod256(image1_path, image2_path, output_path)

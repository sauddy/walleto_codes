from PIL import Image, ImageDraw, ImageFont
import argparse


def generate_image(
    text,
    output_file="output_image.png",
    horizontal="h",
    border_thickness=5,
    border_color="#DC143C",
    padding=20,
    border_radius=20,
):
    """
    Generates an image with text and a rounded rectangle border with white space padding.

    Args:
    - text (str): The text to display.
    - output_file (str): Filename for the output image.
    - horizontal (str): "h" for horizontal, "v" for vertical orientation.
    - border_thickness (int): Thickness of the border line.
    - border_color (str): Color of the border.
    - padding (int): Space between text and the border.
    - border_radius (int): Radius for the rounded corners.
    """
    if horizontal == "h":
        text_width, text_height = 400, 250
    else:
        text_width, text_height = 250, 400

    font_size = 30
    background_color = "white"
    text_color = "#757575"
    # text_color = "#E2333333"

    # Calculate total image size including padding and border space
    width = text_width + 2 * padding
    height = text_height + 2 * padding

    # Create a blank image with a white background
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_path = (
        "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"  # Update if needed
    )

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Font not found. Using default font.")
        font = ImageFont.load_default()

    # Function to wrap text within the max width
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split(" ")
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            text_width, _ = draw.textbbox((0, 0), test_line, font=font)[2:]
            if text_width <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)
        return lines

    # Wrap text if necessary
    lines = wrap_text(text, font, text_width - 40)

    # Calculate total text height to center vertically
    line_height = font.getbbox(text)[3]  # Get text height using bbox
    total_text_height = len(lines) * line_height
    y_start = (height - total_text_height) / 2

    # Draw each line of text
    for line in lines:
        text_width_actual, _ = draw.textbbox((0, 0), line, font=font)[2:]
        x = (width - text_width_actual) / 2
        draw.text((x, y_start), line, font=font, fill=text_color)
        y_start += line_height

    # Draw the rounded rectangle border
    border_start = padding // 2  # Start border slightly inside the padding region
    border_end_x = width - border_start
    border_end_y = height - border_start

    draw.rounded_rectangle(
        [(border_start, border_start), (border_end_x, border_end_y)],
        outline=border_color,
        width=border_thickness,
        radius=border_radius,  # Rounded corner radius
    )

    # Save the image
    image.save(output_file)
    print(f"Image saved as {output_file}")


def get_args():
    parser = argparse.ArgumentParser(
        description="Generate an image with text and a rounded border."
    )
    parser.add_argument(
        "--text", default="Hello World", type=str, help="Text to display on the image."
    )
    parser.add_argument(
        "--output",
        default="output_image.png",
        type=str,
        help="Filename for the output image.",
    )
    parser.add_argument(
        "--dim", type=str, choices=["h", "v"], default="h", help="Image orientation."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    generate_image(args.text, args.output, args.dim)

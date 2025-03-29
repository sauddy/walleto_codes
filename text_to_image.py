from PIL import Image, ImageDraw, ImageFont
import argparse

def generate_image(text, output_file="output_image.png", horizontal= "h"):
    if horizontal == "h":
        # Set image dimensions and properties
        width, height = 400, 250
    else:
        width, height = 250, 400


    font_size=30
    background_color = "white"
    text_color = "#DC143C"  ## DC14C3

    # Create a blank image with a white background
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font_path = "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"  # Update the font path if needed
    # Define font (use a comic-like font or fallback to default)
    # Try to load the font and handle error if not available
    try:
        font = ImageFont.truetype(font_path, font_size)
        print(f"Using font {font_path} with size {font_size}")
    except IOError:
        print(f"Font not found. Using default font.")
        font = ImageFont.load_default()

    # Function to add line breaks if text is too long
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split(' ')
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

    # Wrap text if it's too wide
    lines = wrap_text(text, font, width - 40)

    # Calculate total text height to center vertically
    line_height = font.getbbox(text)[3]  # Get the height of the text using bbox (y-dimension)
    total_text_height = len(lines) * line_height
    y = (height - total_text_height) / 2

    # Draw each line on the image
    for line in lines:
        text_width, _ = draw.textbbox((0, 0), line, font=font)[2:]
        x = (width - text_width) / 2
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_height

    # Save the image
    image.save(output_file)
    print(f"Image saved as {output_file}")

def get_args():
    parser = argparse.ArgumentParser(description="Generate an image with text.")
    parser.add_argument("--text", default="Hello World", type=str, help="Text to display on the image.")
    parser.add_argument("--output", default="output_image.png", type=str, help="Filename for the output image.")
    parser.add_argument("--dim",  type=str,choices=["h","v"], default="h",help="Filename for the output image.")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    generate_image(args.text, args.output, args.dim)

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import re, os


# Function to find optimal font size
def get_optimal_font_size(draw, text, font_path, max_width, initial_size=40):
    """Adjust font size dynamically to fit within max_width."""
    font_size = initial_size
    font = ImageFont.truetype(font_path, font_size)

    while True:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:
            return font  # Return the font object with the right size
        else:
            font_size -= 1  # Reduce font size if text is too wide
            font = ImageFont.truetype(font_path, font_size)


# Function to generate image
def create_image(background_color, text, text_color, filename="output.png"):
    # Image size (width, height)
    width, height = 400, 250
    text = text  # + " membership"

    # Create an image with the given background color
    img = Image.new("RGB", (width, height), color=background_color)

    # Set up drawing context
    draw = ImageDraw.Draw(img)

    # Correct font path based on macOS system fonts
    font_path = (
        "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"  # Update if needed
    )

    # Get optimal font size
    max_text_width = int(width * 0.9)  # Allow some margin
    font = get_optimal_font_size(draw, text, font_path, max_text_width)

    # Calculate text size and position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    # position = ((width - text_width) // 4, height // 4 - text_height // 1)
    position = (width // 14, height // 10)

    # Draw the text on the image
    draw.text(position, text, fill=text_color, font=font)

    # Save the image
    img.save(filename)


# Read CSV file
df = pd.read_csv("data_walleto.csv")
os.makedirs("Merchant_logo", exist_ok=True)

# Loop through each row and create images
for index, row in df.iterrows():
    background_color = row["background_color"]
    text = row["text"]
    text_color = row["text_color"]
    # Sanitize filename by removing spaces and special characters
    file_name = re.sub(
        r"\W+", "_", text
    )  # Replace non-alphanumeric characters with underscores

    # Generate and save the image with an adaptive font size
    create_image(
        background_color,
        text,
        text_color,
        # filename=f"image_{index+1}.png",
        filename=f"Merchant_logo/image_{file_name}.png",
    )
    print(f"Image {file_name} saved.")

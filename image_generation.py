from PIL import Image, ImageDraw, ImageFont
import pandas as pd


# Function to generate image
def create_image(
    background_color, text, text_color, font_size=40, filename="output.png"
):
    # Image size (width, height)
    width, height = 400, 250

    text = text + " membership"

    # Create an image with the given background color
    img = Image.new("RGB", (width, height), color=background_color)

    # Set up drawing context
    draw = ImageDraw.Draw(img)

    # Correct font path based on macOS system fonts
    font_path = "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"  # Update the font path if needed

    # Try to load the font and handle error if not available
    try:
        font = ImageFont.truetype(font_path, font_size)
        print(f"Using font {font_path} with size {font_size}")
    except IOError:
        print(f"Font not found. Using default font.")
        font = ImageFont.load_default()

    # Calculate text size and position (centered) using textbbox method
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 6, (height - text_height) // 6)

    # Draw the text on the image
    draw.text(position, text, fill=text_color, font=font)

    # Save the image
    img.save(filename)


# Read CSV file
df = pd.read_csv("data.csv")

# Loop through each row and create images
for index, row in df.iterrows():
    background_color = row["background_color"]
    text = row["text"]
    text_color = row["text_color"]

    # Generate and save the image with a custom font size
    create_image(
        background_color,
        text,
        text_color,
        font_size=25,
        filename=f"image_{index+1}.png",
    )
    print(f"Image {index+1} saved.")


# Text-to-Image Generator

1. This Python script (text_to_image.py) generates an image with custom text provided via the command line. The generated image has a **white background** with the text in **red color** using a comic-style font.
2. This Python script (brand_image_generator.py) generates multiple images while reading the text from the .csv file which has the "background_color","text","text_color" as the column header

## 🚀 Features 1
- Generates an image with user-provided text.
- Automatically wraps text to fit within the image dimensions.
- Centers text horizontally and vertically.
- Saves the image as `output_image.png` by default.

## 🚀 Features 2
- Generates iamges from user-provided brand names from the .csv.
- Selects the the text and the background color from the .csv

---

## 📚 Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- Pillow (PIL)

### Install Dependencies
## It is recommended that you create a virtual env (You can create the 'venv' a directory above your git code directory)
```bash
   python3 -m venv walleto_env
```
To activate the env --> On Linux/MacOS:
```bash
source walleto_env/bin/activate
```
Once the env is activated You can install the required dependencies by running:
<!-- ```bash
pip install -e .  
``` -->
# pip
pip install pillow

---

If any library is missing, please pip install (make sure your evn is activated)

## 📝 Usage

Run the script from the command line with the following syntax:


### Example 1
```bash
python text_to_image.py --text "Hello, World!" --dim 'v' --output 'story1.png'
```
The generated image will be saved as `story1.png` in the same directory --dim 'v' or --dim 'h' gives the orientation

## ⚙️ Command-Line Arguments

| Argument      | Description                       | Default         |
|---------------|-----------------------------------|-----------------|
| `--text`      | Text to be printed on the image   | "Hello World"   |
| `--dim`       | orientation horizontal/vertical   |      "h"         |
| `--output`]   | file name                         | "output_image.png" |

### Example 2
```bash
python brand_image_generation.py
```
This generates all the images correspoding to the brands once the text, background color and the text color are given on the csv


---



---

## 🖼️ Output

- The image is generated with:
    - **Background color:** White  
    - **Text color:** Red  
    - **Font:** Comic Sans MS (if available) or default system font.

---

## 🛠️ Font Configuration

To use a custom font (such as Comic Sans), make sure the `ComicSansMS.ttf` file is present in the same directory or modify the font path in the script:

```python
font = ImageFont.truetype("ComicSansMS.ttf", size=50)
```

If the font is not found, the script falls back to the default font.



Happy coding! 🎨😊



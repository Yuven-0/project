import os
from PIL import Image

# List of files to check
files_to_check = [
    "Dr_Shashi_Tharoor.jpg",
    "Lab 5-Spring 2025.ipynb",
    "MLPR Prep Assignment - Distance Based Classification.pdf",
    "Plaksha_Faculty.jpg"
]

def check_file_exists(filename):
    """Check if a file exists."""
    if os.path.exists(filename):
        print(f"✅ {filename} exists.")
        return True
    else:
        print(f"❌ {filename} is missing!")
        return False

def check_image(filename):
    """Check if an image file can be opened."""
    try:
        with Image.open(filename) as img:
            img.verify()  # Verify if it's a valid image
        print(f"✅ {filename} is a valid image.")
    except Exception as e:
        print(f"❌ Error opening {filename}: {e}")

def check_pdf(filename):
    """Check if a PDF is accessible (basic check only)."""
    try:
        with open(filename, "rb") as f:
            if f.read(4) == b"%PDF":
                print(f"✅ {filename} is a valid PDF.")
            else:
                print(f"❌ {filename} is not a valid PDF.")
    except Exception as e:
        print(f"❌ Error opening {filename}: {e}")

def check_notebook(filename):
    """Basic check to see if a Jupyter Notebook file is readable."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            if '"cells"' in content and '"metadata"' in content:
                print(f"✅ {filename} is a valid Jupyter Notebook.")
            else:
                print(f"❌ {filename} does not appear to be a valid Jupyter Notebook.")
    except Exception as e:
        print(f"❌ Error opening {filename}: {e}")

# Run checks
for file in files_to_check:
    if check_file_exists(file):
        if file.endswith((".jpg", ".png")):
            check_image(file)
        elif file.endswith(".pdf"):
            check_pdf(file)
        elif file.endswith(".ipynb"):
            check_notebook(file)

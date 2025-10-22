# ui_generator.py
# ========================
# AI Chatbot - UI Generator
# ========================

import os
import random
from config import *

# ------------------------
# AI Image Storage
# ------------------------
# All generated images are stored in IMAGES_DIR
def get_image_path(filename):
    return os.path.join(IMAGES_DIR, filename)

# ------------------------
# Placeholder Image Generation
# ------------------------
def generate_placeholder_image(description, filename):
    """
    Generates a placeholder text image (simulated for now).
    In a real implementation, this would call an AI image API.
    """
    path = get_image_path(filename)
    with open(path, "w") as f:
        f.write(f"IMAGE PLACEHOLDER: {description}\n")
    print(WHITE + f"[Generated placeholder image: {path}]" + RESET)
    return path

# ------------------------
# Main UI Generation
# ------------------------
def generate_ui_image(prompt, filename):
    """
    Simulated AI image generation function.
    Generates an image file in IMAGES_DIR based on the prompt.
    """
    # Simulate some loading
    loading_msg = random.choice(LOADING_MESSAGES)
    print(WHITE + f"{loading_msg} for UI element..." + RESET)
    # Simulate processing delay
    import time
    time.sleep(random.uniform(0.5, 1.5))
    # Create placeholder file
    return generate_placeholder_image(prompt, filename)

# ------------------------
# Generate Multiple UI Elements
# ------------------------
def generate_all_ui():
    """
    Generate all default UI elements listed in config UI_ELEMENTS
    """
    print(WHITE + "Generating all default UI elements..." + RESET)
    for name, prompt in UI_ELEMENTS.items():
        filename = f"{name}.png"
        generate_ui_image(prompt, filename)
    print(WHITE + "All UI elements generated!" + RESET)

# ------------------------
# Helper: List Existing UI Images
# ------------------------
def list_ui_images():
    """
    List all generated UI images in the images directory
    """
    files = os.listdir(IMAGES_DIR)
    if not files:
        print(WHITE + "No UI images found." + RESET)
    else:
        print(WHITE + "Existing UI images:" + RESET)
        for f in files:
            print(" - " + f)

# ------------------------
# Helper: Delete UI Image
# ------------------------
def delete_ui_image(filename):
    path = get_image_path(filename)
    if os.path.exists(path):
        os.remove(path)
        print(WHITE + f"Deleted {filename}" + RESET)
    else:
        print(WHITE + f"{filename} does not exist." + RESET)

# ------------------------
# Helper: Delete All UI Images
# ------------------------
def delete_all_ui():
    files = os.listdir(IMAGES_DIR)
    for f in files:
        delete_ui_image(f)
    print(WHITE + "All UI images deleted." + RESET)

# ------------------------
# Test / Example Usage
# ------------------------
if __name__ == "__main__":
    print(WHITE + "=== UI Generator Test ===" + RESET)
    # Generate individual UI element
    generate_ui_image("Black and white minimalistic Deliver button", "deliver_button.png")
    generate_ui_image("Black and white abstract Jazz icon", "jazz_icon.png")
    generate_ui_image("Black and white AI chatbot logo", "logo.png")
    generate_ui_image("Black and white loading spinner", "loading_spinner.png")
    # List UI images
    list_ui_images()
    # Generate all UI elements from config
    generate_all_ui()
    # Delete a single UI image
    delete_ui_image("deliver_button.png")
    # Delete all UI images
    delete_all_ui()
    print(WHITE + "=== UI Generator Test Complete ===" + RESET)


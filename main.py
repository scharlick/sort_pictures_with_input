import os
import shutil
import subprocess
from PIL import Image
# Hardcoded path to the directory containing images
directory = 'New folder'
# keep_directory = os.path.join('/', "keep")
keep_directory = 'keep'

def focus_terminal():
    try:
        script = 'tell application "Terminal" to activate'
        subprocess.run(["osascript", "-e", script])
    except Exception as e:
        print(f"Error bringing Terminal to foreground: {e}")

def process_images(directory, keep_directory):
    # Create the 'keep' directory in the working directory if it doesn't exist
    if not os.path.exists(keep_directory):
        os.makedirs(keep_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                img.show()

                focus_terminal()

                print(f"Processing {filename}. Press 1 to save, 2 to delete.")
                choice = input()

                if choice == '1':
                    print(f"Saving {filename}.")
                    shutil.move(image_path, os.path.join(keep_directory, filename))
                elif choice == '2':
                    print(f"Deleting {filename}.")
                    os.remove(image_path)
                else:
                    print("Invalid input. Skipping this image.")

if __name__ == "__main__":
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
    else:
        process_images(directory, keep_directory)
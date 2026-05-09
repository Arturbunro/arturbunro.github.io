import os
from PIL import Image

def convert_png_to_webp():
    """
    Iterates through each subdirectory of the current directory,
    looks for .png files, and converts them to .webp using the same base filename.
    """
    # Set the base directory as the current working directory
    base_dir = os.getcwd()

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        # Only process if it's a directory (subfolder)
        if os.path.isdir(folder_path):
            # Loop through the files in that subfolder
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(".png"):
                    # Full path to the current .png file
                    file_path = os.path.join(folder_path, file_name)

                    # Construct new .webp filename
                    new_file_name = os.path.splitext(file_name)[0] + ".webp"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    
                    # Open and convert the image
                    with Image.open(file_path) as img:
                        img.save(new_file_path, "webp")
                    
                    os.remove(file_path)

if __name__ == "__main__":
    convert_png_to_webp()

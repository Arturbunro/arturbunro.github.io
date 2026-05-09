#!/usr/bin/env python3
import os
import json

def main():
    base_dir = os.getcwd()  # current directory where the script is run
    output_data = {}

    # Iterate over all directories
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path) and folder.isdigit():  # Ensure folder names are numeric
            files_list = []
            # Iterate over each file in the folder
            for filename in sorted(os.listdir(folder_path)):  # Sort files alphabetically
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    # Convert filenames like "1.png" to "pic1.png"
                    if filename.endswith(".png"):
                        name, ext = os.path.splitext(filename)
                        new_filename = f"pic{name}{ext}"
                        files_list.append(new_filename)
                    else:
                        files_list.append(filename)

            # Add sorted folder contents to the dictionary
            output_data[int(folder)] = {"files": files_list}

    # Sort the dictionary by folder ID (numeric order)
    sorted_output = dict(sorted(output_data.items()))

    # Write the output data to a JSON file
    with open("output.json", "w") as json_file:
        json.dump(sorted_output, json_file, indent=2)

if __name__ == "__main__":
    main()

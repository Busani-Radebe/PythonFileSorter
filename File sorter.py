import os
import shutil

desktop_path = r"C:/"  # Replace with the actual path to your desktop

# Create a dictionary to map file extensions to folder names
extension_to_folder = {}

# Iterate over files on the desktop
for filename in os.listdir(desktop_path):
    if os.path.isfile(os.path.join(desktop_path, filename)):
        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Add the extension to the dictionary if it's not already present
        if extension not in extension_to_folder:
            folder_name = extension[1:].upper() + " Files"  # Create a folder name based on the extension
            extension_to_folder[extension] = folder_name

            # Create the folder if it doesn't exist
            folder_path = os.path.join(desktop_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        # Move the file to the corresponding folder
        file_path = os.path.join(desktop_path, filename)
        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)

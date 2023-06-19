# PythonFileSorter
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
This code snippet demonstrates a file organization script. It scans the specified desktop path for files and organizes them into folders based on their file extensions.

The import os statement allows you to use various operating system-related functions, such as manipulating file paths and working with directories.

The import shutil statement imports the shutil module, which provides functions for high-level file operations, including moving files.

The desktop_path variable holds the path to the desktop directory. Make sure to replace it with the actual path on your system.

The code utilizes a dictionary, extension_to_folder, to map file extensions to folder names. Each file extension encountered will be associated with a folder name, which will be created if it doesn't already exist.

The os.listdir(desktop_path) function returns a list of files and directories on the desktop. The code iterates over each item, and if it is a file (checked using os.path.isfile()), it proceeds to organize it.

By using os.path.splitext(filename), the code splits the file name and extension. The file extension is extracted and stored in the extension variable.

If the extension is not already in the extension_to_folder dictionary, a folder name is created based on the extension. The folder name is constructed by capitalizing the extension (excluding the leading dot) and appending " Files" to it.

The os.path.join(desktop_path, folder_name) function creates the full path to the folder on the desktop.

If the folder doesn't exist (os.path.exists(folder_path)), it is created using os.makedirs(folder_path).

Finally, the file is moved from the desktop to its corresponding folder using shutil.move(file_path, new_file_path). The file_path variable contains the current file's path, while new_file_path holds the path where the file should be moved.

Please note that this code snippet assumes you have the necessary permissions to modify files and folders on your desktop.

import os
import shutil

# Define the path to the directory
path = './fileOrganizer'

# List all files in the directory
file_name = os.listdir(path)

# Define a dictionary of file extensions and their corresponding directories
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'py': 'Python videos'
}

# Iterate over the file extensions
for file_extension in file_extensions:
    if file_extension == path:
        os.makedirs(path + file_extension, exist_ok=True)
    
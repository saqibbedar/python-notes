import os

# get path for reading file
file_path = os.path.join(".", "ReadMe.md") # get file path

content = ""
# open file in read mode
with open(file_path, "r") as file:
    content = file.read()  # read content

# path to write a file
generated_files_dir = os.path.join("./Python-2025/File-Handling", "00_generated_files")

# check if already file exist?
if not os.path.exists(generated_files_dir):
    os.makedirs(generated_files_dir)

with open(f"{generated_files_dir}/02_read_file.md", "w") as file:
    file.write(content)

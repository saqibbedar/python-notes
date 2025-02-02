import os

read_file_path = os.path.join("./Python-2025/File-Handling/00_generated_files", "03_binary_file.bin")

with open(read_file_path, "rb") as file:
    content = file.read()
    decoded_content = content.decode('utf-8') # convert to normal text
    print(decoded_content)

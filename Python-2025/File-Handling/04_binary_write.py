import os

binary_text = b"Hello, world"

file_path = os.path.join("./Python-2025/File-Handling", "00_generated_files")

if not os.path.exists(file_path):
    os.makedirs(file_path)

with open(f"{file_path}/03_binary_file.bin", "wb") as file:
    file.write(binary_text)


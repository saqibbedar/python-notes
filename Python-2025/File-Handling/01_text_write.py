import os

# Create a directory for generated files
generated_files = os.path.join("./Python-2025/File-Handling", "00_generated_files")

# Check if directory already exits?
if not os.path.exists(generated_files):
    os.makedirs(generated_files) # Create one if not exits

# Open file 
with open(f"{generated_files}/01_write_file.txt", "w") as file:
    file.write("Lorem ipsum dollar...")

# You have source_directory with nested directories (any level of nesting).
# In all those directories could be text files (with extension *.txt) and any other files.
# Create file combined_files.txt.
# For every text file in source_directory that smaller or equal to 120 bytes, add filename (without full path) and content to combined_files.txt
import os
from idlelib.iomenu import encoding

# Working with working directory
print(os.getcwd())
print(os.getcwd())


for dirpath, dirnames, filenames in os.walk('source_directory'):
    for file_name in filenames:
        print(file_name)
        if file_name.endswith('.txt'):
            with open (f'{dirpath}/{file_name}', 'r', encoding="utf-8") as f:
                with open('combined_files.txt', 'w', encoding="utf-8") as file:
                    file.writelines(file_name + ', ' + f.readline())


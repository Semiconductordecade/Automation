import os
import re

# Define paths to relevant files
#c_file_path = "FilePAth.c"
#h_file_path = "FilePAth.h"
inf_file_path = "Filepath.inf"

# Define patterns to search for and their corresponding replacements
patterns_replacements = {
    #r'existing_pattern2': 'replacement2',
    # Add more patterns and replacements as needed
}

# Function to replace patterns in a file
def replace_patterns_in_file(file_path, patterns_replacements):
    with open(file_path, 'r') as file:
        content = file.read()

    for pattern, replacement in patterns_replacements.items():
        content = re.sub(pattern, replacement, content)

    with open(file_path, 'w') as file:
        file.write(content)

# Modify .c file
#replace_patterns_in_file(c_file_path, patterns_replacements)

# Modify .h file
#replace_patterns_in_file(h_file_path, patterns_replacements)

# Modify .uni file
replace_patterns_in_file(inf_file_path, patterns_replacements)

print("Modification complete.")

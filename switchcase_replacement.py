import re

# Define path to the ASL file
asl_file_path = "path/to/your/asl/file.asl"

# Define the new case and its associated code block
new_case = "Case (3)\n{\n    // Code for case 3\n}\n"

# Function to add a new case to a switch statement in an ASL file
def add_new_case_to_asl_file(asl_file_path, new_case):
    with open(asl_file_path, 'r') as file:
        content = file.read()

    # Find the switch statement in the ASL file
    switch_pattern = re.compile(r'Switch\s*\(\s*Arg\s*\)\s*{\s*(.*?)\s*}', re.DOTALL)
    switch_match = switch_pattern.search(content)

    if switch_match:
        switch_statement = switch_match.group(0)

        # Append the new case to the switch statement
        modified_switch_statement = switch_statement.rstrip('}\n') + '\n' + new_case + '}\n'

        # Replace the original switch statement with the modified one
        modified_content = content.replace(switch_statement, modified_switch_statement)

        with open(asl_file_path, 'w') as file:
            file.write(modified_content)

        print("New case added successfully.")
    else:
        print("Switch statement not found in the ASL file.")

# Add the new case to the ASL file
add_new_case_to_asl_file(asl_file_path, new_case)

import os

# Get the current directory
current_dir = os.getcwd()

# Get a list of all files in the current directory
all_files = os.listdir(current_dir)

# Filter the list to include only Excel files
excel_files = [f for f in all_files if f.endswith('.xlsx')]

# Define the command to run for each Excel file
command = 'python plots.py';

# Iterate over each Excel file and run the command
for file_name in excel_files:
    # Print a message to indicate which file is being processed
    print(f"Processing file '{file_name}'...")
    
    # Run the command for the current file
    os.system(f"{command} {file_name}")
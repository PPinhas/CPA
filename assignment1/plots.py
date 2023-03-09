import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Check if the script was called with an argument
if len(sys.argv) == 2:
    # Get the argument from the command line
    filename = sys.argv[1]
    print(f"Argument: {filename}")
else:
    print("Usage: python myscript.py <argument>")
    exit()

#filename = '1.1000.1.xlsx'
directory_name = filename[:-5]

# Import CSV or Excel file and skip rows after first empty line
#df = pd.read_csv('your_file_name.csv', skip_blank_lines=True)
df = pd.read_excel(filename, index_col=None)

first_empty = df[df.isna().all(axis=1)].index[0]

# delete every line after the first empty line, including it
df = df.iloc[:first_empty]


# Get column names except the first one (horizontal axis)
column_names = df.columns[1:]

# Create a line plot for each column
if not os.path.exists(directory_name):
    # Create the directory if it doesn't exist
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
else:
    print(f"Directory '{directory_name}' already exists.")

for column in column_names:    
    plt.plot(df[df.columns[0]], df[column])
    plt.xlabel(df.columns[0])
    plt.ylabel(column)
    plt.xticks([])
    #plt.legend()
    plt.savefig(directory_name + '/' + column + '_plot.png') # Save each plot with column name
    plt.close()
    #plt.show()'''
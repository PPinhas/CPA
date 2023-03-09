import pandas as pd
import matplotlib.pyplot as plt
import os

# Set the path to the Excel file
#excel_file1 = "cpa_mult.xlsx"
#excel_file2 = "cpa_line.xlsx"

# Create a Pandas Excel file reader
#xl1 = pd.ExcelFile(excel_file1)
#xl2 = pd.ExcelFile(excel_file2)

sheets1 = ["1.1000.1.xlsx", "1.1000.2.xlsx", "1.1000.3.xlsx", "1.1400.1.xlsx", "1.1400.2.xlsx", "1.1400.3.xlsx", "1.2000.1.xlsx", "1.2000.2.xlsx", "1.2000.3.xlsx"]

sheets2 = ["2.1000.1.xlsx", "2.1000.2.xlsx", "2.1000.3.xlsx", "2.1400.1.xlsx", "2.1400.2.xlsx", "2.1400.3.xlsx", "2.2000.1.xlsx", "2.2000.2.xlsx", "2.2000.3.xlsx"]


# Loop through the first 9 sheets
for (sheet1, sheet2) in zip(sheets1, sheets2):
    # Create a new directory with the sheet name
    sheet_dir1 = sheet1.replace(" ", "_")
    sheet_dir2 = sheet2.replace(" ", "_")
    sheet_dir = sheet_dir1 + sheet_dir2
    os.makedirs(sheet_dir, exist_ok=True)

    # Read the sheet into a Pandas DataFrame
    df1 = pd.read_excel(sheet1)
    df2 = pd.read_excel(sheet2)

    # Get the name of the third column (x-axis)
    x_col1 = df1.columns[2]
    x_col2 = df2.columns[2]

    # Loop through each column in the DataFrame
    for (col1, col2) in zip(df1.columns, df2.columns):
        # Skip the x-axis column
        if col1 == x_col1:
            continue
        if col2 == x_col2:
            continue

        # Check if the column contains numeric values
        if pd.api.types.is_numeric_dtype(df1[col1]) and pd.api.types.is_numeric_dtype(df1[col2]):
            # Create a new plot for the column
            fig, ax = plt.subplots()

            # Plot the column against the x-axis
            #ax.plot(df1[x_col1], df1[col1])
            ax.plot(df1[x_col1], df1[col1], label=f"mult")
            #ax.plot(df2[x_col2], df2[col2])
            ax.plot(df2[x_col2], df2[col2], label=f"line")
            
            # Set the title and axis labels
            ax.set_title(f"{sheet1} vs {sheet2} - {col2}")
            ax.set_xlabel(x_col1)
            ax.set_ylabel(col1)
            ax.legend()
            # Save the plot to the sheet directory
            plot_file = os.path.join(sheet_dir, f"{col1}_plot.png")
            fig.savefig(plot_file)

            # Close the plot for the next column
            plt.close(fig)
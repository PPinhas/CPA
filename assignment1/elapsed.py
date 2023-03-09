import os
import glob
import pandas as pd

# Get a list of all .xlsx files in the current directory
xlsx_files = glob.glob("*.xlsx")

# Loop over each file
for file in xlsx_files:
    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel(file)



#Elapsed Time (sec)
#Cumulative Processor Energy_0(Joules)
#Cumulative Processor Energy_0(mWh)
#Cumulative IA Energy_0(Joules)
#Cumulative IA Energy_0(mWh)
#Cumulative DRAM Energy_0(Joules)
#Cumulative DRAM Energy_0(mWh)
#Cumulative GT Energy_0(Joules)
#Cumulative GT Energy_0(mWh)

    
    # Check if the 'elapsed time' column exists in the DataFrame
    if 'Elapsed Time (sec)' in df.columns:
        # Subtract the first value in the 'elapsed time' column from every value in that column
        elapsed_time_col = df['Elapsed Time (sec)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Elapsed Time (sec)'] = elapsed_time_col
        
        
    if 'Cumulative Processor Energy_0(Joules)' in df.columns:
        # Subtract the first value in the 'elapsed time' column from every value in that column
        elapsed_time_col = df['Cumulative Processor Energy_0(Joules)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative Processor Energy_0(Joules)'] = elapsed_time_col    
        
    if 'Cumulative Processor Energy_0(mWh)' in df.columns:
        elapsed_time_col = df['Cumulative Processor Energy_0(mWh)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative Processor Energy_0(mWh)'] = elapsed_time_col
        
    if 'Cumulative IA Energy_0(Joules)' in df.columns:
        elapsed_time_col = df['Cumulative IA Energy_0(Joules)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative IA Energy_0(Joules)'] = elapsed_time_col
        
    if 'Cumulative IA Energy_0(mWh)' in df.columns:
        elapsed_time_col = df['Cumulative IA Energy_0(mWh)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative IA Energy_0(mWh)'] = elapsed_time_col
        
    if 'Cumulative DRAM Energy_0(Joules)' in df.columns:
        elapsed_time_col = df['Cumulative DRAM Energy_0(Joules)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative DRAM Energy_0(Joules)'] = elapsed_time_col
        
    if 'Cumulative DRAM Energy_0(mWh)' in df.columns:
        elapsed_time_col = df['Cumulative DRAM Energy_0(mWh)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative DRAM Energy_0(mWh)'] = elapsed_time_col
        
    if 'Cumulative GT Energy_0(Joules)' in df.columns:
        elapsed_time_col = df['Cumulative GT Energy_0(Joules)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative DRAM Energy_0(Joules)'] = elapsed_time_col
        
    if 'Cumulative GT Energy_0(mWh)' in df.columns:
        elapsed_time_col = df['Cumulative GT Energy_0(mWh)']
        elapsed_time_col = elapsed_time_col - elapsed_time_col.iloc[0]
        df['Cumulative DRAM Energy_0(mWh)'] = elapsed_time_col
        
        
    # Save the modified DataFrame back to the Excel file
    with pd.ExcelWriter(file) as writer:
        df.to_excel(writer, index=False)
import pandas as pd
import numpy as np
from asammdf import MDF

def process_mf4_file(mf4_file_path, dbc_file_path, output_csv_path):
    # Read the MF4 file and merge with DBC file
    mdf = MDF(mf4_file_path)
    mdf_df = mdf.to_dataframe(buses=None, dbc=dbc_file_path, dbc_language='en')

    # Organize data using timestamps as the key
    mdf_df = mdf_df.pivot_table(index='Timestamp', columns='CAN_ID', values='Value')

    # Resample timestamps at 0.5 second intervals using the mean of previous values
    mdf_df = mdf_df.resample('0.5S').mean().ffill()

    # Save the results to a CSV file
    mdf_df.to_csv(output_csv_path)

    print(f"Processed CAN data has been successfully saved to {output_csv_path}")

if __name__ == "__main__":
    mf4_file_path = "path/to/your/mf4_file.MF4"  # Change this to the path of your MF4 file
    dbc_file_path = "path/to/your/dbc_file.dbc"  # Change this to the path of your DBC file
    output_csv_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the CSV file
    process_mf4_file(mf4_file_path, dbc_file_path, output_csv_path)

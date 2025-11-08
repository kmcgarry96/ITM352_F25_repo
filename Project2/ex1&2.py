# Read in a CSV file and create a dataframe.  Print some info.
# Pivot the dataframe to show total sales by order type.
# Calculate total sales per order.  Show average sales by state
# and sales type.
import pandas as pd
import numpy as np
import pyarrow 
import ssl
import time

# Temporary fix.  Don't do this in production code.
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)


def load_csv(file_path):
    print(f"Reading CSV file from {file_path}...")
    start_time = time.time()
    
    try:

        df = pd.read_csv(file_path, engine="pyarrow")
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}")

        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%y', errors='coerce')
        df.fillna(0, inplace=True)

        df['sales'] = df['quantity'] * df['unit_price']
        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check that the required columns are in df
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")
        return df

    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found. {e}")

    except pd.errors.EmptyDataError as e:
        print(f"Error: The file {file_path} is empty. {e}")
        return None
    
    except pd.errors.ParserError as e:
        print(f"Error: There was a parsing error while reading {file_path}. {e}")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
sales_data = load_csv(url)

# Check if the dataframe was loaded successfully
if sales_data is not None:
    print("\nThe first 5 rows of the dataframe:")
    print(sales_data.head())

    #print("\nDataframe info:")
    #print(sales_data.info())
else:
    print("Failed to load sales data. Please see above error messages for details.")
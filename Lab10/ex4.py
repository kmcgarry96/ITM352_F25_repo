# read as a json file
# calcule median fares

import pandas as pd
import json
import os

# Change to the correct directory
os.chdir('/Users/kylemcgarry/Desktop/ITM352_F25_repo/Lab10')

taxi_df = pd.read_json('taxi_trips.json')

print(taxi_df.describe())
print(taxi_df.head())
print("median fare:", taxi_df['fare'].median())

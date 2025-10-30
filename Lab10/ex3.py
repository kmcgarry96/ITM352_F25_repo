
import pandas as pd
# Create a DataFrame from a dictionary of lists


data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

# convert the dictionary to a dataframe
df = pd.DataFrame(data)
print(df)  


# read  in a CSV file of employee data and calculate the average salary 
# max salary and min salary
import csv
import os 


csv_filename = "my_custom_spreadsheet.csv" 

def analyze_salaries(csv_filename):
    salaries = []

    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Skip empty rows until we find the header
        header = []
        while not header or all(cell == '' for cell in header):
            header = next(reader)
        
        print(f"Header: {header}")

        salary_index = header.index("Annual_Salary")  # find the index of the salary column
        
        for row in reader:
            if row and len(row) > salary_index:  # Make sure row isn't empty and has enough columns
                salary = int(row[salary_index])
                salaries.append(salary)

    if salaries:
        average_salary = sum(salaries) / len(salaries)
        max_salary = max(salaries)
        min_salary = min(salaries)

        print(f"Average Salary: ${average_salary:.2f}")
        print(f"Max Salary: ${max_salary}")
        print(f"Min Salary: ${min_salary}")

analyze_salaries(csv_filename)

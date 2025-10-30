#  take a List of tuples that are percentiles and household incomes
import numpy as np
hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]


hh_income_array = np.array(hh_income)

# Print the data to verify
print("Household Income by Percentile:")
print("Percentile\tIncome")
print("-" * 20)
for percentile, income in hh_income:
    print(f"{percentile}\t\t${income:,}")

# Example: Access specific data
print(f"\nMedian income (50th percentile): ${hh_income[4][1]:,}")
print(f"Top 10% threshold (90th percentile): ${hh_income[8][1]:,}")

#report the number of the dimensions on the arry , and the number of elements
print('dimensions:', hh_income_array.ndim)
print('shape:', hh_income_array.shape)
print('number of elements:', hh_income_array.size)

for i in range(len(hh_income_array)):
    print(hh_income_array[i,0], hh_income_array[i,1])

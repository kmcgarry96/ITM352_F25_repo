# read 1000 lines of taxi data from the taxi_1000.csv file
# calculate the total of all fares, average fare, and the maximum trip distance
import csv

with open('taxi_1000.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    total_fare = 0
    max_distance = 0
    average_fare = 0
    num_rows = 0

    for line in csv_reader:
        if (num_rows == 0):  # skip header row
            num_rows += 1
            continue

        trip_fare = float(line[10])
        distance = float(line[5])
        total_fare += trip_fare
        if distance > max_distance:
            max_distance = distance
        num_rows += 1

        print(f'we read {num_rows} rows')
        print(f' TotalFare: ${total_fare:.2f}')
        if num_rows > 0:
            average_fare = total_fare / num_rows
        print(f' AverageFare: ${average_fare:.2f}')
        print(f' MaxDistance: {max_distance:.2f}')
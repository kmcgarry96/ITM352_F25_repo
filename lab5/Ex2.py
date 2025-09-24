# define a list of taxi trip durations and miles (with values 1.1, 0.8, 2.5, 2.6)

# define a tuple of fares for the same trips (with values $6.25,” “$5.25,” “$10.50,” “$8.05")

# store the touple and list as values in a dictionary with keys
#m "miles" and "fares"

# name: kyle McGarry
# date : 9/19/2025

tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = (6.25, 5.25, 10.50, 8.05)

trips = {"miles": tripDurations, "fares": tripFares}
print(trips)

print(f'the duration of the third trip is {trips["miles"][2]} miles')

print(f'the fare of the third trip is ${trips["fares"][2]}')

trips["miles"].append(2.2)
trips["fares"] += (4.0,)

print(trips)

trip_num = int(input("what trip do you want?:"))

print(f'the duration of trip {trip_num} is {trips["miles"][trip_num]} miles')
print(f'the fare of trip {trip_num} is ${trips["fares"][trip_num]}')

# zip together a list of trip durations and a tupple of trip fairs
# from thtis zip create a dictionary.

# name: kyle McGarry
# date : 9/24/25

tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = (6.25, 5.25, 10.50, 8.05)

trips = dict(zip(tripDurations, tripFares))
print(trips)

trip_num = int(input("what trip do you want?:"))

print(f'duration: {list(trips.keys())[trip_num - 1]} miles')
print(f' duration : {list(trips.keys())[trip_num - 1]} miles')
print(f'fare: ${list(trips.values())[trip_num - 1]:.2f}')

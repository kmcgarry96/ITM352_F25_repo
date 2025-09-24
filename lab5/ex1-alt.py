# create a list of dictionaries where each ictionary represnets
# a taxi trip
# name: kyle McGarry
# date : 9/19/2025

taxiTrips = [
    {"duration": 1.1, "fare": 6.25},
    {"duration": 2.3, "fare": 12.50},
    {"duration": 0.5, "fare": 3.75}
]


print(taxiTrips)

print(f'the third trip was {taxiTrips[2]["duration"]} miles and cost ${taxiTrips[2]["fare"]}.')

driver_share = taxiTrips[2]["fare"] * 0.8
print(f'the driver made ${driver_share: .2f} on the third trip.')



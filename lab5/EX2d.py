# create a string of dictionaries from the given dictionary
#name: kyle McGarry
#date: 9/24/25

trips = [{'miles': 1.1, 'duration': 6.25}, 
          {'miles': 0.8, 'duration': 5.25}, 
          {'miles': 2.5, 'duration': 10.5}, 
          {'miles': 2.6, 'duration': 8.05}
         ]



print(f'the first trip was {str(trips[0]["miles"])} miles and cost ${str(trips[0]["duration"])}.')
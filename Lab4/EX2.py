# define a list of survey responses values ( 5,7,3,8) and store it in a variable
# in a variable. define a tuple of response ID's (102,1035, 1021, 1053)
# and add these to the list
#name: kyle McGarry 
# date: 9/15/2025

#response_values = [5, 7, 3, 8]
#response_values.sort
#response_ids = (102, 1035, 1021, 1053)
#response_values.append(response_ids)

response_values = [(102, 5), (1035, 7), (1021, 3), (1053, 8)]
response_values.sort()


print("combined response values and ID's:", response_values)

# 3.3. Define a list and a tuple, append the tuple to the list, and print the list
response_values = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)
response_values.append(respondent_ids)
print("List after appending tuple:", response_values)

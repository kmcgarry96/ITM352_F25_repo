# create a data frame from individual lisst
# do some simple stastics on teh data.
import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

#create a dictionary frpm the lists 
dict = zip(ages, gender)

# convert the dictionary to a dataframe with names as the keys.
df = pd.DataFrame(dict, index = names, columns = ["age", "gender"])
print (df)


summary = df.describe()
print(summary)
 
 # calculate the average age by gender
average_age_by_gender = df.groupby("gender")["age"].mean()
print("\nAverage age by gender:")
print(average_age_by_gender)

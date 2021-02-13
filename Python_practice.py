print("Hello World")

#practicing if then staements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Membership operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#Compound and logical Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#Compound and logical Operators 2
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#compund and logical Operators 3
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

#loop practice

for county in counties:
    print(county)

#loop using range
for i in range(len(counties)):
    print(counties[i])

#looping in dictionaries
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
#Loopin in Dictionaries to find values
for voters in counties_dict.values():
    print(voters)
#looping in Dictionaries to find values using dictionary_name[key]
for county in counties_dict:
    print(counties_dict[county])
#looping in Dictionaries to find values using get function
for county in counties_dict:
    print(counties_dict.get(county))
#looping for keys and values
for county, voters in counties_dict.items():
    print(county, voters)
#looping for keys and values 2
for county, voters in counties_dict.items():
    print(county + " county has ", str(voters) + ' registired voters ')
#Get Each Dictionary in a list of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
#Nested for loops to get values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#multiple f strings
candidate_votes = 3345
total_votes = 23123
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

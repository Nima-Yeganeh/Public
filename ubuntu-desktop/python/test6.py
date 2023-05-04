import csv

# Open the CSV file and read the data into a list of dictionaries
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Calculate the average age of the people in the data
total_age = 0
num_people = len(data)
for person in data:
    total_age += int(person['age'])
average_age = total_age / num_people

# Print the results to the console
print("There are", num_people, "people in the data.")
print("The average age is:", average_age)

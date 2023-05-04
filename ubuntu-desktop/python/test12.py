import pandas as pd

# Read the data from a CSV file into a pandas dataframe
data = pd.read_csv('data.csv')

# Print the first few rows of the dataframe
print("First few rows of the data:")
print(data.head())

# Compute the mean and standard deviation of the 'age' column
mean_age = data['age'].mean()
std_age = data['age'].std()

# Print the results
print("Mean age:", mean_age)
print("Standard deviation of age:", std_age)

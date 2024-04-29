import pandas as pd

# Load the dataset into a pandas DataFrame
schools = pd.read_csv('schools.csv')

# Calculate total SAT score for each school
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# Which NYC schools have the best math results?
best_math_schools = schools[schools['average_math'] >= 0.8 * 800]  # Select schools with at least 80% of max math score
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)

# What are the top 10 performing schools based on the combined SAT scores?
top_10_schools = schools[['school_name', 'total_SAT']].nlargest(10, 'total_SAT')

# Which single borough has the largest standard deviation in the combined SAT score?
largest_std_dev = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).nlargest(1, 'std')
largest_std_dev = largest_std_dev.rename(columns={'count': 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'}).round(2)

# Display the results
print("NYC schools with the best math results:")
print(best_math_schools)
print("\nTop 10 performing schools based on combined SAT scores:")
print(top_10_schools)
print("\nBorough with the largest standard deviation in combined SAT score:")
print(largest_std_dev)


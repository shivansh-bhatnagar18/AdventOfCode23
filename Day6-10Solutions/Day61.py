# Read input from the text file
file_path = '../Data/boat_race.txt'  # Replace 'input.txt' with the path to your file

# Initialize lists for time and distance
time_input = []
distance_input = []

# Read the file and extract time and distance values
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('Time:'):
            time_input = [int(num) for num in line.split()[1:]]  # Extract time numbers
        elif line.startswith('Distance:'):
            distance_input = [int(num) for num in line.split()[1:]]  # Extract distance numbers

# Creating a list of lists
data_list = [time_input, distance_input]

print(data_list)    
mul = 1

for time in range(len(data_list[0])):
    count = 0
    for i in range(data_list[0][time] + 1):
        if (i * (data_list[0][time]-i)) > data_list[1][time]:
            count += 1
    mul *= count     

print(mul)



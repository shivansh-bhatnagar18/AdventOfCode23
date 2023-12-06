file_path = '../Data/boat_race.txt'  # Replace 'input.txt' with the path to your file

# Initialize lists for time and distance
time_input = []
distance_input = []

# Read the file and extract time and distance values
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('Time:'):
            time_input = [num for num in line.split()[1:]]  # Extract time numbers
        elif line.startswith('Distance:'):
            distance_input = [num for num in line.split()[1:]]  # Extract distance numbers

    time_input = ''.join(time_input)
    distance_input = ''.join(distance_input)
# Creating a list of lists
data_list = [int(time_input), int(distance_input)]

print(data_list) 
count = 0
for i in range(data_list[0] + 1):
    if (i * (data_list[0]-i)) > data_list[1]:
        count += 1

print(count)


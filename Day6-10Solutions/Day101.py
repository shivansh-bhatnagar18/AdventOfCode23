def read_input_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Remove newline characters and split each line into a list of characters
            grid = [list(line.strip()) for line in lines]
            return grid
    except FileNotFoundError:
        print("File not found.")

# Replace 'input.txt' with the path to your input file
file_name = '../Data/landloop.txt'
result = read_input_file(file_name)

for r in range(len(result)): 
    result[r] = ['.'] + result[r] + ['.']
result.insert(0, ['.'] * len(result[0]))
result.append(['.'] * len(result[0]))   

for r in range(len(result)):  
    if 'S' in result[r]:
        starting_index = [r, result[r].index('S'), 0, 'S']
        break
print(starting_index)
left = [starting_index[0], starting_index[1] + 1, starting_index[2] + 1, 'J']
right = [starting_index[0] + 1, starting_index[1], starting_index[2] + 1, '|']
left_next = [starting_index[0] - 1, starting_index[1] + 1, starting_index[2] + 2, 'F']
right_next = [starting_index[0] + 2, starting_index[1], starting_index[2] + 2, 'L']
numbers = []
numbers.append((left, right))
numbers.append((left_next, right_next))
print(numbers)

while True:
    if left_next[3] == 'L':
        if left_next[0] == left[0] + 1:
            left = left_next
            left_next = [left_next[0], left_next[1] + 1, left_next[2] + 1, result[left_next[0]][left_next[1] + 1]]
        elif left_next[1] == left[1] - 1:
            left = left_next
            left_next = [left_next[0] - 1, left_next[1], left_next[2] + 1, result[left_next[0] - 1][left_next[1]]]
    elif left_next[3] == 'F':
        if left_next[0] == left[0] - 1:
            left = left_next
            left_next = [left_next[0], left_next[1] + 1, left_next[2] + 1, result[left_next[0]][left_next[1] + 1]]
        elif left_next[1] == left[1] - 1:
            left = left_next
            left_next = [left_next[0] + 1, left_next[1], left_next[2] + 1, result[left_next[0] + 1][left_next[1]]]   
    elif left_next[3] == '|':
        if left_next[0] == left[0] + 1:
            left = left_next
            left_next = [left_next[0] + 1, left_next[1], left_next[2] + 1, result[left_next[0] + 1][left_next[1]]]
        elif left_next[0] == left[0] - 1:
            left = left_next
            left_next = [left_next[0] - 1, left_next[1], left_next[2] + 1, result[left_next[0] - 1][left_next[1]]]     
    elif left_next[3] == 'J':
        if left_next[1] == left[1] + 1:
            left = left_next
            left_next = [left_next[0] - 1, left_next[1], left_next[2] + 1, result[left_next[0] - 1][left_next[1]]]
        elif left_next[0] == left[0] + 1:
            left = left_next
            left_next = [left_next[0], left_next[1] - 1, left_next[2] + 1, result[left_next[0]][left_next[1] - 1]]  
    elif left_next[3] == '-':
        if left_next[1] == left[1] + 1:
            left = left_next
            left_next = [left_next[0], left_next[1] + 1, left_next[2] + 1, result[left_next[0]][left_next[1] + 1]]
        elif left_next[1] == left[1] - 1:
            left = left_next
            left_next = [left_next[0], left_next[1] - 1, left_next[2] + 1, result[left_next[0]][left_next[1] - 1]]      
    elif left_next[3] == '7': 
        if left_next[0] == left[0] - 1:
            left = left_next
            left_next = [left_next[0], left_next[1] - 1, left_next[2] + 1, result[left_next[0]][left_next[1] - 1]]
        elif left_next[1] == left[1] + 1:
            left = left_next
            left_next = [left_next[0] + 1, left_next[1], left_next[2] + 1, result[left_next[0] + 1][left_next[1]]]     


    if right_next[3] == 'L':
        if right_next[0] == right[0] + 1:
            right = right_next
            right_next = [right_next[0], right_next[1] + 1, right_next[2] + 1, result[right_next[0]][right_next[1] + 1]]
        elif right_next[1] == right[1] - 1:
            right = right_next
            right_next = [right_next[0] - 1, right_next[1], right_next[2] + 1, result[right_next[0] - 1][right_next[1]]]
    elif right_next[3] == 'F':
        if right_next[0] == right[0] - 1:
            right = right_next
            right_next = [right_next[0], right_next[1] + 1, right_next[2] + 1, result[right_next[0]][right_next[1] + 1]]
        elif right_next[1] == right[1] - 1:
            right = right_next
            right_next = [right_next[0] + 1, right_next[1], right_next[2] + 1, result[right_next[0] + 1][right_next[1]]]   
    elif right_next[3] == '|':
        if right_next[0] == right[0] + 1:
            right = right_next
            right_next = [right_next[0] + 1, right_next[1], right_next[2] + 1, result[right_next[0]][right_next[1]]]
        elif right_next[0] == right[0] - 1:
            right = right_next
            right_next = [right_next[0] - 1, right_next[1], right_next[2] + 1, result[right_next[0] - 1][right_next[1]]]     
    elif right_next[3] == 'J':
        if right_next[1] == right[1] + 1:
            right = right_next
            right_next = [right_next[0] - 1, right_next[1], right_next[2] + 1, result[right_next[0] - 1][right_next[1]]]
        elif right_next[0] == right[0] + 1:
            right = right_next
            right_next = [right_next[0], right_next[1] - 1, right_next[2] + 1, result[right_next[0]][right_next[1] - 1]]  
    elif right_next[3] == '-':
        if right_next[1] == right[1] + 1:
            right = right_next
            right_next = [right_next[0], right_next[1] + 1, right_next[2] + 1, result[right_next[0]][right_next[1] + 1]]
        elif right_next[1] == right[1] - 1:
            right = right_next
            right_next = [right_next[0], right_next[1] - 1, right_next[2] + 1, result[right_next[0]][right_next[1] - 1]]      
    elif right_next[3] == '7': 
        if right_next[0] == right[0] - 1:
            right = right_next
            right_next = [right_next[0], right_next[1] - 1, right_next[2] + 1, result[right_next[0]][right_next[1] - 1]]
        elif right_next[1] == right[1] + 1:
            right = right_next
            right_next = [right_next[0] + 1, right_next[1], right_next[2] + 1, result[right_next[0] + 1][right_next[1]]]       

    numbers.append((left_next, right_next))
    if left_next == right_next:
        break  

    print(numbers)                                                   

with open('../Data/map.txt', 'r') as file:
    lines = file.readlines()

data_dict = {}
for line in lines[2:]:
    line = line.strip().split(' = ')
    key = line[0]
    value = line[1][1:-1].split(', ')
    data_dict[key] = value

instructions = []
for ins in lines[0].strip():
    instructions.append(ins)

count = 0
current_pointer = 'AAA'
final_pointer = 'ZZZ'
i = 0 
print(len(instructions))
while True:
    if current_pointer == final_pointer:
        break
    if instructions[i%len(instructions)] == 'L':
            current_pointer = data_dict[current_pointer][0]
            count += 1
    elif instructions[i%len(instructions)] == 'R':
            current_pointer = data_dict[current_pointer][1]
            count += 1        
    i += 1
print(count)


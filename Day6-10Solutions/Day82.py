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

ends_with_a = []
for key in data_dict:
    if key.endswith('A'):
        ends_with_a.append(key)
ends_with_z = []
for key in data_dict:
    if key.endswith('Z'):
        ends_with_z.append(key)   

print(ends_with_z)        


count = 0
i = 0
while True:  
    for element in range(len(ends_with_a)):
        if instructions[i%len(instructions)] == 'L':
            ends_with_a[element] = data_dict[ends_with_a[element]][0]
        elif instructions[i%len(instructions)] == 'R':
            ends_with_a[element] = data_dict[ends_with_a[element]][1]
    i += 1
    count += 1      
    if set(ends_with_a).issubset(set(ends_with_z)):
         break      

print(count)

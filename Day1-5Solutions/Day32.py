def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def numbers_in_neighbourhood(array_2d, row, col):
    numbers = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if (array_2d[i][j].isdigit()):
                number = array_2d[i][j-2:j+3]
                number_clr = ""
                start_index = None
                for m in range(len(number)):
                    if number[m].isdigit():
                        if start_index == None:
                            start_index = m
                    else:
                        if start_index is not None:
                            number_clr = "".join(number[start_index:m])
                            if int(number_clr) >= 10:
                                numbers.append(int(number_clr))
                            start_index = None

                if start_index is not None:
                    number_clr = "".join(number[start_index:])
                    if int(number_clr) >= 10:
                        numbers.append(int(number_clr))
                
       
    return set(numbers)

file_path = '../Data/engine.txt'
array_2d = read_file(file_path)

# Add '.' as padding to the incoming 2D array
padded_array_2d = [['.' for _ in range(len(array_2d[0]) + 6)],['.' for _ in range(len(array_2d[0]) + 6)],['.' for _ in range(len(array_2d[0]) + 6)]]
for array in array_2d:
    padded_array_2d.append(['.'] + ['.'] + ['.'] + array + ['.'] + ['.'] + ['.'])
padded_array_2d.append(['.' for _ in range(len(array_2d[0]) + 6)])
padded_array_2d.append(['.' for _ in range(len(array_2d[0]) + 6)])
padded_array_2d.append(['.' for _ in range(len(array_2d[0]) + 6)])
array_2d = padded_array_2d

sum = 0
for array in range(3, len(array_2d) - 3):
    element = 3
    while element < len(array_2d[array]) - 3:
        if array_2d[array][element] == "*":
            numbers = numbers_in_neighbourhood(array_2d, array, element)
            if len(numbers) == 2:
                print(numbers)
                mult =1
                for num in numbers:
                    mult *= num
                sum += mult  
        element += 1          
print(sum)

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def symbol_in_neighbourhood(array_2d, row, col):
    symbols = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if (array_2d[i][j]!="." and not (array_2d[i][j].isdigit())):
                symbols += 1
    return symbols

file_path = '../Data/engine.txt'
array_2d = read_file(file_path)

# Add '.' as padding to the incoming 2D array
padded_array_2d = [['.' for _ in range(len(array_2d[0]) + 2)]]
for array in array_2d:
    padded_array_2d.append(['.'] + array + ['.'])
padded_array_2d.append(['.' for _ in range(len(array_2d[0]) + 2)])
array_2d = padded_array_2d

c = 0
sum = 0
for array in range(1, len(array_2d) - 1):
    element = 1
    while element < len(array_2d[array]) - 1:
        c = 0
        number = ""
        sym = 0
        if array_2d[array][element].isdigit():
            while array_2d[array][element + c].isdigit():
                if symbol_in_neighbourhood(array_2d, array, element + c) > 0:
                    sym += symbol_in_neighbourhood(array_2d, array, element + c)
                number += str(array_2d[array][element + c])
                c += 1
            if sym > 0: 
                print(number)   
                sum += int(number)
            element += c
        else:
            element += 1             
            
print(sum)            
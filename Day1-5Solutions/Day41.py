
file_path = "../Data/scratch.txt"
data = []
import math
with open(file_path, "r") as file:
    for line in file:
        data.append(line.strip().split(" | "))
    dataset = []    
    for element in data:
        dataset.append([element[0][element[0].index(":")+2:].split(" ") , element[1].split(" ")])
    for element in dataset:
        for num in element[0]:
            if not num.isdigit():
                element[0].remove(num)
        for num in element[1]:
            if not num.isdigit():
                element[1].remove(num)

    print(dataset)                    

    sum = 0 
    for element in dataset:
        counter = 0
        for num in element[1]:
            if num in element[0]:
                counter += 1
        if counter > 0:        
            sum += math.pow(2, counter - 1) 
        else :
            sum += 0        
    print(int(sum))

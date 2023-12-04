import math
file_path = "../Data/scratch.txt"
data = []

with open(file_path, "r") as file:
    for line in file:
        data.append(line.strip().split(" | "))
    dataset = []    
    for element in data:
        dataset.append([1 , element[0][element[0].index(":")+2:].split(" ") , element[1].split(" ")])
    for element in dataset:
        for num in element[1]:
            if not num.isdigit():
                element[1].remove(num)
        for num in element[2]:
            if not num.isdigit():
                element[2].remove(num)

    for element in range(len(dataset)):
        counter = 0
        for num in dataset[element][2]:
            if num in dataset[element][1]:
                counter += 1
        for i in range(1, counter + 1):
            dataset[element + i][0] += 1*dataset[element][0]

    sum = 0
    for element in dataset:
        sum += element[0]         

    print(sum)        
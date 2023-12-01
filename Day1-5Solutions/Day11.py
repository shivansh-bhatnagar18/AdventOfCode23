
file_path = "../Data/file.txt"  # Replace with the actual file path
sum = 0 
lines = []
with open(file_path, "r") as file:
    start_number = None
    end_number = None
    for line in file:
        lines.append(line.strip())


    for line in lines:    
        for character1 in line:
            if character1.isdigit():
                start_number = int(character1)
                sum +=  (start_number * 10)               
                break

        for character2 in line[::-1]:
            if character2.isdigit():
                end_number = int(character2)
                sum += end_number
                break
            
print(sum)    




dic_straight = {'one': "one1one", 'two': "two2two", 'three': "three3three", 'four': "four4four", 'five': "five5five", 'six': "six6six", 'seven': "seven7seven", 'eight': "eight8eight", 'nine': "nine9nine"}
file_path = "file.txt"  # Replace with the actual file path
sum = 0 
lines = []
with open(file_path, "r") as file:
    start_number = None
    end_number = None
    for line in file:
        lines.append(line.strip())

    for i in range(len(lines)):
        for word in dic_straight.keys():
            if word in lines[i]:
                lines[i] = lines[i].replace(word, str(dic_straight[word]))        
        
    print(lines)

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
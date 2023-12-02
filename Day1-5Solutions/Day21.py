cleaned_dataset = {}
file_path = "../Data/games.txt"

with open(file_path, "r") as file:
    data = file.read().splitlines()

    for line in range(len(data)):  
        trial = data[line].split("; ") 
        cleaned_dataset[line + 1] = {}
        for item in range(len(trial)):
            value = trial[item].split(", ")
            cleaned_dataset[line + 1][item + 1] = [0, 0, 0]
            for element in value:
                if ':' in element:
                    element = element[element.index(':') + 1::1]
                if 'blue' in element:
                    cleaned_dataset[line + 1][item + 1][2] += int(element[0:element.index('b')])
                if 'red' in element:
                    cleaned_dataset[line + 1][item + 1][0] += int(element[0:element.index('r')])
                if 'green' in element:
                    cleaned_dataset[line + 1][item + 1][1] += int(element[0:element.index('g')])

    sum_of_games = 0
    for i in cleaned_dataset.keys():
        for j in cleaned_dataset[i].values():
            if j[0] > 12 or j[1] > 13 or j[2] > 14:
                sum_of_games += i
                print(i)
                break

    print(5050 - sum_of_games)


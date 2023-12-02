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

    sum_of_power = 0
    for game in cleaned_dataset.keys():
        rmax = 0
        gmax = 0
        bmax = 0
        for trial in cleaned_dataset[game].values():
            if trial[0] > rmax:
                rmax = trial[0]
            if trial[1] > gmax:
                gmax = trial[1]
            if trial[2] > bmax:
                bmax = trial[2]      
        power = rmax * gmax * bmax
        sum_of_power += power 

print(sum_of_power)       


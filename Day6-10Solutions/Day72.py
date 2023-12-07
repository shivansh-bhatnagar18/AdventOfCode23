# Read data from the file
file_name = '../Data/camel.txt'

with open(file_name, 'r') as file:
    data = file.read()

dataset = [line.split() for line in data.split('\n')]
ordering = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def is_high_card(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for High Card (No specific poker hand)
    if len(counts) == 5:
        return True,
    return False

def is_five_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for Five of a Kind
    if 5 in counts.values() and len(counts) == 1:
        return True
    return False

def is_one_pair(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for One Pair
    if 2 in counts.values() and len(counts) == 4:
        return True, max(counts.keys(), key=(lambda k: counts[k]))
    return False, max(counts.keys(), key=(lambda k: counts[k]))        

def is_three_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for Three of a Kind
    if 3 in counts.values() and len(counts) == 3:
        return True, max(counts.keys(), key=(lambda k: counts[k]))
    return False, max(counts.keys(), key=(lambda k: counts[k]))

def is_four_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for Four of a Kind
    if 4 in counts.values() and len(counts) == 2:
        return True, max(counts.keys(), key=(lambda k: counts[k]))
    return False, max(counts.keys(), key=(lambda k: counts[k]))

def is_full_house(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Check for Full House
    if sorted(counts.values()) == [2, 3] and len(counts) == 2:
        return True, max(counts.keys(), key=(lambda k: counts[k]))
    return False, max(counts.keys(), key=(lambda k: counts[k]))

def is_two_pair(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Check for Two Pair
    if sorted(counts.values()) == [1, 2, 2]:
        return True, sorted(counts.keys(), key=(lambda k: counts[k]))[1], sorted(counts.keys(), key=(lambda k: counts[k]))[2]
    return False, None


def settle_dataset(data):
    for element in data:
        if is_high_card(element[0]):
            str = element[0].replace('J', 'A')
        elif is_five_of_a_kind(element[0]):
            str = element[0].replace('J', 'A')
        elif is_one_pair(element[0])[0]:
            if is_one_pair(element[0])[1] == 'J':
                str = element[0].replace('J', 'A')
            else:    
                str = element[0].replace('J', is_one_pair(element[0])[1])
        elif is_three_of_a_kind(element[0])[0]:
            if is_three_of_a_kind(element[0])[1] == 'J':
                str = element[0].replace('J', 'A')
            else:    
                str = element[0].replace('J', is_three_of_a_kind(element[0])[1])   
        elif is_four_of_a_kind(element[0])[0]:
            if is_four_of_a_kind(element[0])[1] == 'J':
                str = element[0].replace('J', 'A')
            else:    
                str = element[0].replace('J', is_four_of_a_kind(element[0])[1])
        elif is_full_house(element[0])[0]:
            if is_full_house(element[0])[1] == 'J':
                str = element[0].replace('J', 'A')
            else:    
                str = element[0].replace('J', is_full_house(element[0])[1])
        elif is_two_pair(element[0])[0]:
            print(is_two_pair(element[0]))
            if is_two_pair(element[0])[1] == 'J':
                str = element[0].replace('J', is_two_pair(element[0])[2])
            elif is_two_pair(element[0])[2] == 'J':
                str = element[0].replace('J', is_two_pair(element[0])[1])    
            else:
                replacey = is_two_pair(element[0])[1] if ordering.index(is_two_pair(element[0])[1]) > ordering.index(is_two_pair(element[0])[2]) else is_two_pair(element[0])[2]
                str = element[0].replace('J', replacey)
        element.append(str)

settle_dataset(dataset)                                           

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Flag to check if any swapping occurs in this pass
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if len(set(arr[j][2])) <= len(set(arr[j + 1][2])):
                if len(set(arr[j][2])) < len(set(arr[j + 1][2])):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                if len(set(arr[j][2])) == len(set(arr[j + 1][2])):
                    if is_four_of_a_kind(arr[j][2])[0] and is_full_house(arr[j + 1][2])[0]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    elif is_three_of_a_kind(arr[j][2])[0] and is_two_pair(arr[j + 1][2])[0]:  
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    elif is_two_pair(arr[j][2])[0] and is_three_of_a_kind(arr[j + 1][2])[0]:  
                        arr[j], arr[j + 1] = arr[j], arr[j + 1]
                    elif is_full_house(arr[j][2])[0] and is_four_of_a_kind(arr[j + 1][2])[0]:
                        arr[j], arr[j + 1] = arr[j], arr[j + 1]    
                    else:
                        for k in range(5):
                            if ordering.index(arr[j][0][k]) < ordering.index(arr[j + 1][0][k]):
                                break
                            elif ordering.index(arr[j][0][k]) > ordering.index(arr[j + 1][0][k]):
                                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                                swapped = True
                                break                          
        if not swapped:
            break
print(dataset)
print()
print()
bubble_sort(dataset)
print(dataset)
sum = 0
for i in range(len(dataset)):
    sum += int(dataset[i][1]) * (i + 1)      

print(sum)

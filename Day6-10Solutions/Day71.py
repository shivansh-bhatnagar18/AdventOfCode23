# Read data from the file
file_name = '../Data/camel.txt'

with open(file_name, 'r') as file:
    data = file.read()

dataset = [line.split() for line in data.split('\n')]
ordering = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def is_three_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for Three of a Kind
    if 3 in counts.values() and len(counts) == 3:
        return True
    return False

def is_four_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    
    # Check for Four of a Kind
    if 4 in counts.values() and len(counts) == 2:
        return True
    return False

def is_full_house(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Check for Full House
    if sorted(counts.values()) == [2, 3] and len(counts) == 2:
        return True
    return False

def is_two_pair(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Check for Two Pair
    if sorted(counts.values()) == [1, 2, 2]:
        return True
    return False

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Flag to check if any swapping occurs in this pass
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if len(set(arr[j][0])) <= len(set(arr[j + 1][0])):
                if len(set(arr[j][0])) < len(set(arr[j + 1][0])):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                if len(set(arr[j][0])) == len(set(arr[j + 1][0])):
                    if is_four_of_a_kind(arr[j][0]) and is_full_house(arr[j + 1][0]):
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    elif is_three_of_a_kind(arr[j][0]) and is_two_pair(arr[j + 1][0]):  
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    elif is_two_pair(arr[j][0]) and is_three_of_a_kind(arr[j + 1][0]):  
                        arr[j], arr[j + 1] = arr[j], arr[j + 1]
                    elif is_full_house(arr[j][0]) and is_four_of_a_kind(arr[j + 1][0]):
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

bubble_sort(dataset)
print(dataset)
sum = 0
for i in range(len(dataset)):
    sum += int(dataset[i][1]) * (i + 1)      

print(sum)

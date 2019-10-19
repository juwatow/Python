def binary_search(orderedList, searchItem):
    # lowIndex and highIndex: keep track of which part of the ordered list to search
    lowIndex = 0
    highIndex = len(orderedList) - 1

    while lowIndex <= highIndex: # while we haven't narrowed to 1 element
        midIndex = int((lowIndex + highIndex) / 2)
        guess = orderedList[midIndex]
        
        if guess == searchItem: # search item has been found
            return midIndex
        if guess > searchItem: # guess was too high => focus the search in the lower part of the list
            highIndex = midIndex - 1
        else: # guess was too small => focus the search in the upper part of the list
            lowIndex = midIndex + 1
    return None # search item is not in the list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(binary_search(my_list, 10)) #case: search term in the list
print(binary_search(my_list, 20)) #case: search term not in the list
def binary_search(sorted_list, search_item):
    # low_index and high_index: keep track of which part of the ordered list to search
    low_index = 0
    high_index = len(sorted_list) - 1

    while low_index <= high_index: # while we haven't narrowed to 1 element
        mid_index = int((low_index + high_index) / 2)
        guess = sorted_list[mid_index]
        
        if guess == search_item: # search item has been found
            return mid_index
        if guess > search_item: # guess was too high => focus the search in the lower part of the list
            high_index = mid_index - 1
        else: # guess was too small => focus the search in the upper part of the list
            low_index = mid_index + 1
    return None # search item is not in the list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(binary_search(my_list, 9)) #case: search term in the list
print(binary_search(my_list, 20)) #case: search term not in the list
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    while len(arr) > 0:
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

print(selection_sort([5, 3, 6, 9, 5]))
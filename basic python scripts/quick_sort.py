def quick_sort(data):
    length = len(data)
    if length <= 1:
        return data
    else:
        pivot = data.pop()

    items_greater_right = []
    items_lower_left = []

    for item in data:
        if item < pivot:
            items_lower_left.append(item)  # if data item is less than pivot we place it ot to the left side of the pivot
        else:
            items_greater_right.append(item)  # if data item is greater than pivot we place it ot to the right side of the pivot     

    return quick_sort(items_lower_left) + [pivot] + quick_sort(items_greater_right)

print(quick_sort([1,4,77,3,92,6,0,23,5,3,6,8,44,21,6])) # you can take data from user also just use input function and modify thic code in your way.
""" Find the missing number from a given List.
    Explanation:
        INPUT: [1,2,3,4,5,7,9,10]
        Output: [6,8]
"""
def get_missing_number(num_list):
    sorted_num = sorted(num_list)
    original_list = {num for num in range(sorted_num[0], sorted_num[-1] + 1)}
    num_set = set(sorted_num)
    return list(original_list - num_set)

INPUT = [20,23,27,32,35,40,22,21]
print(sorted(get_missing_number(INPUT)))

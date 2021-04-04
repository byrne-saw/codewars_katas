# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    odds = []  

    if sort_array == []:
        return []
    
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            continue
        else:
            odds.append(source_array[i])
            source_array[i] = 'x'

    odds.sort()
    odd_i = 0

    for i in range(len(source_array)):
        if source_array[i] == 'x':
            source_array[i] = odds[odd_i]
            odd_i += 1

    return source_array



print(sort_array([5, 3, 2, 8, 1, 4]))  # =>  [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))  # =>  [1, 3, 5, 8, 0]
print(sort_array([]))  # => []

# awesome solution: https://www.codewars.com/kata/reviews/5790d34d671cb50d6600016d/groups/595aee254ceb769bac000038
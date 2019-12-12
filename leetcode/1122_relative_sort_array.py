"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19],
        arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

"""

def relative_sort(arr1, arr2):
    sorted_arr = []
    not_included = []
    dict = {}

    for i in arr1:
        if i not in arr2:
            not_included.append(i)
        continue
    not_included.sort()

    # Create dictionary (with values already recorded)
    for i in arr1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    # now, fill in sorted_arr
    for i in arr2:
        for x in range(dict[i]):
            sorted_arr.append(i)

    return sorted_arr + not_included



arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relative_sort(arr1,arr2))

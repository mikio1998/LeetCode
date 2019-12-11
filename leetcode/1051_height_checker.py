"""
Students are asked to stand in non-decreasing order
of heights for an annual photo.

Return the minimum number of students not standing in
the right positions.
(This is the number of students that must move in order
for all students to be standing in non-decreasing order
of height.)

Input: [1,1,4,2,1,3]
Output: 3

Students with heights 4, 3 and the last 1
are not standing in the right positions.

"""

def checker(arr):
    normal = arr
    sort_array = sorted(arr)

    bad = 0

    for i in range(len(arr)):
        if normal[i] != sort_array[i]:
            bad += 1
        else:
            continue
    return bad


arr = [1,1,4,2,1,3]
print(checker(arr))
"""
Given an array of integers arr, write a function
that returns true if and only if the number of occurrences
of each value in the array is unique.

arr = [1,2,2,1,1,3]
true

"""



def unique(arr):
    hashes = {}

    for i in arr:
        if i in hashes:
            #add it
            hashes[i] += 1
        else:
            hashes[i] = 1

    values = []

    for i in hashes.values():
        values.append(i)
    values.sort()

    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            return False


    return True


arr = [1,2,2,1,1,3]
print(unique(arr))




























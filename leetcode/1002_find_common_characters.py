"""
Given an array A of strings made only from lowercase letters, return a list of all characters
that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

"""

"""
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""

def common_characters(arr):
    shortest_string = min(arr, key=len) # get shortest string for efficiency purposes
    array = arr.copy() # make copy of arr, and...
    array.remove(shortest_string)  # remove the shortest_string for iteration purposes later.
    dict = {}
    for i in shortest_string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    dict1 = dict.copy()

    for word in array: # for each word


        for key in dict1:
            if key not in word:
                del dict1[key]
            else: #if key exists
                # if the occurance of they key in the word, is enough...
                if word.count(key) >= dict1[key]:
                    





    return dict

arr = ["bella","label","roller"]
print(common_characters(arr))
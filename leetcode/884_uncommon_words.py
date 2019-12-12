"""

We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]


Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""

def uncommon(a, b):
    found_it = []

    x = a.split(" ")
    y = b.split(" ")

    z = x + y

    dictionary = {}
    for i in z:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    for i in dictionary:
        if dictionary[i] == 1:
            found_it.append(i)

    return found_it

A = "this apple is sweet"
B = "this apple is sour"

print(uncommon(A,B))
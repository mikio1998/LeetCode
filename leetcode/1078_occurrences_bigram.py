"""
Given words first and second, consider occurrences
in some text of the form "first second third",
where second comes immediately after first,
and third comes immediately after second.

Input:
text = "alice is a good girl she is a good student",
first = "a", second = "good"

Output: ["girl","student"]

"""

def first_second(text, first, second):
    good = []

    text = text
    splitted = text.split()
    for i in range(len(splitted)-2):
        if splitted[i] == first:
            if splitted[i+1] == second:
                good.append(splitted[i+2])
            else:
                continue
    return good



text = "alice is a good girl she is a good student"
first = "a"
second = "good"


print(first_second(text, first, second))
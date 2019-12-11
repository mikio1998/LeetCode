"""
Balanced strings are those who have equal quantity
of 'L' and 'R' characters.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into...
"RL", "RRLL", "RL", "RL",
each substring contains same number of 'L' and 'R'.

"""
"""
Genius solution (not by me)

balance = 0

for... iterate through s
"L" = +1
"R" = -1

when balance is 0, add one 
(balance=0 indicates symmetric string).

"""


def split_string(s):
    ok = 0
    balance = 0

    for i in s:
        if i == "L":
            balance += 1
        else: # if "R"
            balance -= 1

        if balance == 0: # if works here?
            ok += 1
    return ok

s = "RLRRLLRLRL"
print(split_string(s))
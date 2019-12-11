"""
Quizbucks!
"Quiznos", "Starbucks"... are they adjacent?
Given array is a strip mall. Does the stripmall have a Quizbucks?

["Jamba Juice", "Sally Beauty Supply", "State Farm", "Quiznos", "Starbucks"]	True
["Starbucks", "Rose Creek Family Chiropractic Center", "Quiznos", "GNC"]    False
["Little Caesars", "H&R Block", "Gamestop", "T-Mobile", "Big-5 Sporting Goods"]     False

"""

def containsQuizbucks(mall):
    star = "Starbucks"
    quiz = "Quiznos"


    if not star in mall or not quiz in mall: #check the existence
        return False

    curr_index = 0
    curr = mall[curr_index]

    while curr != mall[-1]:

        if curr == star:
            print(curr, curr_index)
            if mall[curr_index + 1] == quiz:
                return True

            else:
                print("not quiz")
                if curr == mall[-2]:
                    return False
                curr_index += 2

        elif curr == quiz:
            if mall[curr_index + 1] == star:
                return True
            else:
                if curr == mall[-2]:
                    return False
                curr_index += 2
        else:
            curr_index += 1

    return False





mall1 = ["Jamba Juice", "Sally Beauty Supply", "State Farm", "Quiznos", "Starbucks"] #tru

mall2 = ["Starbucks", "Rose Creek Family Chiropractic Center", "Quiznos", "GNC"] #false

mall3 = ["Little Caesars", "H&R Block", "Gamestop", "T-Mobile", "Big-5 Sporting Goods"] #false

print(containsQuizbucks(mall2))
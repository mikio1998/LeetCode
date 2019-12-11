"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""
"""
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6

Explanation: 
The strings that can be formed are "cat" and "hat" 
so the answer is 3 + 3 = 6.

***
Remember to count recurring letters!
***

"""

def find_words(arr, chars):
    # create duplicate
    good_words = arr.copy()

    dict = {}
    for i in chars:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    # Now check words in arr.
    for word in arr:
        print(word)
        temp_dict = dict.copy() #create temp_dict for letter counting purposes.

        for letter in word:
            # word is not applicable... if letter is missing, or if letters are used up.
            if letter not in dict or temp_dict[letter] == 0:
                good_words.remove(word) #remove it from good_words
                break       #continue to the next word.
            else:
                temp_dict[letter] -= 1

    # now, just add up the count.
    count = 0
    for i in good_words:
        count += len(i)

    return count

#arr = ["cat","bt","hat","tree"]
#chars = "atach"

arr = ["skwgxuuuumkfurejmqrbipvlavdrozjyxhagbwetabjwevfsegqfpllgafm","ufvpzzgpswnk","tcouxmlrnfyoxvkeglchhryykmdvgvdxpookbtiyhuthoqsnqbowewpfgbcy","qwpttmxzazkkfqqtrnkaejifligdvgnyvtmppjbkeuqryxzqyegttvhzolpztvigxygzvsppurijaekb","vbtvbheurzbglzljczmziitkbmtoybiwhoyfrsxvfveaxchebjdzdnnispzwbrgrbcdaistps"]
chars = "avyteswqppomeojxoybotzriuvxolmllevluauwb"

print(find_words(arr, chars))


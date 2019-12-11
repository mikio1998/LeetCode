"""
Valid words do not contain any special characters, or numbers. However, it can contain apostrope ', but no more than 1.
Valid words has to contain at least 1 character, but no word contains only consonants.
No word longer than 1 character can contain only vowels.
We love Northern Europe, so words can contain the letters å, ä, ö, æ, ø.
Valid words can be a mix of upper and lower case characters
"""

"""
No special characters. ' allowed (only one)
At least 1 character
Both vowels and consonants
If longer than 1 character, both vowel and consonants.
å, ä, ö, æ, ø ... ok
not case sensitive 
"""

vowelArr = ["A", "E", "I", "O", "U", "Å", "Ä", "Ö", "Æ", "Ø"]
consonantArr = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def valid(word):
    word = word.upper()
    word = str(word)
    if len(word) == 0:  # word is nil
        return False
    elif len(word) == 1:   # if len is 1, should be vowel.
        if word in consonantArr:
            return False
        return True

    else:

        wordArr = []
        for i in range(len(word)):
            #obj = str(word[i])
            #wordArr.append(obj)
            wordArr.append(word[i])

        vowel = False
        consonant = False

        for i in wordArr:
            if i in vowelArr:
                vowel = True
            elif i in consonantArr:
                consonant = True
            else:
                return False

        if vowel == True and consonant == True:
            return True
theWord = "Bö1"
print(valid(theWord))

"""
Input:

"flew"
"flu"
"In January, Time reported that the 2017-18 flew season was one of the worst seasons in the past 13 years. The dominant viral strain, H3N2, was a particularly severe form of influenza, leading to widespread and serious illness across the country,” according to the Time article. “The flew and its complications killed around 80,000 people last year, the CDC estimates, including 180 children. That’s the highest flew death toll in four decades.”

Output:

"In January, Time reported that the 2017-18 flu season was one of the worst seasons in the past 13 years.

“The dominant viral strain, H3N2, was a particularly severe form of influenza, leading to widespread and serious illness across the country,” according to the Time article. “The flu and its complications killed around 80,000 people last year, the CDC estimates, including 180 children. That’s the highest flu death toll in four decades.”

"""





def replaceMistake(wrong, right, text):
    if text.find(wrong):

        lenOfRight = len(wrong)

        wrongIndexes = [] #look in this array for index location of wrong word instances
        currentIndex = 0
        while currentIndex < len(text):
            currentIndex = text.find(wrong, currentIndex)

            if currentIndex == -1: #if find() doesn't find anything, it returns -1.
                break

            wrongIndexes.append(currentIndex)
            currentIndex += lenOfRight #update the current index, so the next iteration starts at the end of the previous word.



        wrongIndexes = wrongIndexes[::-1] #have to reverse, since dif length right/wrong could run into replacing issues. If replace from the end to start, won't run into indexing issues.
        newText = text

        for i in wrongIndexes:

            newText = newText[:i]+right+newText[i+lenOfRight:]

        return newText

    else:
        return "No mistakes"



wrong = "cat"
right = "dog"
text1 = "In January, Time reported that the 2017-18 flew season was one of the worst seasons in the past 13 years. The dominant viral strain, H3N2, was a particularly severe form of influenza, leading to widespread and serious illness across the country,” according to the Time article. “The flew and its complications killed around 80,000 people last year, the CDC estimates, including 180 children. That’s the highest flew death toll in four decades."
text2 = "Gadget is a laid back guy. He has lived with another cat, but will still need a gradual introduction to any resident cat. His history with dogs and small kids is unknown. Gadget tested positive for FIV which is a condition that can reduce his immunity to diseases. It is spread usually during cat fights. It’s not a disease that can be spread to other species and FIV cats often live long, happy lives. Do some research and consider adopting a friendly, FIV positive cat like Gadget."

print(replaceMistake(wrong, right, text2))
#print(wrong[-1])
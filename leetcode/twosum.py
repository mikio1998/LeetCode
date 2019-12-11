"""
TWO SUM

return indexes of two digits in array that add up to target.

ex.
Inputs: [2, 7, 11, 15], 9

Output: [0, 1]
"""


def twoSum(array, target):
    sortedArray = sorted(array)

    sums = []

    for i in sortedArray:
        if i > target:
            return sums
        else:
            if target - i in array:
                found = []
                found.append(i)
                found.append(target-i)
                found = sorted(found)
                if not found in sums:
                    sums.append(found)
                continue
            continue

    return sums

a = [2,7,11,15,6,3]
b = 9

#print(twoSum(a, b))


'''
If next is left
    1x > 2x 
    1y = 2y
    
if next is right
    1x < 2x 
    1y = 2y

if next is up
    1x = 2x 
    1y < 2y
    
if next is down
    1x = 2x 
    1y > 2y
    
'''


def minimumTime(points):

    def nextIsHigher(a, b):
        if a[0] > b[0]:
            return True
        return False

    def nextIsRight(a, b):
        if a[1] > b[1]:
            return True
        return False

    def verticallyEqual(a, b):
        if a == b:
            return True
        return False

    def horisontallyEqual(a, b):
        if a == b:
            return True
        return False


    x = points
    steps = 0
    coordinate = x[0]
    print(coordinate)

    for i in x[1:]:
        print(x[1:])
        while coordinate != i:
            print("ok")
            if nextIsRight(coordinate, i): #if the next is right
                print("ok")
                if nextIsHigher(coordinate, i): #if the next is higher & right
                    coordinate[0] += 1
                    coordinate[1] += 1  #move coordinate NorthEast
                    steps+=1
                    continue

                elif horisontallyEqual(coordinate[1],i[1]): # if next is Right and Vertically equal
                    coordinate[0] += 1
                    coordinate[1] += 0
                    steps += 1
                    continue

                else: #if the next is lower & right
                    coordinate[0] += 1
                    coordinate[1] -= 1
                    steps += 1
                    continue



            elif coordinate[0] == i[0]: # if vertically alligned
                if nextIsHigher(coordinate, i): #if next is higher
                    coordinate[0] += 0
                    coordinate[1] += 1
                    steps += 1
                    continue
                else:
                    coordinate[0] += 0
                    coordinate[1] -= 1
                    steps += 1
                    continue



            else: #if the next is left
                if nextIsHigher(coordinate, i): #if the next is higher and left
                    coordinate[0] -= 1
                    coordinate[1] += 1  #move coordinate NorthWest
                    steps += 1
                    continue

                elif horisontallyEqual(coordinate[1],i[1]): # if next is Right and Vertically equal
                    coordinate[0] -= 1
                    coordinate[1] += 0
                    steps += 1
                    continue

                else: #if the next is lower and left
                    coordinate[0] -= 1
                    coordinate[1] -= 1
                    steps += 1
                    continue

    return steps



points = [[1,1],[3,4],[-1,0]]
print(minimumTime(points))



# xi = [0, 0]
# zi = [0, 3]
# xi[0] += 1
# print(xi)
# if xi != zi:
#     print("nah")





"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y.

The result of this smash is:

    If x == y, both stones are totally destroyed;

    If x != y, the stone of weight x is totally destroyed,
    and the stone of weight y has new weight y-x.


At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)

"""

def smashing_stones(stones):
    if len(stones) == 1:
        return stones[0]

    stones = sorted(stones)
    stones.reverse()

    largest = stones[0]

    for i in stones:
        if i == largest:
            largest = 0
        else:
            largest = abs(i-largest)

    return largest

#stones = [2,7,4,1,8,1]
stones = [1,3]
print(smashing_stones(stones))
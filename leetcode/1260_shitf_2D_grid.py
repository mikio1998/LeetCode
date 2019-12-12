"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] becomes at grid[i][j + 1].
Element at grid[i][n - 1] becomes at grid[i + 1][0].
Element at grid[n - 1][n - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

"""
def pop_and_add(grid, k):
    length = len(grid[0]) #length of a subarray

    new_grid = []
    for i in grid:
        new_grid += [x for x in i]

    for i in range(k):
        popped = new_grid.pop()
        new_grid.insert(0, popped)

    answer = []
    index = 0

    for i in range(len(grid)):
        temp_arr = []
        for x in range(length):
            temp_arr.append(new_grid[index])
            index += 1
        answer.append(temp_arr)

    return answer



grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 2
print(pop_and_add(grid,k))
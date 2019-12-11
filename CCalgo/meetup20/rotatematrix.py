"""
INPUT
[[ 1, 2, 3, 4, 5 ],
 [ 6, 7, 8, 9, 10 ],
 [ 'A', 'B', 'C', 'D', 'E' ],
 [ 'F', 'G', 'H', 'I', 'J' ]]

OUTPUT
[[ 'F', 'A', 6, 1 ],
 [ 'G', 'B', 7, 2 ],
 [ 'H', 'C', 8, 3 ],
 [ 'I', 'D', 9, 4 ]]
 [ 'J', 'E', 10, 5 ]]
"""

def rotate(matrix):
    output = []
    row = []
    index = 0

    for x in range(len(matrix[0])): #5
        for i in range(len(matrix)): #4
            row.append(matrix[index][x])
            index += 1
        row = row[::-1]
        output.append(row)
        row = []
        index = 0
    return output


input = [[ 1, 2, 3, 4, 5 ],
 [ 6, 7, 8, 9, 10 ],
 [ 'A', 'B', 'C', 'D', 'E' ],
 [ 'F', 'G', 'H', 'I', 'J' ]]

print(rotate(input))
A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

result = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

result = [[A[m][n] for m in range(len(A))] for n in range(len(A[0]))]
    


def printMatrix(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()


printMatrix(A)
print()
printMatrix(result)

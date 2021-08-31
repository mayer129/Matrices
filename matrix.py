from os import linesep
from matrixSample import A

def importWordSearch():
    file = open('wordSample.txt', 'r')
    Lines = file.readlines()
    arr1 = []
    for line in Lines:
        stripped = ''.join(line.split())
        arr2 = []
        for element in stripped:
            arr2.append(element)
        arr1.append(arr2) 
    return arr1


def transpose(A):
    result = [[A[m][n] for m in range(len(A))] for n in range(len(A[0]))]
    return result

def printMatrix(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()
    print()

printMatrix(A)
printMatrix(transpose(A))
printMatrix(importWordSearch())
printMatrix(transpose(importWordSearch()))


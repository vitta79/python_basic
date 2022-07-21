matrixA=[
    [2, 5, 8],
    [3, 7, 9],
    [1, 0, 4]
]
matrixB=[
    [0, 7, 2],
    [3, 5, 0],
    [3, 3, 3]
]
matrixC=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def printMartix(matris):
    for i in matris:
        for j in i:
            print(str(j)+" ")
        print("\n")
printMartix(matrixA)


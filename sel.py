def showMatrix(matrix):
    for i in range(0,len(matrix[0])):
        print("[\t")
    for j in range(0,len(matrix)):
        print(matrix[i][j])
    print("]\t")
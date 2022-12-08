class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroList = []
        for i in range(len(matrix)):
            row = matrix[i]
            if 0 in row:
                for j in range(len(row)):
                    if row[j] == 0:
                        zeroList.append((i,j))
        for item in zeroList:
            row = item[0]
            column = item[1]
            for i in range(len(matrix)):
                matrix[i][column] = 0
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
                

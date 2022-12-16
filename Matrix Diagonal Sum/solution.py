class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        if len(mat) % 2 == 0:
            index = 0
            for i in range(len(mat)):
                total += mat[i][index]
                index = index + 1
            index = 0
            for i in reversed(range(len(mat))):
                total += mat[i][index]
                index = index + 1
        else:
            index = 0
            middle = len(mat) // 2
            for i in range(len(mat)):
                if i == middle:
                    index += 1
                    continue
                total += mat[i][index]
                index = index + 1
            index = 0
            for i in reversed(range(len(mat))):
                if i == middle:
                    index += 1
                    continue
                total += mat[i][index]
                index += 1
            
            total += mat[middle][middle]
        return total

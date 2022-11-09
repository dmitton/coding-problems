class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            print(answer)
            newRow = []
            if i == 0:
                newRow.append(1)
                answer.append(newRow)
            else:
                counter = 1
                while counter <= i + 1:
                    if counter == 1 or counter == (i + 1):
                        newRow.append(1)
                        counter = counter + 1
                    else:
                        num1 = counter - 1
                        num2 = counter - 2
                        number1 = answer[i - 1][num1]
                        number2 = answer[i - 1][num2]
                        newNumber = number1 + number2
                        newRow.append(newNumber)
                        counter = counter + 1
                answer.append(newRow)
        return answer

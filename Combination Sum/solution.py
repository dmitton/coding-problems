class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        
        def dfs(i, tempList, total):
            if total == target:
                answers.append(tempList.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            tempList.append(candidates[i])
            dfs(i, tempList, total + candidates[i])
            tempList.pop()
            dfs(i + 1, tempList, total)
            
            return
        
        dfs(0, [], 0)
        
        return answers

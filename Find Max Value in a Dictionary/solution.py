class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        print(dictionary)
        return max(dictionary, key=dictionary.get)

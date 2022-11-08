class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counter = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                if counter < len(nums2):
                    nums1[i] = nums2[counter]
                    counter = counter + 1
        nums1.sort()
        return nums1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]
        while left <= right:
            mid = (left + right)//2
            if nums[left]<= nums[mid]:
                result = min(nums[left], result)
                left = mid + 1 
            else:
                result = min(nums[mid], result)
                right = mid - 1
        return result
        
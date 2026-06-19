class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        count=0
        for i in range(len(nums)):
            count+=nums[i]
            if count==s:
                return i
            s-=nums[i]
        return -1
   
class Solution:
    def solve(self, nums):
        return sorted(x * x for x in nums)
ob = Solution()
nums = [1,2,4,8,9,10,15,18,20,35,38,69]
print(ob.solve(nums))
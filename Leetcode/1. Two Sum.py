class Solution:
    def twoSum(self, nums:int, target: int):
        
        for index in range(len(nums)):
            num = target - nums[index]
            nums.pop(index)
            print(nums)
            if num in nums:
                print( index , nums.index(num)+1)
                
            else:
                nums.insert(index,num[index])
                pass


nums = [3,5,4,7]
target = 9
obj = Solution()
obj.twoSum(nums, target)
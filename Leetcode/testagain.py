class Solution:
    def twoSum(self, nums, target) :
        for index in range(len(nums)):
            for count in range(len(nums)):
                print(count)
                if index == count:
                    pass
                    print(index,count)
                              
                elif nums[index]+nums[count] == target:
                    return index , count


nums = [2,7,11,15]
target = 4
obj=Solution()
obj.twoSum(nums, target)
        
    

        
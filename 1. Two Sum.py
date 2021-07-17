class Solution(object):
    def twoSum(self, nums, target):
        #print(nums)
        nums_index = [(i, indices ) for indices , i in enumerate(nums)]
        nums_index.sort()
        #print(nums_index)
        start, end = 0, len(nums) - 1
        while start < end:
            current = nums_index[start][0] + nums_index[end][0]
            if current == target:
                return [nums_index[start][1], nums_index[end][1]]
            elif current < target:
                start += 1
            else:
                end -= 1
        
if __name__ == '__main__':
    sol = Solution()
    #print sol.twoSum([2,7,11,15], 9)
    print sol.twoSum([3, 2, 4], 6)
    #print sol.twoSum([3, 3], 6)
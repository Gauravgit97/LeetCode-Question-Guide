# In this problem we have an arry(in python we have a list) we need to traverse it and get the index number which hols the values those sum is equeal to the target value.


# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# The answer time complexity is o(n^2)  --->Which makes it worst(in terms of time complexity ) answer but it is very easy to understand.


class Solution(object):
    def twoSum(self, nums, target):

# Here nums= the list and the target= the targeted value which we want

        for i in range(0,len(nums)):     # ---->This i get the first index and start with 0.
            for j in range(i+1,len(nums)):    #-----> Here we don't want same index again that's the reason we start i+1.
                sum = nums[i]+nums[j]
                if sum == target:
                    return [i,j]
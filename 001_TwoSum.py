#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


def twoSum(nums, target: int):
        len_of_nums = len(nums)
        indeces = []
        for i in range(len_of_nums-1):
            if nums[i] + nums[i+1] == target:
                indeces.append(i)
                indeces.append(i+1)
        return indeces

print(twoSum([2,7,11,15],9))
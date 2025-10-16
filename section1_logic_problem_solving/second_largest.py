def second_largest(nums):
    """Returns the second-largest number in a list of integers."""
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]


numbers = [4, 1, 7, 3, 7, 5]
print("Second largest number:", second_largest(numbers))
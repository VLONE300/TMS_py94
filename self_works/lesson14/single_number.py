def get_single_number(nums):
    d = {nums.count(i): i for i in nums}
    return d[min(d)]


print(get_single_number([4, 1, 2, 1, 2]))

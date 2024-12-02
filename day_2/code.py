file = "input.txt"

with open(file) as f:
    data = f.readlines()


def is_safe(nums):
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) < 1 or abs(nums[i] - nums[i + 1]) > 3:
            return False

    is_decreasing = True
    is_increasing = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            is_increasing = False
        if nums[i] < nums[i + 1]:
            is_decreasing = False

    return is_increasing or is_decreasing


def sol_1():
    res = 0
    for line in data:
        nums = line.strip().split()
        nums = list(map(int, nums))
        if is_safe(nums):
            res += 1

    return res


def sol_2():
    res = 0
    for line in data:
        nums = line.strip().split()
        nums = list(map(int, nums))
        for i in range(len(nums)):
            ncop = nums.copy()
            ncop.pop(i)
            if is_safe(ncop):
                res += 1
                break
    return res


print(sol_1())  # 559
print(sol_2())  # 601

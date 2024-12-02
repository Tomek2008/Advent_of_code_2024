file = "input.txt"

with open(file) as f:
    data = f.readlines()


def sol_1():
    res = 0
    left, right = [], []
    for line in data:
        a, b = line.strip().split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    for i in range(len(left)):
        res += abs(left[i] - right[i])

    return res


def sol_2():
    res = 0
    left, right = [], []
    for line in data:
        a, b = line.strip().split()
        left.append(int(a))
        right.append(int(b))

    for i in range(len(left)):
        res += (left[i] * right.count(left[i]))

    return res


print(sol_1())  # 2378066
print(sol_2())  # 18934359

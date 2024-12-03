import re

file = "input.txt"
with open(file) as f:
    data = f.read()


def sol_1():
    res = 0
    mul = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    for m in mul:
        res += int(m[0]) * int(m[1])

    return res


def sol_2():
    res = 0
    mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    do = True
    for m in mul:
        if m == "don't()":
            do = False
        elif m == "do()":
            do = True

        elif do:
            m = m.removeprefix("mul(")
            m = m.removesuffix(")")
            a , b = m.split(",")
            res += int(a) * int(b)
    return res


print(sol_1())  # 187833789
print(sol_2())  # 94455185

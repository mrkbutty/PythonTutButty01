def max3(one, two, three):
    return max(one, two, three)


def maxlist(numlist):
    maxnum = 0
    for i in numlist:
        if i > maxnum:
            maxnum = i
    return maxnum


def maxargs(*args, graph=False):
    maxnum = 0
    for i in args:
        if i > maxnum:
            maxnum = i
    if graph:
        return '*' * maxnum
    else:
        return maxnum



print(max3(1, 3, 2))
print(maxlist((12, 69, 13)))
print(maxargs(33, 77, 66, graph=True))
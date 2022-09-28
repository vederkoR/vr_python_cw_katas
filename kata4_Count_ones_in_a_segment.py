from math import factorial


def ones_count_for_number(a):
    i = 1
    n = 0
    sum_ones = 0
    while a != 0:
        if a == 1:
            sum_ones += n + 1
            break
        if a == 2:
            sum_ones += 2 * n + 2
            break
        if a == 3:
            sum_ones += 3 * n + 4
            break
        while a >= 2 ** i:
            i += 1
        i -= 1
        a = a - 2 ** i
        for k in range(i):
            z = (i + n - k) * factorial(i) / (factorial(i - k) * factorial(k))
            sum_ones += z
        sum_ones += (n + 1)
        i = 1
        n += 1
    return sum_ones


def count_ones(left, right):
    return ones_count_for_number(right) - ones_count_for_number(left - 1)
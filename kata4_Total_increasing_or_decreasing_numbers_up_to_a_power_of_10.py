# slow
def total_inc_dec_slow(x):
    if x == 0:
        return 1
    elif x == 1:
        return 10
    elif x == 2:
        return 100
    first = 2 * "123456781" + 2 * "123456721" + 2 * "123456321" + 2 * "123454321" + "123456789" + "AABBCCDDE" + 10 * "0"
    for i in range(x - 2):
        length = len(first)
        first = first.replace("2", "12").replace("3", "123").replace("4", "1234").replace("5", "12345").replace(
            "6", "123456").replace("7", "1234567").replace("8", "12345678").replace("9", "123456789").replace(
            "A", "A123456781").replace("B", "B123456721").replace("C", "C123456321").replace(
            "D", "D123454321").replace("E", "E123456789").replace("0", "") + "0" * length
    return len(first)


# quick:
from decimal import Decimal


def total_inc_dec(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 100

    a = [(sum([Decimal(
        (17 * 1 + 15 * (x + 1) + 13 * ((x + 1) * (x + 2) / 2) + 11 * ((x + 1) * (x + 2) * (x + 3) / (2 * 3)) \
         + 9 * ((x + 1) * (x + 2) * (x + 3) * (x + 4) / (4 * 3 * 2)) + 7 * (
                 (x + 1) * (x + 2) * (x + 3) * (x + 4) * (x + 5) / (5 * 4 * 3 * 2)) + 5 * (
                 (x + 1) * (x + 2) * (x + 3) * (x + 4) * (x + 5) * (x + 6) / (6 * 5 * 4 * 3 * 2)) + 3 * (
                 (x + 1) * (x + 2) * (x + 3) * (x + 4) * (x + 5) * (x + 6) * (x + 7) / (
                 7 * 6 * 5 * 4 * 3 * 2)) + (
                 x + 1) * (x + 2) * (x + 3) * (x + 4) * (x + 5) * (x + 6) * (x + 7) * (x + 8) / (
                 8 * 7 * 6 * 5 * 4 * 3 * 2))) for x in range(j - 2)]) + 9) for j in range(n + 2)]

    result = sum(a[3:])
    return result + 10


print(total_inc_dec(196))
import random

num0 = list('111'
            '101'
            '101'
            '101'
            '111')
num1 = list('001'
            '001'
            '001'
            '001'
            '001')
num2 = list('111'
            '001'
            '111'
            '100'
            '111')
num3 = list('111'
            '001'
            '111'
            '001'
            '111')
num4 = list('101'
            '101'
            '111'
            '001'
            '001')
num5 = list('111'
            '100'
            '111'
            '001'
            '111')
num6 = list('111'
            '100'
            '111'
            '101'
            '111')
num7 = list('111'
            '001'
            '001'
            '001'
            '001')
num8 = list('111'
            '101'
            '111'
            '101'
            '111')
num9 = list('111'
            '101'
            '111'
            '001'
            '111')

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

weights = []
for i in range(15):
    weights.append(0)

bias = 7


def proceed(number):
    net = 0
    for i in range(15):
        net += int(number[i]) * weights[i]
    return net >= bias


def decrease(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] -= 1


def increase(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] += 1


for i in range(10000):
    option = random.randint(0, 9)
    if option != 5:
        if proceed(nums[option]):
            decrease(nums[option])
    else:
        if not proceed(num5):
            increase(num5)
print(weights)
print("0 это 5? ", proceed(num0))
print("1 это 5? ", proceed(num1))
print("2 это 5? ", proceed(num2))
print("3 это 5? ", proceed(num3))
print("4 это 5? ", proceed(num4))
print("6 это 5? ", proceed(num6))
print("7 это 5? ", proceed(num7))
print("8 это 5? ", proceed(num8))
print("9 это 5? ", proceed(num9), '\n')
print("Узнал 5? ", proceed(num5))
print("Узнал 5 - 1? ", proceed(num51))
print("Узнал 5 - 2? ", proceed(num52))
print("Узнал 5 - 3? ", proceed(num53))
print("Узнал 5 - 4? ", proceed(num54))
print("Узнал 5 - 5? ", proceed(num55))
print("Узнал 5 - 6? ", proceed(num56))
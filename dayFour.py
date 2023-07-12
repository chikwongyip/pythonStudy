"""
水仙花数
三位数字每位的立方之和刚好等于该数字
先获取所有的三位数 100 - 999
然后获取每位数的百分位，十分位，个位
"""
for x in range(100,1000):
    low = int(x % 100)
    mid = x // 10 % 10
    high = x // 100
    if x == low ** 3 + mid ** 3 + high ** 3:
        print(x)
"""
整数翻转
"""
num = int(input("请输入3位正整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

for x in range(0,20):
    for y in range(0,33):
        z = 100 - x - y
        if 5 * x + y * 3 + z / 3 == 100:
            print(x, y, z)


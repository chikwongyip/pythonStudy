# 将华氏度转成温度
# 公式为：$C = (F - 32) div 1.8 $
f = float(input("请输入华氏度："))
c = (f - 32) / 1.8
print('%f华氏度等于%f温度' % (f, c))

"""
输入圆的半径计算周长和面积
周长 = 半径 * 2
面积 = pi * 半径平方
"""
r = float(input('请输入半径：'))
print('半径为%f，周长为%f，面积为%f' % (r, r * 2, 3.14 * r**2))

"""
输入年份判断是不是润年
"""

year = int(input("请输入年份:"))
is_leap = year % 4 == 0 and year % 100 != 0 and year % 400 == 0
print(is_leap)


"""
英尺与厘米换算
"""
value = float(input("请输入数值:"))
unit = input("请输入单位:")
if unit == "in" or unit == "英寸":
    print('%f英寸 = %f里面' % (value, 2.54 * value))
elif unit == 'cm' or unit == '里面':
    print('%f里面 = %f英寸' % (value, value / 2.54))
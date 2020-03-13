"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
12321 --> 12321
"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10  # 每循环一次，把先获取的数字进位
    num2 += temp % 10  # 循环获取个位数
    temp //= 10  # 循环获取除个位的整数位
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)

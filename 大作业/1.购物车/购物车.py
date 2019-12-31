# -*- coding: utf-8 -*-
# @Time     : 2019/12/29 17:24
# @Author   : 童庆
# @FileName : 购物车.py
# @Software : PyCharm


'''
需要实现的需求：
1.让用户输入金额
2.选择要购买的商品加入购物车
3.当商品的总监超过你的金额提示余额不足
4.让用户输入N结算，输入Q退出
5.用户退出后提示消费了多少钱，还剩多少
思路：
展示商品 --> 挑选商品 -- > 加入购物车 --> 结算 --> 是否超支(如果超支就减少商品) --> 退出
'''

goods = [
    {'name':'电脑', 'price':'1999'},
    {'name':'鼠标', 'price':'10'},
    {'name':'美女', 'price':'50'},
    {'name':'游艇', 'price':'20'},
    {'name':'火箭', 'price':'250'}
]
# 建立商品表单
shop_car = {}
# 建立客户的购物车  键：列表的索引  值：商品的数量
fei_yong = 0
# 用来计算客户消费金额
new_fei_yong = 0
# 用来重新计算客户超支后的金额
is_round = True
# 用于循环计算超支结算
money = input('请输入您的金额:')
# 让客户设置初始有多少钱用来消费

if money.isdigit():
# 判断输入的金额是否为数字
    while 1:
        for i in range(len(goods)):
            print(i+1, goods[i]['name'], goods[i]['price'])
            # 打印商品表单
        choose = input('请输入您要购买的商品序号(N结算/Q退出)：')
        # 让客户输入需要购买商品的序号
        if choose.isdigit() and 0 < int(choose) <= len(goods):
            # 判断客户输入的商品讯号是否为数字，并且是否在合理范围内
            int_index = int(choose) - 1
            # 把商品序号按照商品列表下标的索引进行存储
            if shop_car.get(int_index) == None:
                shop_car[int_index] = 1
            else:
                shop_car[int_index] += 1
            # 把用户商品添加到到购物车
            for k in shop_car:
                print(goods[k]['name'], shop_car[k])
            # 购物后显示已购买的商品和数量
        elif choose.upper() == 'N':
            # 结算  ... == pass
            for f in shop_car:
                fei_yong = fei_yong + shop_car[f] * int(goods[f]['price'])
                # 计算消费金额
                if int(money) >= fei_yong:
                    # 如果客户没有超支
                    for k in shop_car:
                        print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
                        # 打印客户购买的产品名称，单价和数量
                else:
                # 如果客户超支
                    while is_round:
                        # 循环计算，知道客户消费不超支
                        if fei_yong > int(money) or new_fei_yong > int(money):
                            # 用来提示客户超支
                            print('用户您好，您的余额不足了！')
                        for i, v in enumerate(shop_car):  # 枚举
                            print(f'{i+1} {goods[i]["name"]} {shop_car[i]}')
                            # 打印客户购买商品的序号，名称和数量
                        str_del = int(input('请删除商品对应的序号：'))
                        # 让客户输入需要舍弃的产品序号
                        shop_car[str_del -1] -= 1
                        # 每输入一次舍弃一件产品
                        new_fei_yong = 0
                        # 把金额重置为零，用于下次循环计算
                        for i in range(len(shop_car)):
                            new_fei_yong = new_fei_yong + int(goods[i]['price']) * shop_car[i]
                            # 计算删除产品的指出
                        print(f'您好，您现在消费了{new_fei_yong}')
                        if new_fei_yong <= int(money):
                            # 如果用户不超支，结束循环
                            print(f'您好，您一共消费了{new_fei_yong}')
                            is_round = False
                        else:
                            # 如果超支，继续循环
                            print(f'您还是超值啦!一共超支了{new_fei_yong - int(money)}')
                            is_round = True
        elif choose.upper() == 'Q':
            # 退出,退出后显示客户消费金额和余额
            if fei_yong <= int(money):
                print(f'您此次共消费{fei_yong},余额{int(money)-fei_yong}')
            else:
                print(f'您此次共消费{new_fei_yong},余额{int(money) - new_fei_yong}')
            break
        else:
            # 输入的商品序号不在范围内，并且不结算也不退出
            print('输入有误，请重新输入')
else:
    # 输入的金额不是数字
    print('请正确输入金额')
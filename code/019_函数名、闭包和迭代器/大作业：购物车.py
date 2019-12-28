# -*- coding: utf-8 -*-
# @Time     : 2019/12/27 22:20
# @Author   : 童庆
# @FileName : 大作业：购物车.py
# @Software : PyCharm


'''
让用户输入金额
选择要购买的商品加入购物车
当商品的总监超过你的金额提示余额不足
让用户输入N结算，输入Q退出
用户退出后提示消费了多少钱，还剩多少
'''
goods = [
    {'name':'电脑', 'price':'1999'},
    {'name':'鼠标', 'price':'10'},
    {'name':'美女', 'price':'50'},
    {'name':'游艇', 'price':'20'},
    {'name':'火箭', 'price':'250'}
]

shop_car = {}  # 键：列表的索引  值：商品的数量
fei_yong = 0
money = input('请输入您的金额:')
if money.isdigit():
    # 这是真钱
    # 显示商品
    while 1:
        for i in range(len(goods)):
            print(i+1, goods[i]['name'],goods[i]['price'])

        choose = input('请输入您要购买的商品序号(N结算/Q退出)：')
        if choose.isdigit() and 0 < int(choose) <= len(goods):
            # 让用户输入商品序号并判断是不是数字，以及在不在正常输入范围内
            # int_index商品序号
            int_index = int(choose) - 1
            # 通过用户输入的内容减一获取到goods的索引
            if shop_car.get(int_index) == None:
                shop_car[int_index] = 1
            else:
                shop_car[int_index] += 1
            # 让用户把商品加入到购物车
            for k in shop_car:
                print(goods[k]['name'], shop_car[k])
            # 购物后显示已购买的商品和数量
        elif choose.upper() == 'N':
            # 结算  ... == pass
            for f in shop_car:
                fei_yong = fei_yong + shop_car[f] * int(goods[f]['price'])
                if int(money) >= fei_yong:
                    for k in shop_car:
                        print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
                else:
                    print('余额不足')
                    for i,v in enumerate(shop_car): # 枚举
                        print(f'{i+1}{goods[i]["name"]}{shop_car[v]}')
                    str_del = int(input('请删除商品对应的序号：'))
                    shop_car[str_del -1] = shop_car[str_del - 1] -1
                    for f in shop_car:
                        fei_yong = 0
                        fei_yong = fei_yong + shop_car[f] * int(goods[f]['price'])
                        if int(money) >= fei_yong:
                            for k in shop_car:
                                print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
                    # 退款需求还没有完成
                    # else:
                    #
                    #     print('余额还是不足')
                    #     str_del = int(input('请删除商品对应的序号：'))
                    #     shop_car[str_del - 1] = shop_car[str_del - 1] - 1
                    #     fei_yong = fei_yong + shop_car[f] * int(goods[f]['price'])

        elif choose.upper() == 'Q':
            # 退出
            print(f'您此次共消费{fei_yong},余额{int(money)-fei_yong}')
            break
        else:
            print('输入有误，请重新输入')
else:
    # 这是假钱
    print('请正确输入金额')
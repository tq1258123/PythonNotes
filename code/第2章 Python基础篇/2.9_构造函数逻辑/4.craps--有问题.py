"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

思路：玩家有固定的赌资
     计算玩家参与的次数和输赢情况
"""
from random import randint

money = 1000
count_first_win = 0
count_first_lose = 0
count_second_win = 0
count_second_lose = 0

while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
        else:
            print('请输入正确的金额')
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        count_first_win += 1
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        count_first_lose += 1
        money -= debt
    else:
        needs_go_on = True
        print('没赢没输,请继续摇骰子')

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            count_second_lose += 1
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            count_second_win += 1
            money += debt
            needs_go_on = False
        else:
            print('没赢没输,请继续摇骰子')

print('你总共赢了%d次，输了%d次' % (count_first_win + count_second_win, count_first_lose + count_second_lose))
print('你破产了, 游戏结束!')

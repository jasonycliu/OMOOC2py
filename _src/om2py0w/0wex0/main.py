#-*- coding:utf-8 -*-
''' 20151015基于42行代码设计一个小游戏-猜数字：
功能设计：
1、每次运行游戏（运行main.py）生产一个1-100的随机数
2、游戏玩家可以通过命令行输入自己猜想的数字，得分规则是：
     1）猜中的话：得100分
     2）猜的数字和随机数的差距小于10的话：得90分
     3）猜的数字和随机数的差距大于10小于20：得80分
     4）猜的数字和随机数的差距大于20：得70分
'''
import os
import random  #导入生产随机数的包

def foo(param1, secondParam):

        res = 0
        score = 0

        if param1 > secondParam :
            res = param1 - secondParam
        else:
            res = secondParam - param1

        if res < 10:
            score = 90
        elif res > 10 and res <= 20:
            score = 80
        else:
            score = 70

        return score # 这个是单行注释！


def main():
    print '哈喽，欢迎来到猜数字游戏!'

    print "我们已经为您生成了一个1-100之间的数字"

    randomNumber = random.randint(1,100);

    inputStr = raw_input("请输入你猜的数字哦：")
    inputNumber = int(inputStr)

    print '好的，我们已经检测到您输入是：' + str(inputNumber)

    print '哈哈，经过我们的检测，您的得分是：' + str(foo(inputNumber, randomNumber))

if __name__ == '__main__':
    main()


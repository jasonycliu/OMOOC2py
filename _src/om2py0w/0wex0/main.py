#-*- coding:utf-8 -*-
import os

def foo(param1, secondParam):
        res = param1 + secondParam

        print '%s 加上 %s 等于：%s' % (param1,secondParam,res)

        if res < 50:
            print '这个foo'

        elif (res >= 50) and ((param1 == 42) or secondParam ==24 ):
            print '那个bar'

        else:
            print '哈哈！'

        return res # 这个是单行注释！

        ''' 多行注释这样用，
                多行。。。。'''

def main():
    print 'Hello World!'    #打印hello world！

    print "这是Alice的问候!"
    print '这是Bob的问候!'

    foo(5, 10)

    print '=' * 10
    print '现在的工作目录是： ' + os.getcwd()

    counter = 0
    counter += 1

    food = ['apple', 'oranges', 'cat']

    for i in food:
        print '我喜欢吃： ' + i

    print '数数到10:'
    for i in range(10):
        print i

if __name__ == '__main__':
    main()


#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as cc
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cc.add(a, b)))
    print("{} - {} = {}".format(a, b, cc.sub(a, b)))
    print("{} * {} = {}".format(a, b, cc.mul(a, b)))
    print("{} / {} = {}".format(a, b, cc.div(a, b)))

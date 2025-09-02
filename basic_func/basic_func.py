def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return 0


def power(base, pow):
    return base ** pow


def square(base):
    return base ** 2


def greet(이름="낯선자", 나이=20):
    msg=""
    if 나이 < 20:
        msg = "안녕 "+ 이름 + "!"
    elif 나이 == 20:
        msg = "안녕하신가 "+ 이름 + "!"
    else:
        msg = "안녕하십니까 "+ 이름 + "!"

    return msg
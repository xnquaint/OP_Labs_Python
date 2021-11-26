def maxVal(x, y):
    return x if x > y else y


def initVal():
    global a
    global b
    global c
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))


def theValueOfT(a1, b1, c1):
    global t
    t = (maxVal(a1, a1 + b1) + maxVal(a1, b1 + c1)) / (1 + maxVal(a1 + b1 * c1, 1.15))


def outputOfT(t1):
    print(f"The value of T is: {t1}")


a = b = c = t = 0.0
initVal()
theValueOfT(a, b, c)
outputOfT(t)

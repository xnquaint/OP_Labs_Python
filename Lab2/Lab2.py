# Визначити, чи дорівнює одному із заданих чисел r або s
# залишок, отриманий при діленні невідємного цілого числа a
# на додатнє ціле число b.

r = int(input("Input r: "))
s = int(input("Input s: "))
a = int(input("Input a: "))
b = int(input("Input b: "))
if a >= 0 and b > 0:
    ost = a % b
    if ost == r or ost == s:
        result = True
    else:
        result = False
else:
    result = False
print("True") if result is True else print("False")

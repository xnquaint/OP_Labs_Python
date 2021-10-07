# Визначити, чи дорівнює одному із заданих чисел r або s
# залишок, отриманий при діленні невідємного цілого числа a
# на додатнє ціле число b.
print("Input r: ")
r = int(input())
print("Input s: ")
s = int(input())
print("Input a: ")
a = int(input())
print("Input b: ")
b = int(input())
if a >= 0 and b > 0:
    ost = a % b
    if ost == r or ost == s:
        result = True
    else:
        result = False
else:
    result = False
print("True") if result == True else print("False")

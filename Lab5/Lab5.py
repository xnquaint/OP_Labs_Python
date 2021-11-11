factorial = 1
definition = False
a = b = c = 0
number = int(input("Enter the number: "))

if number < 0:
    print("You should start from 0")
    exit(0)
else:
    for i in range(number, 0, -1):
        factorial *= i
    for n in range(1, factorial, 1):
        c = b
        b = a
        a = n
        composition = a*b*c
        if composition == factorial:
            definition = True
            break

print(f"The factorial is: {factorial}")
print(f"It can be divided into: {c}*{b}*{a}") if definition is True else print("It can't be divided")


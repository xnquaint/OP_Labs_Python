import sys

# Визначити, скільки повних годин(h) і повних хвилин(m)
# пройшло з початку доби до k-ої її секунди

print("Input the number of seconds")
seconds = int(input())
if seconds > 86400  or seconds < 0:
    print("There are only 86400 seconds in a single day. Please try again.")
    sys.exit()
hours = seconds // 3600
minutes = int(seconds % 3600 / 60)
print(f"The number of hours is {hours}, the number of minutes is {minutes}")


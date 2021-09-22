import sys

# Визначити, скільки повних годин(h) і повних хвилин(m)
# пройшло з початку доби до k-ої її секунди
SecDay = 86400
SecMinute = 60
print("Input the number of seconds")
seconds = int(input())
if seconds > SecDay  or seconds < 0:
    print("There are only 86400 seconds in a single day. Please try again.")
    sys.exit()
hours = seconds // SecDay
minutes = int(seconds % SecDay / SecMinute)
print(f"The number of hours is {hours}, the number of minutes is {minutes}")


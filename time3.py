# -*- coding: utf-8 -*-
"""Time3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P1pV4zYCVPWZf4hwULiuRcHODoyXaNaM
"""

import time
# Y=Year, m=month, d=day, I=hours, M=minutes, S=second, p=am/pm
timestamp1 = time.strftime('%I:%M:%S %p')
print("Time: ", timestamp1)
date = time.strftime('%Y-%m-%d')
print("Date:", date)
day = time.strftime('%A')
print("Day:", day)
hour = int(time.strftime('%I'))
print("Hour:", hour)
minute = time.strftime('%M')
print("Minute:", minute)
second = time.strftime('%S')
print("Second:", second)
ampm = time.strftime('%p')
print("AM/PM:", ampm)

# Check the times and generate the message according to the time
if ampm == 'AM':
    if hour < 12:
        print("Good Morning Sir")
    else:
        print("Good Afternoon Sir")
elif ampm == 'PM':
    if hour < 5:
        print("Good Afternoon Sir")
    elif hour < 8:
        print("Good Evening Sir")
    else:
        print("Good Night Sir")
else:
    print("Good Evening Sir")
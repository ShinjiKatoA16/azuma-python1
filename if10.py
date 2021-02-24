# python1 P17 if10

time = input('input time=>')

###
time = int(time)
if 0 <= time and time <= 11:
    print('AM')
elif 12 <= time and time <= 23:
    print('PM')
else:
    print('???')
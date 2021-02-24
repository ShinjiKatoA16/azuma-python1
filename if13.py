# python1 P21 if13

japanese = input('japanese test score=>')
programming = input('programming test score=>')

###
japanese = int(japanese)
programming = int(programming)

if japanese >= 70:
    if programming >= 70:
        print('excellent!')
    else:  # japanese >= 70 and programming < 70
        print('good japanese score!')
else: # japanese < 70
    if programming >= 70:
        print('good programming score')
    else:
        print('do your best!')
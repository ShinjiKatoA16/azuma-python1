# python1 P13 if07

score = input('input score=> ')

###
int_score = int(score)

if int_score > 100:
    print('???')
elif int_score >= 90:
    print('great!')
elif int_score >= 70:
    print('good')
elif int_score >= 50:
    print('passing')
else:
    print('failing')
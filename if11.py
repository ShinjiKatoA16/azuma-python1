# python1 P18 if11

month = input('input month=>')

###
if month in ['3', '4', '5']:
    print('spring')
elif month in ['6', '7', '8']:
    print('summer')
elif month in ['9', '10', '11']:
    print('autumn')
elif month in ['12', '1', '2']:
    print('winter')
else:
    print('invalid!')
# python1 P12 if06

str_num_a = input('input number_a => ')
str_num_b = input('input number_b => ')

int_num_a = int(str_num_a)
int_num_b = int(str_num_b)

###
if int_num_a > int_num_b:
    print(int_num_a)
elif int_num_b > int_num_a:
    print(int_num_b)
else:
    print('same value')
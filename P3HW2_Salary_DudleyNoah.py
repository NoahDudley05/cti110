# A calculator for salary.
# CTI-110
# P3HW2 - Salary
# Noah Dudley 
# 11/21/2022
user_name = input('Enter employee\'s name:\n' )
user_hours = float(input('Enter number of hours worked:\n' ))
user_rate = float(input('Enter employee\'s pay rate:\n' ))
print('---------------------------------')

if user_hours > 40:
    user_ot = user_hours - 40
else:
    user_ot = 0
if user_hours > 40:
    user_otpay = ((user_hours - 40) * (user_rate * 1.5))
    user_pay = ((user_hours - user_ot) * user_rate)
else:
    user_pay = (user_rate * user_hours)
    user_otpay = 0
if user_hours > 40:
    gross_pay = user_otpay + user_pay
else:
    gross_pay = user_pay

print('Employee name:', user_name)
print('')
print('Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay')
print('-----------------------------------------------------------------------------------')
print(str(user_hours).rjust(4), str(user_rate).rjust(15), str(user_ot).rjust(12), str(user_otpay).rjust(12), str(user_pay).rjust(15), str(gross_pay).rjust(15))

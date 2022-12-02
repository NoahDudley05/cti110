# CTI-110
# P4HW2 - Salary Calculator
# Noah Dudley 
# 12/1/2022
# A calculator for multiple salaries.
elist = []
otlist = []
regpaylist = []
grosslist = []
ename = input('Enter employee\'s name or "None" to terminate: ')
if ename != 'None':
    while ename != 'None':
        ehours = float(input(f'How many hours did {ename} work?: '))
        epay = float(input(f'What is {ename} pay rate?: '))
        elist.append(ename)
        print('---------------------------------')
        if ehours > 40:
            user_ot = ehours - 40
        else:
            user_ot = 0
        if ehours > 40:
            user_otpay = ((ehours - 40) * (epay * 1.5))
            user_pay = ((ehours - user_ot) * epay)
            otlist.append(user_otpay)
            regpaylist.append(user_pay)
        else:
            user_pay = (epay * ehours)
            user_otpay = 0
            regpaylist.append(user_pay)
            otlist.append(user_otpay)
        if ehours > 40:
            gross_pay = user_otpay + user_pay
            grosslist.append(gross_pay)
        else:
            gross_pay = user_pay
            grosslist.append(gross_pay)

        print('Employee name:', ename)
        print('')
        print('Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay')
        print('-----------------------------------------------------------------------------------')
        print(str(ehours).rjust(4), str(epay).rjust(15), str(user_ot).rjust(12), str(user_otpay).rjust(12), str(epay).rjust(15), str(gross_pay).rjust(15))
        print()
        ename = input('Enter employee\'s name or "None" to terminate: ')
        print()

    else:
        print('Total number of employees entered: ', len(elist))
        print('Total amount payed for overtime: ', sum(otlist))
        print('Total amount payed for regular hours: ', sum(regpaylist))
        print('Total amount payed in gross: ', sum(grosslist))
else:
    print('There are no employee\'s')

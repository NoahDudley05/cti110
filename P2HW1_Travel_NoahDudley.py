
 # An Updated calculator to see travel expenses.
    # 11/3/2022
    # CTI-110 P1HW2 - Travel Expense
    # Noah Dudley
budg_num = int(input('Enter budget:\n'))
dest_num = input('Enter your travel destination:\n')
gas_num = int(input('How much do you think you will spend on gas?\n'))
accom_num = int(input('Approximately, how much will you need for accomodation/hotel?\n'))
food_num = int(input('Last, how much do you need for food?\n'))
total_num = int(gas_num + accom_num + food_num)
print('--------Travel Expenses--------')
print('Location:', '         ',dest_num)
print('Initial Budget:', '     $',float(budg_num))
print('Fuel:', '               $',float(gas_num))
print('Accomodation:', '       $',float(accom_num))
print('Food:', '               $',float(food_num))
print('-------------------------------')
print('')
print('Remaining Balance:', '  $',float(budg_num - total_num))

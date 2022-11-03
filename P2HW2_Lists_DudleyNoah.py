# A program to input grades
    #Noah Dudley
    #11/3/2022
    #CTI-110
module_1 = float(input('Enter grade for Module 1:\n'))
module_2 = float(input('Enter grade for Module 2:\n'))
module_3 = float(input('Enter grade for Module 3:\n'))
module_4 = float(input('Enter grade for Module 4:\n'))
module_5 = float(input('Enter grade for Module 5:\n'))
module_6 = float(input('Enter grade for Module 6:\n'))
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]
module_avg = ((module_1 + module_2 + module_3 + module_4 + module_5 + module_6)/6)
module_sum = (module_1 + module_2 + module_3 + module_4 + module_5 + module_6)
print('------------Results------------')
print('Lowest Grade:', '    ', min(module_grades))
print('Highest Grade:', '   ', max(module_grades))
print('Sum of Grades:', '   ', module_sum)
print('Average:', '         ', f'{module_avg:.2f}')

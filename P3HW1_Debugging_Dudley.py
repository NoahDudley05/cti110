# Debugging this program
# Dudley
#Cti-110
#P3HW1- Debugging


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


grade_low = min(grades)
grade_high = max(grades)
grade_sum = sum(grades)
grade_avg = grade_sum/len(grades)

print('------------Resullts------------')
print('Lowest Grade:', '  ', grade_low)
print('Highest Grade:', ' ', grade_high)
print('Sum of Grades:', ' ', grade_sum)
print('Average:', '       ', format(grade_avg, '.2f'))

print('--------------------------------')

if grade_avg >= 90:
    print('Your grade is: A')
elif grade_avg >= 80:
    print('Your grade is: B')
elif grade_avg >= 70:
    print('Your grade is: C')
elif grade_avg >= 60:
    print('Your grade is: D')               
else:
    print('Your grade is: F')






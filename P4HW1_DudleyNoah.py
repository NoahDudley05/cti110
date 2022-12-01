# CTI-110
# P4HW1 - Score List
# Noah Dudley 
# 12/1/2022
# Program to display test scores.
scorelist = []
sn = int(input('How many scores do you want to enter? ', ))
ns = 0
scores = []

while sn > ns:
    ns += 1
    scores = float(input('Enter score #{}: '.format(ns)))
    scorelist.append(scores)

if scores < 0 or scores > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    scores = float(input('Enter score #{} again: '.format(ns)))
    
ls = min(scorelist)
sa = sum(scorelist) / len(scorelist)
ml = scorelist
ml.remove(min(scorelist))

print('--------------Results--------------')
print('Lowest Score  :', ls)
print('Modified List :', ml)
print('Scores Average:', sa)
if sa >= 90:
    print('Your grade is: A')
elif sa >= 80:
    print('Your grade is: B')
elif sa >= 70:
    print('Your grade is: C')
elif sa >= 60:
    print('Your grade is: D')               
else:
    print('Your grade is: F')
print('-----------------------------------')

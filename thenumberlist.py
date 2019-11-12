#Sum/Average Program
#Your first and last name:
#Your student ID:

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
numList = []
count = 0
total = 0
avg = 0

for x in range (0,20):
        num=input("Enter a number:")
        numList.append(num)
        num= int(num)
        count = count + 1
        total = total + num

print('The sum of the number you entered is:', total)

avg= total/count
print('The average of the numbers you entered is:',avg)
#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

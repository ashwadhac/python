# take salary as input, if the person salary is above 90000
# then print "eligible" else print "not eligible"

# TestCase 1
'''
INPUT: 90000
OUTPUT: 'not eligible'
'''

# TestCase 2
'''
INPUT: 120000
OUTPUT: 'eligible'
'''
salary=int(input("Enter the salary:"))
if(salary>90000):
    print("Eligible")
else:
    print("not eligible")
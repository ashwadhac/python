# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

YOB=int(input("Enter your year of birth:"))
currentyear=2026
currentage=currentyear-YOB
print("currentage:",currentage)
if (currentage>=18):
    print("Eligible to vote")
else:
    print("not eligible")
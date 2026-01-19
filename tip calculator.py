print("welcome to the tip calculator!")
bill= float(input("what was the total bill?: "))#type casting string to float
tip=float(input("how much percent tip would you like to give ? 10,12 or 15 : "))
people=float(input("how many people to split the bill? : "))
final_tip=(tip/100)
final_tip+=1#addition assignment operator+=
bill_with_tip= (bill*final_tip)
bill_per_person= (bill_with_tip/people)
print(f"the total bill is : {bill_with_tip}")
print(f"EACH PERSON SHOULD PAY : {(round(bill_per_person , 2 ))}")#round up till 2 digits of decimal
# print(final_bill )            accurate bill 
# print(round(final_bill ))     round it up/down depends of value after point 

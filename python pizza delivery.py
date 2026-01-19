print("welcome to python pizza deliveries ")
size= (input("what size pizza would you like s, m or l?? : "))
pepperoni=(input("do you want pepperoni on your pizza?? yes or no : "))
cheese=(input("do you want extra cheese yes or no ?? : "))
if size=='s' :
    bill=15
    if pepperoni=='yes':
        bill+=2
elif size=='m':
    bill=20
    if pepperoni == 'yes':
        bill+=3
else:
    bill=25
    if pepperoni == 'yes':
        bill+=3
if cheese== 'yes':
    bill+=1
print(f"Your total bill is : {bill}$\n thankyou for your order!!")

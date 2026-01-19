print("welcome to the rollercoster")
height= int(input("what is your heiht in cm ??"))
bill=0
if height > 120:
    age= int(input("what is your age??"))
    if age > 18:
        bill=12
        print("Adult ticket price : $12 ")
    elif 12<age<18:
        bill=7
        print("Youth ticket price : $7 ")
    else :
        bill=5
        print ("kids ticket price : $5 ")
    photo=input("would you like to have a photo yes or no ?")
    if photo == 'yes':
        bill+=3
        print(f"your total bill would be ${bill}")
    else :
        print(f"your bill would be ${bill}")
else:
    print("sorry you have to grow taller to ride ! ")
    
import random
print('''
█▀█ █▀█ █▀▀ █▄▀ 
█▀▄ █▄█ █▄▄ █░█ 

█▀█ ▄▀█ █▀█ █▀▀ █▀█ 
█▀▀ █▀█ █▀▀ ██▄ █▀▄ 

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
''')
user_choice=(int(input('''what do you choose?
type 0 for rock ,1 for paper ,2 for scissors : ''')))
comp_choice = random.randint(0 , 2)
#print (f"the computer choose {comp_choice}")
if user_choice == 0:
    print ("""your choice:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
if user_choice == 1:
    print("""your choice:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
if user_choice == 2:
    print ("""your choice:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if comp_choice == 0:
    print ("""my choice:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
if comp_choice == 1:
    print("""my choice:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
if comp_choice == 2:
    print ("""my choice:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if user_choice == 0 and comp_choice == 2:
    print ("you win !!")
elif user_choice == 0 and comp_choice == 0:
    print ("its a tie !!")
elif user_choice == 1 and comp_choice == 0:
    print ("you win !!")
elif user_choice == 1 and comp_choice == 1:
    print ("its a tie !!")
elif user_choice == 2 and comp_choice == 1:
    print ("you win !!")
elif user_choice == 2 and comp_choice == 2:
    print ("its a tie !!")
elif user_choice >= 3 :
    print("oops what do you mean! please give a valid input to continue the game!")
else:
    print("you loose")

print("welcome to tresure hunt")
print('''  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 You wake up on the shores of a mysterious island. The waves crash
 behind you, and ahead lies a thick jungle. Legends say the island
 hides a chest of unimaginable treasure — but few have ever
 returned...your goal is to find that treasure!! 
 ''')
direction=input("You follow a dirt path that splits in two. WHICH PATH WOULD YOU CHOOSE LEFT OR RIGHT??: ")
if direction =='left':
    print(" this path leads deeper into the jungle, where you can hear distant drums You push through the vines and reach a calm lake In the center, you see a small island shimmering with golden light ")
    do=input("WOULD YOU SWIM or WAIT ??: ")
    if do == 'wait':
        print('''A small rowboat drifts to shore. You climb in and cross safely. On the glowing island, you find a strange stone house with three doors: A red door that smells of smoke.A blue door that echoes with growls.A yellow door glowing softly.''')
        door=input("which colour door would you go in RED,BLUE,YELLOW?? :")
        if door== 'yellow':
            print("you found the tresure and you win this game")
        else :
            print("game over")
    else:
        print("game over-eaten by crocodiles")
else :
    print('''You walk into the cave; it’s dark and echoing. A pair of glowing eyes suddenly appear.A pirate skeleton with a sword blocks your way''')
    fight=input('would you "fight" the skeleton or "run" outside: ')
    if fight=="run":
        print("You escape the cave and follow a narrow path up the cliffs.At the top, you see two routes:A wooden bridge hanging over a canyon. and A hidden tunnel behind a waterfall.")
        cliff=input("would you choose the tunnel or the bridge :")
        if cliff=="tunnel":
            print("WIN (tunnel leads to the treasure vault).")
        else :
            print("you loose the Bridge collapsed ")
    else:
        print("game over-you were Killed by skeleton")
        
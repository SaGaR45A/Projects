print("by Sagar lamba")
loose=("pc wins")
win=("you win")
lives = 5
score=0
draw=0
pc_lives=7
while True:
    print("To start enter your info")
    username=input("enter username:")
    password=input("enter your password:")
    searchfile=open("accounts.csv","r")
    for line in searchfile:
        if username and password in line:
            print("access granted")
            print(" ___________    _________     _________ ")
            print("|           |  |         |   |            ")
            print("|           |  |         |   |            ")
            print("|___________|  |_________|   |_________ ")
            print("|\ \           |                      | ")
            print("| \ \          |                      |")
            print("|  \ \         |                      | ")
            print("|   \ \        |              ________|")
            print("")
            print("live rules\n")
            print("you start with",lives,"lives\n")
            print("if you win you will get extra live\n")
            print("if draw lives stay same\n")
            print("if you loose you will loose one live")
            print("_ _ _ _ _ _ _ _ _ __ _ __ _ _ ")
            print("MAKE SURE DONT USE CAPITALS")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ __ _ ")
            print("to see list of rules type rules")
            print("_ _ _ ___ _ _ _ _ __ _ _ _ _ ")
            print("to leave game type exit")
            print("__ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print("The PC has lives aswell\n")
            print("Can you beat the pc\n")
            print("LETS PLAY")
            print("_ _ _ _ _ _ _ _ _ _  _ _ _")

            while True:
                rps=input("rock, paper, scissors \n ")
                import random
                pc=("rock", "paper", "scissors")
                pc=random.choice(pc)
                #rock if statements
                if rps=="rock" and pc == "paper":
                    print("Pc choose",pc)
                    print("")
                    print("loose")
                    print("")
                    print("")
                    lives-=1
                if rps=="rock" and pc =="scissors":
                    print ("Pc choose",pc)
                    print("")
                    print("win")
                    print("")
                    print("")
                    lives+=1
                    score+=1
                #paper if statements
                if rps=="paper" and pc == "scissors":
                    print("Pc choose",pc)
                    print("")
                    print("loose")
                    print("")
                    print("")
                    lives-=1
                if rps=="paper" and pc == "rock":
                    print("Pc choose",pc)
                    print("")
                    print("win")
                    print("")
                    print("")
                    lives+=1
                    score+=1
                #scissors if statements
                if rps=="scissors" and pc == "paper":
                    print("Pc choose",pc)
                    print("")
                    print("win")
                    print("")
                    print("")
                    lives+=1
                    score+=1
                if rps=="scissors" and pc == "rock":
                    print("Pc choose",pc)
                    print("")
                    print("loose")
                    print("")
                    print("")
                    lives-=1
                #duplicates
                if rps=="rock" and pc == "rock":
                    print("Pc choose",pc)
                    print("")
                    print("its a draw")
                    print("")
                    print("")
                    draw=1
                if rps=="paper" and pc == "paper":
                    print("Pc choose",pc)
                    print("")
                    print("its a draw")
                    print("")
                    print("")
                    draw=1
                if rps=="scissors" and pc == "scissors":
                    print("Pc choose",pc)
                    print("")
                    print("its a draw")
                    print("")
                    print("")
                    draw=1
                #system
                if rps=="rules":
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
                    print(" Rules ")
                    print("_ _ _ _ _ _ _ __ _ _ _ _ _ _ \n")
                    print(" rock looses against paper")
                    print(" ")
                    print(" paper looses against scissors")
                    print(" ")
                    print(" scissors looses against rock")
                    print(" ")
                    print(" rock beats scissors")
                    print(" ")
                    print(" scissors beats paper")
                    print(" ")
                    print(" paper beats rock")
                    print("_ _ _ _ _ _ _ _ _ _ _  _ _ _ ")
                if rps =="dlives":
                    print(lives)
                if rps =="dscore":
                    print(score)
                if rps =="ddraw":
                    print(draw)
                #lives
                if lives== 0 or rps=="test":
                    print("thanks for playing\n")
                    print("out of lives\n")
                    print("you got",score,"correct\n")
                    print("you draw", draw,"times\n")
                    stop= input("press enter to exit")
                    import time
                    time.sleep(900)
                if pc_lives ==0:
                    print("thanks for playing\n")
                    print("pc lost all lives. you win\n")
                    print("you got",score,"correct")
                    print("you draw", draw,"times")
                    stop= input("press enter to exit")
                    import time
                    time.sleep(900)
                #exit
                    if rps=="exit":
                        break
        else:
             print("your username or password is incorrect")
             print("_ _ _ _ _ _ _ _ _  _ _ _ _ _  __  _ _")
                

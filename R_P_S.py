def stone_paper_scissors():
    import os
    clear = lambda:os.system('cls')
    import random
    global con
    con = ["rock","paper","scissors"]

    print("Enter choice: \n",
        "1. Single Player\n",
        "2. Computerized")
    comp = int(input())
    
    print()
    bold = "\033[1m"
    print(bold+"HOW MUCH ROUND WANT TO PLAY:".center(80))

    global t
    t = int(input("\n"))
    clear()

    if comp == 1:
        global user1
        user1 = input("Enter user name :")
        print(bold+"MATCH STARTED:\n".center(80))
        print(f"Enter choice:'r' for rock,'p' for paper,'s' for scissors\n")

        for i in range(t):
            def single_player():
                global user1,t
                def bot():
                    global bots,con
                    bots = random.choice(con)
                bot()
                inp = input()
                print("ROUND",i+1,"\n")
                print(f"{user1} {inp} || computer {bots}")

                if inp == 'r' and bots == 'rock' or inp == 's' and bots == 'scissors' or inp == 'p' and bots == 'paper':
                    print(bold+"Match Tie")

                elif inp == 'r' and bots == 'scissors' or inp == 's' and bots == 'paper' or inp == 'p' and bots == 'rock':
                    print(bold+f"{user1.capitalize()} wins")

                elif inp == 'r' and bots == 'paper' or inp == 's' and bots == 'rock' or inp == 'p' and bots == 'scissors':
                    print(bold+"Computer wins")
            single_player()

    elif comp == 2:
        
        global user2
        user1 = input("Enter 1st user name : ")
        user2 = input("Enter 2nd user name : ")
        global ply1,ply2,player1,player2
        ply1=0;ply2=0

        def repoint():
            global user1,user2,player1,player2

            def again():
                global user1,user2

                def playe1():
                    global player1,con
                    player1 = random.choice(con)
                playe1()
                def playe2():
                    global player2,con
                    player2 = random.choice(con)
                playe2()


                def result():
                    global player1,player2
                    clear()
                    bold = "\033[1m"
                    print(bold+"MATCH STARTED:\n".center(80))
                    print(player1,"  ||  ",player2)

                    global ply1,ply2,user1
                    if (player1=="rock"and player2 =="rock"):
                        print("match draw\n")
                        return(again())
                    elif (player1=="rock"and player2 =="paper"):
                        print(user2,"win")
                        ply2 = ply2+1
                    elif (player1=="rock"and player2 =="scissors"):
                        print(user1,"win")
                        ply1 = ply1+1

                    elif (player1=="paper"and player2 =="rock"):
                        print(user1,"win")
                        ply1 = ply1+1
                    elif (player1=="paper"and player2 =="paper"):
                        print("match draw\n")
                        return(again())
                    elif (player1=="paper"and player2 =="scissors"):
                        print(user2,"win")
                        ply2 = ply2+1

                    elif (player1=="scissors"and player2 =="rock"):
                        print(user2,"win")
                        ply2 = ply2+1
                    elif (player1=="scissors"and player2 =="paper"):
                        print(user1,"win")
                        ply1 = ply1+1
                    elif (player1=="scissors"and player2 =="scissors"):
                        print("match draw\n")
                        return(again())
                result()
            again()

            print(user1,"=",ply1,"||",user2,"=",ply2)

            if(ply1>ply2):
                print(user1,"is winning...")
            elif(ply2>ply1):
                print(user2,"is winning...")
            else:
                print("equal points")

            bold = "\033[1m"

            if(ply1==t):
                n = len(user1)
                def pat():
                    for i in range(n+24):
                        print(bold+":",end="")
                clear()
                print(user1,"=",ply1,"||",user2,"=",ply2)
                print()
                pat()
                print(bold+"\n||",user1,"win with:",ply1-ply2,"points||")
                pat()
                return 0

            if(ply2==t):
                n = len(user2)
                def pat():
                    for i in range(n+25):
                        print(bold+":",end="")
                clear()
                print(user1,"=",ply1,"||",user2,"=",ply2)
                print()
                pat()
                print(bold+"\n||",user2,"win with:",ply2-ply1,"points||")
                pat()
                return 0

            rp = input("\nPress 'Enter' to play again:\n")
            if(rp==""):
                return(repoint())
            else:
                print("!!! Game Over !!!")
        repoint()
stone_paper_scissors()
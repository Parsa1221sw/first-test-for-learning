import classes as fil



def user_menu2(userName):
    
    while(True):
        empty=0
        while(True):
            try:
                print("1.my game\n2.buy game\n3.close")
                empty = int(input())
                if empty<1 or empty>3:
                    raise ValueError("pleas enter the right number \n")
                break
            except ValueError as e:
                print(e)
                print()
                continue
        if empty==2:
            for i in fil.game_database:
                i.show_info()
            while(True):
                print("name : ",end="")
                gamename= input()
                empty2=0
                for i in fil.game_database:
                    if i.name==gamename:
                        i.sell_1_number()
                        empty2=1
                        userName.add_game(gamename)
                if empty2==1:
                    break
                elif empty2==0:
                    print("pleas enter thr right nema of game\n")
                    continue
        elif empty ==1:
            userName.show_games()
        elif empty ==3:
            break
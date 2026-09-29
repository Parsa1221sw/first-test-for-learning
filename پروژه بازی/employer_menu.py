import classes as fil


def  Employer_Menu():
    while(True):
        while(True):
            try:
                print("1.show games\n2.add game\n3.show members\n4.remove members\n5.close")
                flag = int(input())
                if flag<1 or flag>6:
                    raise ValueError("pleas enter the right number\n")
                break
            except ValueError as e:
                print(e)
                print()
                continue
        if flag==2:
            name = ""
            number = 0
            price = 0.0
            print("name : ",end="")
            name = input()
            while(True):
                try:
                    print("number : ",end="")
                    number = int(input())
                    if number <=0:
                        raise ValueError("number can not be zero or negetive\n")
                    break
                except ValueError as e:
                    print(e)
                    print()
                    continue
            while(True):
                try:
                    print("price : ",end="")
                    price = float(input())
                    if price <=0:
                        raise ValueError("price can not be zero or negetive\n")
                    break
                except ValueError as e:
                    print(e)
                    print()
                    continue
            new_game =fil.GAME(name,number,price)
            fil.game_database.append(new_game)
        elif flag==1:
            for i in fil.game_database:
                i.show_info()
            flag2=0
            while(True):
                try:
                    print("1.change\n2.close")
                    flag2= int(input())
                    if flag2<1 or flag2 >2:
                        raise ValueError("pleas enter the right number\n")
                    break
                except ValueError as e:
                    print(e)
                    print()
                    continue
            if flag2==1:
                while(True):
                    game_name= input("enter name of game : ")
                    d=0
                    if i in fil.game_database:
                        if i.name==game_name:
                            d=1
                            print("1.change name\n2.change price\n3.add numer\n")
                    if d==0:
                        print("this game not pleas try agen\n")
                        continue
                    elif d==1:
                        num =0
                        while(True):
                            try:
                                num = int(input())
                                if num <1 or num>3:
                                    raise ValueError("enter right number")
                                break
                            except ValueError as e:
                                print(e)
                                print()
                                continue
                        
                        if num==1:
                            nm = str(input("new name : "))
                            for i in fil.game_database:
                                if i.name==game_name:
                                    i.name=nm
                            break
                        elif num==2:
                            while(True):
                                try:
                                    nm = float(input("new price : "))
                                    if nm <=0:
                                        raise ValueError(" number can not be zero or negetive")
                                    break
                                except ValueError as e:

                                    print(e)
                                    print()
                                    continue
                            
                            for i in fil.game_database:
                                if i.name == game_name:
                                    i.price=nm
                            break
                        elif num==3:
                            while(True):
                                try:
                                    nm = int(input("enter the number"))
                                    if nm <=0:
                                        raise ValueError("number can not be zero or negetive\n")
                                    break
                                except ValueError as e:
                                    print(e)
                                    print()
                                    continue
                            for i in fil.game_database:
                                if i.name ==game_name:
                                    i.number=nm
                            break

        elif flag==3:
            for i in fil.user_database:
                i.show_info()
        elif flag==4:
            for i in fil.user_database:
                i.show_info()
            username=""
            while(True):
                try:
                    username = input("user name : ")
                    f=0
                    for i in fil.user_database:
                        if username==i.user_name:
                            fil.user_database.remove(i)
                            f=1
                    if f==0:
                        raise ValueError("pleas enter the right user name\n")
                    print("user deleted")
                    break
                except ValueError as e:
                    print(e)
                    print()
                    continue
        elif flag==5:
            break           
                
            
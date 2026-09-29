import classes as fil
import user_menu
import employer_menu
fil.begeining_progarm()
while(True):
    try:
        print("pleas chose ")
        print("1.user\n2.employer\n3.colose")
        a = int(input("-----"))
        if a<1 or a>3:
            raise ValueError("pleas enter 1 or 2 : \n")
        
    except ValueError as e:
        print(e)
        print("you must enter integer!!\n")
        continue
    print("---------------------\n")
    if a==1:
        b=0
        while(True):
            try:
                print("pleas chose ")
                print("1.sing in\n2.login")
                b = int(input("-----"))
                if b<1 or b>2:
                    raise ValueError("pleas enter 1 or 2 : \n")
                break
            except ValueError as e:
                print(e)
                print("you must enter integer!!\n")
                continue
        if b==1:
            Name=""
            Code = ""
            Username = "" 
            password = ""
            while(True):
                try:
                    print("name : ",end="")
                    Name = str(input(""))
                    if not Name.isalpha() or not Name.isascii():
                        raise ValueError("just english ")
                    break
                except ValueError as e:
                    print(e)
                    print("------")
                    continue
            while(True):
                try:
                    print("code : ",end="")
                    Code = str(input(""))
                    if not Code.isdigit():
                        raise ValueError("just dijit ")
                    break
                except ValueError as e:
                    print(e)
                    print("------")
                    continue
            while(True):
                print("user name : ",end="")
                flag=0
                Username = str(input())
                print()
                for i in fil.user_database:
                    if i.user_name == fil.user_database:
                        flag+=1
                if flag==0:
                    break
                else:
                    print("this user name used pleas chose another user name\n")
                    continue

            print("password : ",end="")
            password = str(input())
            empty_list = []
            person = fil.User(Name,Code,Username,password, empty_list)
            fil.user_database.append(person)
            user_menu.user_menu2(person)
        elif b==2:
            us = fil.Login_page()
            user_menu.user_menu2(us)

    elif a==2:
        while(True):
            print("user name : ",end="")
            user1= input()
            if user1==fil.employer_user:
                break
            else:
                print("user name not cracct pleas try egan\n")
                continue
        while(True):
            print("password : ",end="")
            user1= str(input())
            if user1==fil.employer_password:
                break
            else:
                print("password not cracct pleas try egan\n")
                continue
        employer_menu.Employer_Menu()
    elif a==3:
        list_for_user = []
        list_for_game = []
        for i in fil.user_database:
            list_for_user.append(i.manage_info())
        fil.dump_user_json(list_for_user)
        for i in fil.game_database:
            list_for_game.append(i.manage_game())
        fil.dump_game_json(list_for_game)
        break

import json

user_database =[]
game_database = []
employer_user = "parsa1385sw"
employer_password  = "parsa1221swsw"
class person:
    def __init__(self,name,natoin_code):
        self.name= name
        self.nation_code= natoin_code


class User(person):
    def __init__(self, name, natoin_code,user_name,password,game):
        self.user_name= user_name
        self.password=password
        super().__init__(name, natoin_code)
        self.game = game

    def manage_info(self):
        dat = {"name": self.name
        ,"nation code": self.nation_code
        ,"user name": self.user_name
        ,"password":self.password
        , "game": self.game
        }
        return dat
    def show_info(self):
        print("-------------------")
        print(f"name : {self.name}")
        print(f"code : {self.nation_code}")
        print(f"user name : {self.user_name}")
        print(f"password : {self.password}")
        print("-------------------")
    def add_game(self,name_of_game):
        self.game.append(name_of_game)
    def show_games(self):
        print("-------------")
        for i in self.game:
            print(i)
        print("-------------")





def load_user_json():
    with open(r"C:\Users\Elm&Fan\Desktop\پروژه بازی\user.json","r") as file:
        data =json.load(file)
        return data
def dump_user_json(data):
    with open(r"C:\Users\Elm&Fan\Desktop\پروژه بازی\user.json","w") as file:
        json.dump(data,file, indent=4)
def load_game_json():
    with open(r"C:\Users\Elm&Fan\Desktop\پروژه بازی\game.json","r") as file:
        data =json.load(file)
        return data
def dump_game_json(data):
    with open(r"C:\Users\Elm&Fan\Desktop\پروژه بازی\game.json","w") as file:
        json.dump(data,file, indent=4)

def Login_page():
    user=""
    while(True):
        print("user name : ",end="")
        user = input()
        flag= 0
        for i in user_database:
            if i.user_name==user:
                flag=1
        if flag==1:
            break
        elif flag==0:
            print("this user name not cracct pleas try egan\n")
            continue
    while(True):
        print("password : ",end="")
        pasw= input()
        flag=0
        for i in user_database:
            if i.user_name==user and i.password==pasw:
                flag=1
        if flag==1:
            break
        elif flag==0:
            print("password not cracct pleas try agen\n")
            continue
    for i in user_database:
        if i.user_name==user:
            return i

class GAME():
    def __init__(self,name,number,price):
        self.name = name
        self.number = number
        self.price = price
    def sell_1_number(self):
        self.number-=1
    def add_number(self,ii):
        self.number+=ii
    def change_price(self,ii):
        self.price=ii
    def change_name(self,ii):
        self.name=ii
    def show_info(self):
        print("-----------")
        print(f"name : {self.name}\nprice : {self.price}\nnumber : {self.number}")
        print("-----------")
    def manage_game(self):
        dat = {
            "name": self.name,
            "price": self.price,
            "number": self.number
        }
        return dat

def begeining_progarm():
    user_data = load_user_json()
    game_data = load_game_json()
    for i in user_data:
        name =i["name"]
        code = i["nation code"]
        user=i["user name"]
        password =i["password"]
        game = i["game"]
        member = User(name,code,user,password,game)
        user_database.append(member)
    for i in game_data:
        name =i["name"]
        price = i["price"]
        number = i["number"]
        gamee = GAME(name,number,price)
        game_database.append(gamee)
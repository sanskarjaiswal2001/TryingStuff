import mysql.connector
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

mydb = mysql.connector.connect(
  host="192.168.1.105",
  user="root",
  passwd="imperialknightphoenix35202810",
  database="login"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM users;")
table=mycursor.fetchall()
user_db = [i[0] for i in table]
pass_db = [i[1] for i in table]
mydb.autocommit=True

def create():
    user_name = input("Enter username:")
    if user_name in user_db :
        print("username already taken!")
        create()
    else:
        user_pass = input("Enter password:")
        user_pass = generate_password_hash(user_pass,method='sha256',salt_length=20)
        mycursor.execute(f"INSERT INTO users VALUES ('{user_name}','{user_pass}');")
    
def login():
    user_name = input("Enter username:")
    user_pass = input("Enter password:")
    b=user_db.index(user_name)
    key = pass_db[b]
    if user_name in user_db and check_password_hash(key,user_pass):
        print("Access Granted!")
    else :
        print("Invalid username or password")

def main():
    global a
    a = input("1:Login \n2:Create Account \nOption:")
    a = int(a)
    if (a==1):
        login()
    elif (a==2):
        create()
main()

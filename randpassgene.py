import random

print("welcome to password generator ")

letters=['a','b','c','d','e','f','g','h','i']
symbols=['!','#','$','%','(',')',"*"]
numbers=['0','1','2','3','4','5','6','7','8','9','10']

letter_num=int(input("dear user enter the numbers of letters you want in the password"))
symbols_num=int(input("dear user enter the number of symbols you wnt in the password"))
numbers_num=int(input("dear user enter the number of numbers you wnt in the password"))
password=""

for i in range(1,letter_num+1):
    char= random.choice(letters)
    password = password+char
    for i in range(1,symbols_num+1):
        char=random.choice(symbols)
        password=password+char
        for i in range(1,numbers_num+1):
            char=random.choice(numbers)
            password=password+char


print(password)



# we can even easily shuffle this list quite easy


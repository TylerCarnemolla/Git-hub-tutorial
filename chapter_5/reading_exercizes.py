cars=["audi","bmw","chevy","ford","dodge","mercades"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

I=5
if I == 5:
    print("\nyes")
else:
    print("no")

answer=42
if answer != 42:
    print("that is not the right answer")
if answer == 42:
    print("correct")


cars=["audi","bmw","chevy","ford","dodge","mercades"]
if "audi" in cars:
    print("yes")
if car in cars != "lambo":
    print("that car is not here")

#exercizes
car="subaru"
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n Is car == 'audi'? I predict false.")
print(car=='audi')

list= ['1','2','3','4','5']
print("is 6 in list? i think it is")
if "6" in list:
    print("yes")
else:
    print("6 is missing")

cakes=["vanilla","chocoalte","yellow","fruit","german chocolate"]
for cake in cakes:
    if "velvet" in cakes:
        print("yes")
    else:
        print("no velvet here")
    
print("\n What is the best country?")
list=["USA","germany","sweeden","mexico","australia","england"]
for country in list:
    if "USA" in list:
        print("USA")
    else:
        print("not that country")

answer=45
if answer != 42:
    print("the real answer is 42")
elif answer ==42:
    print("that is correct")

guests=["allan","doug","robert","james","felix"]
if "kenny" in guests:
    print("kenny is here")
else:
    print("kenny is not here")

user="alex"
if user not in guests:
    print("thank god alex isnt here")

#ch5-3 exercizes
alien_color=["green"]
if "green" in alien_color:
    print("you earn 5 points")
if "red" in alien_color:
    print("you recieve zero points")
if "yellow" in alien_color:
    print("you recieve zero points")
print("nice try")

car=["dodge"] #write one thats wrong
if "ford" in car:
    print("its a ford")
if "ram" in car:
    print("its a ram")
if "audi" in car:
    print("its an audi")
else:
    print("its a dodge")

car=["lambo"]#write on thats right
if "ram" in car:
    print("wrong")
if "pontiac" in car:
    print("wrong")
if "chevy" in car:
    print("wrong")
if "lambo" in car:
    print("correct")

alien= "orange"
if "orange" in alien:
    print("correct")
    print("you earn 5 points")
else:
    print("try again")

fish=["salmon"]
if "trout" in fish:
    print("one point")
if "tuna" in fish:
    print("one point")
else:
    print("no point")

car="red"
if "red" in car:
    print("10pts")
if "black" in car:
    print("no points")
if "silver" in car:
    print("no points")
print("the correct color is " + car + ".")

age=27
if age < 2:
    print("your just a baby")
if age < 4:
    print("you ae a toddler")
if age < 13:
    print("you are a kid")
if age < 20:
    print("you are a teenager")
if age < 65:
    print("you are an adult")
if age > 65:
    print("you are a senior")

requested_acts=["chris stapleton", "zach bryan","metallica"]
for requested_act in requested_acts:
    if "zach bryan" in requested_act:
        print("sorry ZB cannot attend")
    else:
        print(requested_act +" will be included")
print("this is going to be a killer concert")

cars=["dodge","audi"] #checking if there are items in a list
if cars:
    for car in cars:
        print(car)
else:
    print("sorry no cars here")

    #using two lists in a loop
available_foods=["beef","chicken","rice","beans","nuts", "bread"]
requested_foods=["rice","bread","salmon","pineapple","nuts"]
for requested_food in requested_foods:
    if requested_food in available_foods:
        print(requested_food + " shall be served")
    else:
        print("soory we do not have " + requested_food + "in stock.")

usernames=["tyer_admin","alex_admin","rachel_admin","emma_admin","amber_admin", "eric","jezza", "richard"]
for username in usernames:
    if "admin" in username:
        print("Hello "+ username +", here is a status report since your last login")
    else:
        print("hello "+ username+ ", since you are not important to us, here is your ordinary persons dashboard")

employees=[] #check if there are people in this list

if employees:
        print("thank you for coming in to work on time")
else:
        print("nobody showed up")
    
current_users=["tod567","loony94","lennybruce","joeybeans53","bellyrock09"]
new_users=["loony94","tomdyln","jessieandrew","joeybeans53","jbrockface99"]
for new_user in new_users:
    if new_user in current_users:
        print(new_user + ", please pick a new user name")
    else:
        print("this name is available")

numbers=["1","2","3","4","5","6","7","8","9"]
for number in numbers:
    if number == "1":
        print(number + "st")
    elif number == "2":
        print(number +"nd")
    elif number =="3":
        print(number + "rd")
    else:
        print(number + "th")
print(number)

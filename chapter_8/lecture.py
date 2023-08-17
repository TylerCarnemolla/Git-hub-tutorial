cars=["audi", "bmw", "porche", "mercades", "mini",]
cars.append("volkswagen")
cars.append("ferarri")
cars.append("jaguar")
print(cars)

#append is a finction... but how do we make our own function?
#(def) is the syntax to tell python that we are making a function
#functions always have perenthasis (). A colon : says that the function is about to begin

def car_adder():
    cars.append("car") #if we run it now nothing will happen because function isnt "on"
    #we just made the funtion

car_adder()
print(cars) #this time it worked. It added "car" to the list

#this will add "car" every time we run it though because we put a "string" in the parenthasis
#what if we want to put anything in the car adder? We simply dont put a string in there

food=["taco", "burger","begal","ramen"]
def food_adder(food_addition):
    food.append(food_addition)
food_adder("bowl")
food_adder("sub")

print(food)

food_adder("turkey")
print(food)

#you cam complicate it by puting "if" statements and "while" statemtns withint it

drinks=["coffee", "booze", "water", "gatorade"]
not_allowed_drinks=["sweet cocktails","milk", "OJ", "tea"]

def drink_mix(add_drink):
    if add_drink in not_allowed_drinks: #if the user inputs somthing from the forbidden list,
        print("this drink is not allowed") #it will be filtered out
    else:
        drinks.append(add_drink) #everything else will be added to the drink list
    
drink_mix("lemonade")
drink_mix("milk")
drink_mix("white claw")
print(drinks)
print(not_allowed_drinks)


#what about returns??? returns allows us to use the data that our function makes.

def addtwo(num):
    return num + 2 #return tells python that we want an output
print(addtwo(6))

def addten(num):
    return num + 10
#                           you can stack funtions on functions and returns on returns
print(addten(addtwo(7)))

def nameprinter(first, middle, last):
    return f"my name is {first} {middle} {last}. "
print(nameprinter("Tyler", "joseph", "carenmolla"))
print(nameprinter("donald", "angelico", "trump"))


def shopping(thing_to_add):
    shopping_list=["drinks","ice","bags","food",]
    shopping_list.append(thing_to_add)
    return shopping_list

print(shopping('soap'))


#making a function for a dictionary

def sportsteams(teams_to_add):
    teamsdict={
        "football": ["9ers", "jets", "dolphins", "packers"],
        "baseball":["marlins", "redsox", "rockies"],
        "basketball":["lakers"]
    }
    teamsdict["nascar"]= teams_to_add
    return teamsdict
print(sportsteams(["bass pro", "mobile1", "lowes"]))

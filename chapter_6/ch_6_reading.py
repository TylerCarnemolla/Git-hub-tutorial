#dictionariest
car={"color": ["grey", "red", "silver", "tan", "blue"],
    "types":["hypercar","trucks","economy car","suv","sports cars"]
 }

print(car["color"]) #basic dictionary, one dict: one key: one list for value.
print(car["types"])
print(car["types"][3])

favorite_car=car["types"][1] + " " + car["color"][2]
print (favorite_car)

#adding keys
car["size"]=["compact","mid-sized","large",]
print(car)

#dictionaries dont need to be lists
truck={
    1:"chevy",
    2:"ford",
    3:"ram",
    4:"gmc",
    5:"toyota",
    6:"nissan"
}

#replacing a value
truck[5]="jeep"
print(truck)

#sometimes its helpful to start with an empty dictionary
dodge={}
dodge["charger"]="sedan"
dodge["journy"]="van"
dodge["durango"]="SUV"
dodge["challenger"]="coupe"
print(dodge)

#replacing a value
dodge["challenger"]="fast"
print(dodge["challenger"])


#run a loop
for key, value in dodge.items():
    print(key, value)

alien={'xposition': 0, 'yposition': 25, 'speed': 'medium'} #we give the speed
print("original x-position" + " " + str(alien['xposition']))
if alien["speed"]== "slow": # we check to see if this is the speed, no
    x_incriment = 1
elif alien["speed"]=="medium":#we check to see if this is the speed, yes
    x_increment = 2
else:
    x_increment = 3        

alien["xposition"] = alien["xposition"] + x_increment #original postion is added to 
                                                        #the increment of the test that passed
print("New x_position: " + str(alien["xposition"]))

#6-1 exercize
Jessica ={
    "last name": "Brown",
    "age": str("27"),
    "city": "Bend, Oregon",
    "status": "unmarried",

}
for key, value in Jessica.items():
    print(key, value)

favorite_numbers ={
    "jarred": "15",
    "kenny": "99",
    "mom": "719",
    "jessica": "7",
}
for key, value in favorite_numbers.items():
    print(key, value)

vocab={
    "\n sold:":"the food has been ran to the table",
    "\n in hand:":"the product being asked for is near completion",
    "\n building:": "the situation is building",
    "\n eight-top:": "a party of eight",
    "\n 86,ed:": "we do not have this item",
}
for key, value in vocab.items():
    print(key, value)

for phrase, meaning in vocab.items():
    print(phrase)

for phrase, meaning in vocab.items():
    print(meaning)

foods={
    "italian": "pasta",
    "american": "bbq",
    "asian": "sushi",
    "mexican": "tacos",

}

favorite_food= ["italian", "american"]
for kind in foods.keys():
    print("\n" +kind.title())
    if kind in favorite_food:
        print("my favorite foods tend to be " + kind)


for kind in foods.keys():
    if kind in favorite_food:
        print("i love " + kind.title())

for kind, dishes in foods.items(): #another way of doing the same thing
    if kind in favorite_food:
        print(kind)
        
if "irish" not in foods.keys():
    print("irish food is not included because it isnt any good")

vocab={
    "\n sold:":"the food has been ran to the table",
    "\n in hand:":"the product being asked for is near completion",
    "\n building:": "the situation is building",
    "\n eight-top:": "a party of eight",
    "\n 86,ed:": "we do not have this item",
}
for term, meaning in vocab.items():
    print(term, meaning)

for term in vocab.keys():
    print(term)
for meaning in vocab.values():
    print(meaning)

#creating dictionaries within lists
ducks=[] #crate an empty list
for duck_number in range(30):#create 30 ducks with attributes
    new_duck={'color': 'green', 'sound':'quack', 'speed':'fast',}
    ducks.append(new_duck) #add 30 ducks to list
for duck in ducks[:5]:
    print(duck)

print("there are " + str(len(ducks)) + " ducks headed right for us!") #prove how many ducks there are

#lets modify our list of dictionaries
for duck in ducks[0:3]:
    if duck['color']== 'green':
        duck['color']= "yellow"
        duck['speed']= "slow"
        duck['sound']= 'squack'

for duck in ducks:
    print(duck)
# name= input("Hello! What is your name?")

# prompt = "if you tell us about yourself we can find the right career for you."
# prompt += "\nwhat are your intrests?"
# question= input(prompt)

# prompt2 = "you responded by saying " + "'" + question + "'" +" what about" + question + " do you like?"
# print(prompt2)

# height= input("tell us your height in feet.")
# height=int(height)
# if height >= 4:
#     print("congrats! you are not a midget!")
# else:
#     print("im sorry but you are unfortunatly a midget")

# #usung modulos 
# #it only produces the remainder of a division equasion
# # 4%2 = 0  13%7 = 6
# number= input("tell me a number and i will tell you if it is even or odd.")
# number=int(number)
# if number % 2 == 0:
#     print(str(number) + "is even!")
# else: 
#     print("this number is odd")

# ####7-1 exercizes
# rental_car_prompt = "we only have subaru imprezas and toyota camrys"
# rental_car_prompt += "\nwhich would you like? "
# rental_car= input(rental_car_prompt)
# if rental_car == "camry":
#     print("sorry we dont have that.")
# elif rental_car == "impreza":
#     print("sorry we do not have that")
# else:
#     print("sorry we dont have that car")

# #while loops
# prompt= "\n tell me anything and i will repeat it back to you."
# prompt += "\n to stop the program, enter 'quit'."

# message =""
# while message != 'quite':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)
#     if message == 'quit':
#         break

# #7-4 exersize

# stuff= []
# flag=True
# while flag:
#     toppings= input("what toppings whould you like? :")
#     if toppings== 'quit':
#         flag=False
#     else:
#         print(toppings)


# age= input("please tell us your age to find your price")
# age = int(age)
# if age < 3:
#     print("your ticket is free!")
# elif age < 12:
#     print("your ticket is $10")
# elif age > 12:
#     print("your ticket costs $15."

#practice moving items from one list to another using a WHILE loop. 

#start a list of new hires and an empty list of trained hired
new_hires=["rex","ally","sami"]
trained_hires=[]

#after new hires are trained, move them to the trained hires list using a while loop
while new_hires: #while this list has things in it...
    current_employees = new_hires.pop() #we just made a third list and made it full of popped items from new hires

    print("we are training " + current_employees.title()) #this represents the training phase.
    trained_hires.append(current_employees) #move items from current employees to trained hires

print("the following employees have been trained")
for trained_hire in trained_hires:
    print(trained_hire.title())

#you can also remove things from a list using a while loop because it removes all instances of that value
names=["ron", "kenny", "tyty", "ron", "cassidy", "andrew"]
while "ron" in names:#as long as ron is in there, delete it.
    names.remove("ron")
print(names)

## filling a dictionary using a while loop
data={}#make a empty dictionary
flag = True
while flag:
    name= input("what is your name? :")
    opinion= input("who will you vote for this next election? :")

    data[name]=opinion
    
    repeat= input("would you like to test another subject? :")
    if repeat == 'no':
        flag = False
print("\nthe polling results show...")
for name, opinion in data.items():
    print(name +" will vote for "+ opinion + " this voting season.")


#one more try at moving things from one list to another.
types=["grinder", "ham", "turkey", "pb&j", "salami", "italian sub", "pastrami", "pastrami","pastrami"]
made_sandwiches=[]
if "pastrami" in types:
    print("\nsorry we have run out of pastrami.")
while "pastrami" in types:
    types.remove("pastrami")
while types:
    making=types.pop()
    print("\nwe are making " + making.title() + " sandwiches")
    made_sandwiches.append(making)

for sandwich in made_sandwiches:
    print("\nhere is your " + sandwich+ " sandwich")


#one more go at adding things to a dictionary with a while loop
polling= True
dream_car={}

while polling:

    demo =input("what kind of person are you? :")
    car=input("what is your dream vehicle? :")

    dream_car[demo]=car
    repeat=input("\nwould you like to test another sample?")
    if repeat == 'no':
        polling = False

print("Here are the polling results.")
for demo, car in dream_car.items():
    print("\n" + demo + " said that a " + car + " is their dream car." )
#intro to looping
cars=["audi","chevy","dodge","BMW","ram"]
for brands in cars:
    print(brands)
for brands in cars:   
    print(brands.title()+ " , is a great car manufacturer.")
    print("one day I would like to own a " + brands.title() + "\n")

donuts=["glazed","old fashoned","maple"]
for donut in donuts:
    print( "my favorite kind of donut is a " + donut + ".")
    print( "to bad donuts are terrible for you.""\n")


#numerical looping
#range finction
for value in range(1,5):
    print(value)
#only prints 1-4, stops AT 5.

#list function. Almost like range finction
numbers=list(range(1,9))
print(numbers)
#no need to indent here.

#skip numbers
#even numbers 1-10:
even_numbers=list(range(2,14,4))
print(even_numbers)
#starts at 2, ends at 14, jumps every 4 numbers

#math with lists
squares=[] #need an empty list
for value in range (1,11): #set up the range
    square=value**2 #identify our list items are range numbers to the power of 2
    squares.append(square) #list items are to be added to by the range value to the 2nd power
print(squares)#print once empty list

#list comprehensions
#takes the 4 lines of code to do the above equation and distills it down to one code
result=[number**2 for number in range(1,11)]
print(result)

#excersizes#

for value in range(1,21):
    print(value)
ducks=list(range(1,101))
print(ducks)
print(min(ducks))
print(max(ducks))
print(sum(ducks))

beavers=list(range(1,21,2))
print(beavers)

#make a list of multiples of 3 from 3-30
multiples=[]
for value in range(3,31):
    multiple=value*3
    multiples.append(multiple)
print(multiples)

#list comprehention version
multiples=[value*3 for value in range (3,31)]
print(multiples)

#make a list of cubes for 1-10 (number to the third power)
cubes=[otter**3 for otter in range (1,11)]
print(cubes)

#slicing
order=[1,2,3,4,5,6,7,8,9,10]
print(order[1:8])#full slices
print(order[0:6])

print(order[:8])#missing slices
print(order[5:])

print(order[-7:])#negative slices
print(order[:-6])

#looping with a slice
players=["dylan","exander","levit","jocko","donly","tefton","lewiston","franklin"]
print("here are the first five players")
for player in players[:5]:

    print(player)

#copying a list and adding to it
enemies_players=players [:]#this simple makes the list from the first to the last
print(enemies_players)

enemies_players.append("douglas") #you can only append one thing at a time.
print(enemies_players)
print(players)

#exercizes
birds=["duck","chicken","goose","crane","hawk","falcon","raven","woodpecker","gull"]
print("the first three birds are")
for bird in birds[0:3]:
    print(bird) 
print("\n")
print("the middle three birds are")
for bird in birds[4:7]:
    print(bird)
print("\n")

print("the final birds are")
for bird in birds[7:9]:
    print(bird)

#tuples are unchangable lists using (parenthesis ) rather than [square brackets]
animals=("dog","cat","bird","lion","whale","rat")
for animal in animals:
    print(animal)


print("modified animals")
animals=("dog","cat","alligator","lion","whale","rat")
print(animals)



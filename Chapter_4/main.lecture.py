x=12
if x>10:
    print("x is big")
    #if thing is true, then it does some stuff
elif x == 12:
    print("x is 12")
else:
    print("x is tiny")

#list slicing
mylist=["coffee","beer","wine","tea","water","booze"]

print(mylist[0:-1])

#start,stop,step: == start at this one: dont go past this one: move by this many
print(mylist[0:4:2])

#print statements
print(f'My favorite drinks are {mylist[0]} and {mylist[5]}.')
myage=27
print(f'My name is Tyler Carnemolla and I am {myage} years old. My favorite drink is {mylist[0]}.')
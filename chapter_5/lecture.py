#Loop work



mylist=["apple","banana","orange","spinach","kale","pneapple","guava"]

letter_to_look_for= "o"
for item in mylist:
    if item[0] == letter_to_look_for:
        print("i found it!" + item)
    else:
        print("that letter was not found...")

##### NEW TEST
list_length = len(mylist)

for i in range(list_length):
    print(i)

#or!

for i in range(len(mylist)):
    print(mylist[i])

#playing with loops
mylist=["apple","banana","orange","spinach","kale","pneapple","guava"]

urgent_groceries=[]

for item in mylist:
    if item[0] in ["a","b","c"]: #if an item in my list has a first letter IN this list
        urgent_groceries.append(item) #add to urgent list
    else: #if it doesnt have a first letter in that list
        continue #default keep running
print(urgent_groceries)

#when we print, it should only produce word within out list that have first letters abc

#or you can make it more consice

select_items=[item for item in mylist if item[0] in ["a","b","c"]] #get the items, of the items, in my list, 
                                                            #that have these letters in the [0]index
print(select_items)                                                            

number = 8

if number <= 8:
    print("number is greater than 8")
else:
    print("number is less than 8")
x=5
print("a spoon ")


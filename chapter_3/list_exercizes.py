names_list=["jessica","ty","kaitlyn","JP","kenny","Kingsley"]
print(names_list)
print(names_list[0])
print(names_list[4])
#excersize inputting list items
message="Why are you in my room " + names_list[1] + "?"
print(message)
message="Why are you in my room " + names_list[3] + "?"
print(message)
#changing elements from a list
bikes=["yamaha","honda","kawasaki","ktm"]
print(bikes)
bikes[0]="indian"
print(bikes)

#adding elements to a list
#append
print(bikes)
bikes.append("ducati")
print(bikes)

 #inserting
bikes=["ktm","yamaha","honda","suzuki"]
print(bikes)
bikes.insert(2, "ducati")
print(bikes)

#removing
#del
car_list=["honda","subaru","toyota", "nissan"]
print(car_list)
del car_list[2]
print(car_list)

#pop method
tools=["hammer","chissel","wrench","plyer","saw"]
print(tools)
popped_tool=tools.pop()
print(tools)
print(popped_tool)
del popped_tool
popped_tool=tools.pop(1)
print(tools)
print(popped_tool)

#removing by value
tools.append(popped_tool)
print(tools)
tools.remove("hammer")
print(tools)

#guest invite exercize
guests=["sarah","emily","miranda"]
message="hey "+ guests[0]+"!"+" would you want to come over tonight?"
print(message)
message="hey "+ guests[1]+"!"+" would you want to come over tonight?"
print(message)
message="hey "+ guests[2]+"!"+" would you want to come over tonight?"
print(message)
cantmakeit="hey ty, i cannot come over tonight because I have to work.-emily"
print(cantmakeit)
guests.pop(1)
print(guests)
guests.append("Kenzie")
print(guests)
message="hey "+ guests[2]+"!"+" would you want to come over tonight?"
print(message)
guests.insert(0,"sami")
guests.insert(1,"hannah")
guests.insert(2,"jessica")
print(guests)
new_message="hey " + guests[0]+ ","+"I found a bigger table so you are all invited!"
print(new_message)
new_message="hey " + guests[1]+ ","+"I found a bigger table so you are all invited!"
print(new_message)
new_message="hey " + guests[2]+ ","+"I found a bigger table so you are all invited!"
print(new_message)
new_message="hey " + guests[3]+ ","+"I found a bigger table so you are all invited!"
print(new_message)
new_message="hey " + guests[4]+ ","+"I found a bigger table so you are all invited!"
print(new_message)
new_message="hey " + guests[5]+ ","+"I found a bigger table so you are all invited!"
print(new_message)

#sorting
cars=["bmw","audi", "honda","chevy"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)

#list length (len)
cars=["audi","bmw","dodge","ford","fararri","land rover"]
print(len(cars))


#list exercize
hotspots=["iceland","norway","australia","greece","capri"]
print(hotspots)
print(sorted(hotspots))
print(hotspots)
hotspots.sort(reverse=True)
print(hotspots)
print(hotspots)
hotspots.sort(reverse=False)
print(hotspots)
hotspots.sort(reverse=True)
print(hotspots)
print(len(guests))
y=6
message= "Hello everyone, since I accidentaly invited " + str(y) + " people to many, sadly I have to resind a couple invitations. My bad."
print(message)
print(hotspots[-1])
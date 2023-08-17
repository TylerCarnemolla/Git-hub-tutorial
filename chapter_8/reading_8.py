def display_meaage():
    print("we are learning baout functions")

display_meaage()

def favorite_food(fav_food):
    foods=["taco", "burger", "steak"]
    foods.append(fav_food)
    print("hello!, my favoite food is "+ fav_food)

favorite_food("muffins")

def fav_book(title):
    print("my favorite book is " + title)

fav_book("jackson")

#8-3 excersize

#positional arguments
def tshirt(shirt_size, shirt_print):
    print("I need a " + shirt_size + " shirt with " + shirt_print + " printed on the front.")

tshirt('large', "bula bula")

#keyword argument
def shoes(size= '12', brand = 'vans'):
    print("i need a size " + size + " pair of " + brand + ".")

shoes()

#default argument
def custom_shirt(logo, size = 'large'):
    print("I need a shirt thats size " + size + " and I need " + logo + " on the front.")
custom_shirt('bula bula')

def tanks(size, message= 'bula bula'):
    print(size, message)
tanks("large")
tanks('medium')

def city_country(city_name, country = 'United States'):
    print(city_name, country)
city_country('dallas')
city_country('Newport')
city_country('Berlin', 'Germany')

#maiking an optional argument
def three_names(first, last, middle = ""):
    if middle:
        fullname= first + " " + middle + " " + last
    else:
        fullname = first + " " + last
    return fullname.title()
user53 = three_names('tyler', 'carnemolla', 'joseph')
print(user53)

user53 =three_names('tyler', 'carenmolla')
print(user53)

#return a dictionary

def viking(title, name, age):
    character = {'identifier': title, 'person': name, 'age': age, }
    return character
cast = viking('king', 'ragnar', '29')
print(cast)

cast2=viking('leader', 'tyler', '27')
print(cast2)

#8-9 excersize

bandmembers =['lars', 'james', 'rob', 'kirk']
def showmembers(bandmembers):
    for member in bandmembers:
        print(member)
showmembers(bandmembers)

def rocks(bandmembers):
    for member in bandmembers:
        print(member + " rocks")
    
rocks(bandmembers)

#8-12 exercizes

def sandwich(*fillings):
    print("we will build you a sandwich with: ")
    for filling in fillings:
        print("- " + (filling))

sandwich('olives', 'vinager', 'salami', 'lettuce', 'tomato')

#create a profile for sombody where you know some of the info they will provide but not all of it.
def crate_profile(first, last, age, sex, **user_info):
    profile={}
    profile['first_name']= first
    profile['last_name']= last
    profile['age']= age
    profile['gender']= sex
    for key, value in user_info.items():
        profile[key]= value
    return profile
tyler = crate_profile('tyler', 'carenmolla', str('27'), 'male', location = 'USA', occupation= 'agent')
print(tyler)
print(tyler['location'])

def car(maker, model, **more_info):
    details={}
    details['manufacturer']= maker
    details['type']= model
    for key, value in more_info.items():
        details[key]= value
    return details

ram= car('ram', '1500', color='silver', tires='big', interior='dirty')
print(ram)


#dictionary
my_dict={
    #key:value
    1:"mazda",
    2:"nissan",
    3:"chevy",
    4:"volvo",
    5:"dodge",
    9:"jeep",
    15:"ford",

}
print(my_dict[9])
print(my_dict)

my_dict["new key"]= "mini"
print(my_dict)
my_dict[2]="BMW"

del my_dict[1]
print(my_dict)

for key, value in my_dict.items():
    print(f"the key is {key}")
    print(f"and this is the value: {value}")

for key in my_dict:
    print(key)

for key, value in my_dict.items(): #must write .item(s)
    print(value)

for value in my_dict.values(): #must write .value(s) ()
    print(value)

#dictionaries in dictionaries in dictionaries
dict1={
    "metallica":["master", "lightning", "72 seasons","sandman"], #one key one value
    "cont_metal": {"avenge": "natural born killer"}, #key :key: value
    "thrash": {"mega":["symphony","peace","sweating"], #key : key : key :key
               "pantera": ["cowboys", "walk", "gates"],
               1:3}

    }

print(dict1["metallica"][2])
print(dict1["thrash"]["pantera"][1])
print(dict1["thrash"][1])
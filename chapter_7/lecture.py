myinput= input("what is your input?")
print(myinput)
print(input)

G = 99
    #
#while True:
    #print(G)
   #G += 1 
   # 
   # #this will go indefinatly unless manually stopped

#while G < 2000:
    #print(G)
    #G +=3
# this will run, starting at 99 and goint up by 3 at a time untill it hits 2000

#while True:
    #G += 1
    #if G >2000:
        #break
        #another way of doing the same thing. once the numbers hit 2000 it breaks the loopwhile True:
while True:
    myname= input ("what is your name? \n")
    if myname.lower== 'quit':
        break
    elif myname.lower()[0] in 'abcdefg':
        print("\nplease go to line one.")
    elif myname.lower()[0] in 'hijklmnop':
        print('\nplease go to line two.')
    elif myname.lower()[0] in 'qrstuvwxyz':
        print('\nplease fo to gate three.')

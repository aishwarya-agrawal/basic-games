import time
print("Welcome new user")
word = "secret"
new = list()
guess =''
chances = 0
length = 0
while chances<10 :
    if len(new)== len(word):
        break
    guess = input("Enter a character : ")
    if guess in word:
        index = [i for i,x in enumerate(word) if x==guess]
        for j in index:
            new.insert(j,guess)
            length = length+1
        chances=chances+1
        for i in new:
                       if i == None:
                           print("_ ",end="")
                       else:
                           print(i," ",end="")
                       
        
    else:
                       chances = chances+1
        

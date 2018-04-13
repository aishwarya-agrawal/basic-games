import random
guess= 0
a = random.randint(0,99)
while(guess < 5):
    user = int(input("guess the number"))
    if(user < 0):
        print("guess number too low")
    else:
        if(user > 99):
            print("guess number too high")
        else:
            if(user == a):
                break
            else:
                guess = guess + 1
print("correct no is : ",a)
print("you took :",guess," guesses still the correct wrong")

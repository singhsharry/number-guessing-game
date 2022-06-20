# Number guessing game


from pickle import TRUE
from re import S

n=12
b=15
print("rules:, \n 1. numbers from 0 to 15  \n 2.  Guess the number")
print("Lets Start The Game")
print("Enter your number")
 
user= int(input())


while(TRUE) :
      
    if user>b :
        print("ERROR")
        user= int(input("Guess only between 1 to 15!"))
        continue
    elif  user<n:
        print("Increase your number")
        print("Retry:(")
        user= int(input("Guess Again:"))
        
        continue
    elif user>n:
        print("Decrease your number")
        print("Retry:(")
        user= int(input("Guess Again:"))
      
        continue
    elif user==n:
        print("That's Correct!")
        print("You win")
        break

    


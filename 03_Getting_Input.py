# Ask the user for their name
from time import sleep
from turtle import delay


print()
username = input("What is your name? ")

# Ask the user for their favourite integer
fav_num = int(input("Favourite Number? "))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
sleep(1.75)
# Output the results of doubling, halving 
# and squaring their favourite number

print("double {} is {}".format(fav_num, double))
sleep(1.75)
print("half {} is {}".format(fav_num, half))
sleep(1.75)
print("{} squared is {}".format(fav_num, square))
print()
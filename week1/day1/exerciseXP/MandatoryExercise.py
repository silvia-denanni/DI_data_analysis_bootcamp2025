# 1
print('hello world')

# 2
print((99^3)*8)

# 3
print(15 < 8) #False
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3) #False -- actually not supported
print("Hello" == "hello") #False -- actually not supported

#4
computer_brand = "HP"
print(f"I have a {computer_brand} computer.")

#5
name = "Silvia"
age = "37"
shoe_size = "36"
info =f"My name is {name}, I am {age} years old, my shoe size is {shoe_size} and I was born on April 1st"
print(info)

#6
a = 3
b = 4
if a > b:
    print("Hello World")

#7
number = int(input("Enter your number:"))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

#8
user_name = input("What is your name? ")
my_name = "Silvia"
if user_name == my_name:
    print("Twinsies!")
else:
    print("Your name is not as cool as I thought it was gonna be...")

#9
your_height = int(input("Enter your height in cms: "))
if your_height > 145:
    print("You are tall enough to ride this ride")
else:
    print("You have some more growing to do, shortie...")

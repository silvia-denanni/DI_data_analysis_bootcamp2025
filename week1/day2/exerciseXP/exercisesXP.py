#1 Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
my_fav_numbers = set()
my_fav_numbers = {1,3,5,13} 
my_fav_numbers.add (1991)
my_fav_numbers.add (11)
print(my_fav_numbers)
my_fav_numbers.remove(11)
print(my_fav_numbers)

friend_fav_numbers = set()
friend_fav_numbers = {15,23,44,8}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

#2
#Given a tuple of integers, try to add more integers to the tuple. --> Tuples are immutable, meaning they cannot be changed after creation. 

#3 
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.insert(2,"Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
count_of_apples = basket.count("Apples")
print(count_of_apples)
basket.clear()
print(basket)

#4
# Recap: What is a float? What’s the difference between a float and an integer? A float is a numerical value that is not an integer, meaning that it features a decimal value, e.g. 3.4
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

sequence = []
start = 1,5
end = 5
step = 0.5

current = start
while current <= end:
    if current.is_integer():
        sequence.append(int(sequence)) # sequence.append(int(current)) converts values like 2.0 to 2 before storing.

    else:
        sequence.append(current)
    current += step #moves to the next value for the next loop run
    
print(sequence)


#5
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range (1,21):
    print(i)

for i in range (0, 21, 2):
    print(i)

#6
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
while True:
    ask_user_name = input("Enter your username: ")
    if len(ask_user_name) >=3 and not ask_user_name.isdigit():
        print("thank you")
        break
    else:
        print("try again")

#7
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new one! I hope you like it!"
ask_fav_fruit = input("Enter your favorite fruit: ")
user_list = list(ask_fav_fruit)
ask_any_fruit = input("Give me a fruit: ")
if ask_any_fruit in ask_fav_fruit:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new one! I hope you like it!")

#8
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
base_price = 10
topping_price = 2.50
toppings = []

while True:
    topping = input("Enter your pizza toppings(type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

total_cost = base_price + topping_price * len(toppings)

print("Your pizza toppings are:")
for t in toppings:
    print(f"{t}")
print(f"Total cost of your pizza is: ${total_cost:.2f}")

#9
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
total_cost = 0

while True:
    age_input = input("Enter the age of your family member (type 'done' to finish): ")
    if age_input.lower() == 'done':
        break

    if not age_input.isdigit():
        print("Please enter a valid age.")
        continue

    age = int(age_input)

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"Total ticket cost for the family is: ${total_cost}")
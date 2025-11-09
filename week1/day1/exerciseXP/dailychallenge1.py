user_string =(input("Please enter a 10 character long string: "))
if len(user_string) < 10:
    print("Please enter a longer string.")
elif len(user_string) > 10:
    print("Please enter a shorter string.")
else:
    print(f"Your string is such a 10! The first character is {user_string[0]} and the last character is {user_string[9]}")
for i in range(1, len(user_string) + 1): #RANGE FUNCTION: range(len(user_string) + 1) --> it becomes 11 (10 +1). 
#Then, the range(1, 11) creates a sequence of counting numbers starting at 1 and going up to, but not including, 11.
#LOOP: for i in --> do the following step n times, and in each step, let the variable i be the next number in the
# count (1, 2, 3, etc.)
    print(user_string[:i]) #STRING SLICING: user_string[:i] --> user_string[start : end]; since 0 is not mandatory, i only
# indicates the end position
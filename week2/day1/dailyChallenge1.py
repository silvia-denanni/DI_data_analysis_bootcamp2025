#1 Instructions: Old MacDonald’s Farm
# Create a class called Farm.
# Implement the __init__ Method
# Implement the add_animal Method



class Farm():
    def __init__(self, name = "McDonald\'s"):
        self.name = name
        self.animals = {}       #empty dictionary
    
    def add_animal(self, animal_type, count = 1):
            if animal_type in self.animals:  
                self.animals[animal_type] += count   #
                print(f"The animal {animal_type} in already in the dictionary {count} times.")
            else:
                 self.animals[animal_type] = count
                 print(f"{animal_type} will be added to the dictionary and to the counter!")
    
    def get_info(self):  # self parameter means this method can access the object’s own data (like name and animals)
        farm_info = (f"This is {self.name} farm\n")
        for animal, count in self.animals.items():  #lets you get both the animal’s name (animal) and how many there are (count) for each entry
            farm_info += f"{animal} : {count}\n" # += means “add to the end of the existing string”, "\n" puts each animal in its own line
        farm_info += "E-I-E-I-0!"                # += means “add to the end of the existing string”
        return farm_info                         # Returns the complete string so that when you call get_info(),
                                                 # you get all the information as one nicely formatted text

farm = Farm("McDonald\'s")
#print(farm.name)
farm.add_animal("cow",5)
#print(farm.animals)
farm.add_animal("cow",5)
#print(farm.animals)
farm.add_animal("pig",3)
#print(farm.animals)
print(farm.get_info())
        


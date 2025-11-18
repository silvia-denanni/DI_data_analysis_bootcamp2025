#Daily Challenge - Circle: The goal is to create a class that represents a simple circle.
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"
    
    def circle_area(self, radius):
        calculate_area = (math.pi * (radius ** 2)) 
        return calculate_area
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented                           # special value used in __add__, __eq__, etc.to indicate that
                                                        # the operation is not implemented for the given operand types 
                                                        # When you write __add__ and the "other" object is not a type 
                                                        # your method knows how to handle -->you return "NotImplemented" 
                                            #NOT AN ERROR, it’s a signal to Python to try other ways to work it out
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.radius > other.radius:
               return self.radius > other.radius
            else:
                return self.radius < other.radius
            
        return NotImplemented
    
    def __lt__(self, other):             
        if isinstance(other, Circle):
            return self.radius < other.radius    # defines the behavior of the "<" operator between two Circle objects
        return NotImplemented                    # If "other" is not a Circle

circles = [Circle(5), Circle(2), Circle(9), Circle(1), Circle(7)]
circles.sort()                              # Python calls __lt__ to compare pairs of circles and sort them by radius

for c in circles:
    print(c)
 

c1 = Circle(5)
c2 = Circle(7)
c3 = c1 + c2  # creates a new Circle with radius 12

print(c3)  # >>> Circle with radius 12
print(c1 == c2)  # >>>False
print(c1 == 10)  # >>>False
print(c1 < c2)   # >>>True
print(c1 > c2)   # >>>False

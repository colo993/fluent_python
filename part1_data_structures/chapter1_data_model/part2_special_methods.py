# Example 1-2. A simple two-dimensional vector class
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Vector addition 
# The output is returned in user friendly version due to __repr__ implementation
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2

# Calculate the magnitude of a vector
v = Vector(3, 4)
abs(v)

# Multiplie magnitude
v * 3

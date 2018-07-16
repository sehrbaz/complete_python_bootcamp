# Object Oriented Programming Homework
# Problem 1
class Line(object):
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        dx = x2 - x1
        dy = y2 - y1
        return (dx**2 + dy**2)**0.5
    
    def slope(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        dx = x2 - x1
        dy = y2 - y1
        return dy / dx
        
# Problem 2
class Cylinder(object):
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.r = radius
        self.h = height
        
    def volume(self):
        return Cylinder.pi * (self.r**2) * self.h
    
    def surface_area(self):
        return (2 * Cylinder.pi * (self.r**2)) + (2 * Cylinder.pi * self.r * self.h)

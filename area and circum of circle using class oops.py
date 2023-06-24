class circle:
    pie=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pie*self.radius*self.radius
    def circum(self):
        return 2*circle.pie*self.radius
c=circle(7.5)
print("area=",c.area())
print("circumference=",c.circum())

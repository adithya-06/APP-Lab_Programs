#4
class Rectangle:
    def __init__(self,length=0,breadth=0):
        self.length=length
        if breadth==0:
            self.breadth=length
        else:
            self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)


c1=Rectangle()
c2=Rectangle(6)
c3=Rectangle(9,6)
c1.area()
c2.area()
c3.area()
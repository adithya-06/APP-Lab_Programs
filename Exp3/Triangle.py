#8
class Triangle:
    def __init__(self,a=3,b=4,c=5):
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        return self.a+self.b+self.c
    
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(1/2)


f=Triangle()
print(f.perimeter())
print(f.area())
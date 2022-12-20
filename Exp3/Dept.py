#3
class Dept:
    def __init__(self,name='SCO'):
        self.name=name
    def getName(self):
        print(self.name)

d1=Dept()
d2=Dept('CSE')
d1.getName()
d2.getName()
#5
class PrintDT:
    def python_data(self,str):
        self.str=''
        print(str)
    def python_data(self,list):
        self.list=[]
        print(list)
    def python_data(self,tuple):
        self.tuple=()
        print(tuple)



a=PrintDT()
a.python_data('123')
a.python_data([1,2,3,4])
a.python_data((1,2,3,4,5))
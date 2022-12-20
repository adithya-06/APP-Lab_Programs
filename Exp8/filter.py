#8
marks=[[100,80,60,20,35],[5,30,80,60,70],[70,90,80,60,70],[45,20,40,60,70],[90,90,90,70,80]]

def failed(a):
    return a<40
l=[]
for i in range(len(marks)):
    l.append((list(filter(failed,marks[i]))))

for i in range(len(l)):
    if len(l[i])>0:
        print(i+1)

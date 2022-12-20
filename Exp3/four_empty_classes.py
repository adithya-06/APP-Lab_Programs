#2
class CTECH:
    pass
class CINTEL:
    pass
class NWC:
    pass
class DBMS:
    pass

student1=CTECH()
roll_no1=CTECH()
name2=CINTEL()
marks2=CINTEL()
student2=NWC()
name2=NWC()
roll_n2=DBMS()
marks2=DBMS()

print(isinstance(student1,CTECH))
print(isinstance(student2,CINTEL))
print(isinstance(roll_no1,NWC))
print(isinstance(marks2,DBMS))
print('Subclass:')
print(issubclass(CTECH,object))
print(issubclass(CINTEL,object))
print(issubclass(NWC,object))
print(issubclass(DBMS,object))



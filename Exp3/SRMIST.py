#1
class SRMIST:
    school = 'SRMIST'
    dept1 = 'Computer Science'
    dept2 = 'Artificial Intelligence'
    dept3 = 'Mechanical Engineering'
    dept4 = 'Biotech'
print("Original attributes and their values of the Student class:")
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\nAfter adding the specialization, attributes and their values with the said class:")
SRMIST.specialization  = 'Blockchain'
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\nAfter removing the dept1,dept2 attributes and their values from the said class:")
del SRMIST.dept1
del SRMIST.dept2
#delattr(Student, 'student_name')
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

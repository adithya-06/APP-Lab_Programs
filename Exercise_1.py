#1
def divisible(a,b):
    l=[]
    for i in range(a,b+1):
        if i%40==0:
            l.append(i)
    return l


#2
from random import randint
x=randint(1,9)
print('Guess a number')
while(1):
    y=int(input())
    if x==y:
        print('Well guessed!')
        break
    else:
        print('Guess again')


#3
'''def pattern(a):
    for i in range(2,a+1):
        for jz in range(1,i):
            print('*',end='')
        print('')
    for i in range(1,a+1):
        for j in range(i,a+1):
            print('*',end='')
        print('')'''
def pattern(a):
    for i in range(1,2*a):
        for j in range(a-abs(i-a)):
            print('*',end='')
        print('')
    return


#4
def reverse_word(a):
    return a[::-1]


#5
def matrix_creation(a,b):
    matrix=[]
    for i in range(a):
        l=[]
        for j in range(b):
            l.append(i*j)
        matrix.append(l)
    return matrix


#6
def digits_letters(a):
    letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='1234567890'
    l_count,d_count=0,0
    for x in a:
        if x in letters:
            l_count+=1
        elif x in numbers:
            d_count+=1
    return l_count,d_count
    

#7
def password_validity(a):
    if len(a)>16 or len(a)<6:
        return False
    lower_letters='abcdefghijklmnopqrstuvwxyz'
    upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nos='1234567890'
    symbols='$#@'
    flag1,flag2,flag3,flag4=False,False,False,False
    for x in a:
        if x in lower_letters:
            flag1=True
        if x in upper_letters:
            flag2=True
        if x in nos:
            flag3=True
        if x in symbols:
            flag4=True
    if flag1 and flag2 and flag3 and flag4:
        return True
    return False


#8
def check_digits(x):
    while(x>0):
        if x%2!=0:
            return False
        x//=10
    return True
def even_digits(a,b):
    l=[]
    for i in range(a,b+1):
        if check_digits(i):
            l.append(i)
    return l


#9
def month_to_days(x):
    if x=='January' or 'March' or 'May' or 'July' or 'August' or 'October' or 'Decenber':
        return 'Number of days: 31'
    if x=='April' or 'June' or 'September' or 'November':
        return 'Number of days: 30'
    if x=='February':
        return 'Number of days: 29(Leap Year)  28(Non-Leap Year)'
    return 'Check Spelling'


#10
def sum_of_two_ints(a,b):
    if a+b>105 and a+b<200:
        return 200
    return a+b


#11
def num_pattern(a):
    for i in range(a,0,-1):
        for j in range(i,0,-1):
            print(i,end='')
        print('')
    return


#12
from pandas import read_excel as re
import matplotlib.pyplot as plt
df=re(r'D:\Assignments SRM\Semester 4\Advanced Programming Practice\Practical\Heights_Dataset.xlsx')
print(df)
plt.hist(df['Height(Inches)'],bins=100)
plt.show()


#13
def ret_true(a,b):
    if a==b:
        return True
    if a+b==5 or abs(a-b)==5:
        return True
    return False


#14
def distance_bw_points(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


#15
def all_different(l):
    for x in l:
        if l.count(x)>1:
            return False
    return True


#16
def number_of_each_char(a):
    d={}
    for x in a:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    return d


#17
def num_ops(a):
    x=str(a)
    s=0
    for i in x:
        s+=int(i)
    if a-s<1:
        return x
    return num_ops(a-s)

def num_ops(a):
    if a<10:
        return a
    return 9


#18
def digits_absent(a):
    n='0123456789'
    l=[]
    for x in n:
        if x not in a:
            l.append(x)
    return l


#19
def repeat_till_palindrome(a):
    while(1):
        s=a+int(str(a)[::-1])
        if str(s)==str(s)[::-1]:
            break
        else:
            a=s
    return s


#20
def complicated(l):
    print(len(l))
    print(l[2:])
    print(l[-3:])
    print(sum(l))
#1
def mirror(s):
    return s[::-1]


#2
def rotate(a,b):
    if a==b[::-1]:
        return True
    return False


#3
def binary_len(n):
    from random import randint as r
    a=''
    for i in range(n):
        a+=str(r(0,1))
    return a


#4
def remove_punctuation(a):
    letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_a=''
    for x in a:
        if x in letters:
            new_a+=x
    return new_a


#5
def tupple_addition(t1,t2,t3):
    return tuple(map(sum,zip(t1,t2,t3)))


#6
def remove_empty_tuples(l):
    for x in l:
        if not x:
            l.remove(x)
    return l


#7
def count_till_tuple(l):
    count=0
    for x in l:
        if type(x)==type(()):
            break
        count+=1
    return count


#8
def convert_matrix_list(l):
    a=[]
    for j in l:
        b=(j[0][0],j[0][1],j[1][0],j[1][0])
        a.append(b)
    return a


#11
def print_even(l):
    for x in l:
        if x%2==0:
            print(x,end=', ')

def main():
    l=map(int,input().split())
    return print_even(l)

#12
def is_palindrome(s):
    if s==s[::-1]:
        return True
    return False


#13
def isprime(a):
    flag=True
    for i in range(2,int((a**(1/2))+1)):
        if a%i==0:
            flag= False
            break
    return flag
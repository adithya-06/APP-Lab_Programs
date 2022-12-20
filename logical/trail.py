def is_prime(n):
    return n>1 and all(n%i for i in range(2,int(n**0.5)+1))

if is_prime(int(input('Enter a number: '))):
    print('It is a Prime number.')
else:
    print('It is not a prime number.')
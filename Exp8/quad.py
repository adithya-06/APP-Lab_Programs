def square(a):
    return a**2

def twice(function,x):
    return function(function(x))


quad=twice(square,3)
print(quad)
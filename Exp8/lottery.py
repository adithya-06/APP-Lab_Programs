import random
def out_fun(n):
    mylist = list(range(n))
    def inf_fun():
        print(random.choice(mylist))
    inf_fun()

out_fun(100)
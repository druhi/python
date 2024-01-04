
from calculate import add,sub,mul,div

choose = input("what calculation do you want to perform [add, sub, mul, div] ")
if choose == "add":
    add()
if choose == "sub":
    sub()
if choose == "mul":
    mul()
    if choose == "div":
        div() 

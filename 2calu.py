
# import sys
# sys.path.append(r"C:\Users\djukaria\Desktop\code")
from calu import add,sub,mul,div

def user_option():
    options = ["add","sub","mul","div"]
    ans = input("Please choose opertions from set : Add,Sub,Mul,Div : ").strip().lower()
    count = 1
    while ans not in options:
        print("Incorrect option choosen, Plese choose from Add,Sub,Mul,Div : ")
        ans = input("Please choose opertions from set : Add,Sub,Mul,Div : ")
        if count == 2:
            print("sorry, you gave the answer wrong 3 times, exiting") 
            break
        count += 1
    return ans
    

def main():
    ans = user_option()
    if ans == "add":
        try:
            add()
        except:
            TypeError 
            print("Value should be integer only")    
    elif ans == "sub":
        sub()
    elif ans == "mul":
        mul()
    elif ans == "div":
        try:
            div()
        except:
            ZeroDivisionError
            print("Divisor cannot be 0, please try with valid input")        
main()        

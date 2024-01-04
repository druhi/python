import re
def play():
    name = input("what is your name ").strip()
    email = input(f"what is your e-mail id, {name} ").strip()
    return email
def again(email):
    regex = r"^\w.+@(\w+\.\w+\.)?\w+\.(com|edu|in)$"
    if re.search(regex,email):
        print("thank you ,your email is valid")
        exit()
    else:
        print("oops try again")
        retry = "retry"
        return retry
        

def main():
    email = play()
    retry = again(email)
    if retry == "retry":
        counter =1
        while counter < 3:
            email = play()
            retry = again(email)
            counter += 1
    if counter > 3:
        print("exiting") 
        exit()       
            

if __name__ == '__main__':
    main()
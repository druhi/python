x =input("what is your hobby ")
y =input(""" how do you :
            well
            good
      very good """)
if y == "well":
    print("focus on your goal make it go well ☺")
    print("dont forget to achieve your goal ☺")
if y == "good":
    print("pratice to the tippy top ☺")
if y == "very good":
    print(f"happy to see you to do you hobby ,{x}")
    print("keep practicing")
words = "well","good","very good"
if y not in words:
    print("sorry,exiting")
    exit()
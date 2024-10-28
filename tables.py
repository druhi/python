try:
    x = int(input(" which number table do you want : "))
    y = int(input(" which number table do you want : "))
except:
      ValueError()
      print("Input should be only Integer, Exiting")
      exit()

for w in range(1,y+1):
        z = w*x
        print(f"{x}*{w}={z}")
        y=y+1
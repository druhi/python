num = 54321
n = str(num)
li = []
for j in n:
    li.append(j)

# list = ["1","2","3","4"]
x = len(li)
for i in range(x):
    print(li[x-1],end="")
    x = x -1
print()
##############################
n = 54321
num = n
reverse = 0
while(num!=0):
    digit = num%10
    reverse = reverse*10+ digit
    num=int(num/10)
print(f"reverse of {n} is {reverse}")

    





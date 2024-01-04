row = int(input("How many rows to print : "))
y = 1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(y, end=' ')
        y=y+1
    print()    


# row = int(input("How many rows to print : "))
# # y = 1
# for i in range(row, 0 , -1):
#     for j in range(0,i):
#         print('*', end=' ')
#         # y=y+1
#     print()    # you could do this to
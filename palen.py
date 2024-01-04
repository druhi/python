

def palindrom(word):
    for i in range(0,int(len(word)/2) ):
        if word[i] != word[len(word)-1-i]:
           return False
        else: 
           return True    
 

def main():
    word = input("give a word : ").strip()
    if palindrom(word) == True:
        print(f"{word} is a palindrom")
    else:
        print(f"{word} is not a palindrom")

main()



# word[0]  == word[4]
# word[1]  == word[4]
# # madam  5

# 0    4
# 1    3

# malayalam

# 0        8
# 1        7
# 2        6
# 3        5
# 4        4
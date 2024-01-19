num = int(input("Please enter a number"))
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num>1:
    for a in range(2,num):
        if num%a == 0:
            flag = True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")

n =int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if(i == j):
            print(j+1,end="  ")
        elif(j == n-i-1):
            print(j +1,end="  ")
        else:
            print("",end="  ")
    print()

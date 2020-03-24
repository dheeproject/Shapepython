l=int(input("Enter the number of rows of ladder"))
m=int(input("Enter the width of ladder"))
for i in range(1,l+1):
    if i%3==0:
        for j in range(1,m+1):
            print("*",end="")
        print("\n")
    else:
        for j in range(1,m+1):
            if j%(m-1)==1:
                print("*", end="")
            else:
                print(" ", end="")
        print("\n")
 

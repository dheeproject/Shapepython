#print this shape
#1
#22
#333
#4444
#55555
row=int(input("Enter the number of rows for which you want a shape like this"))
for i in range(1, row+1):
    for j in range(0,i):
        print(i,end="")
    print("\r")
    
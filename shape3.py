#printing a shape like this
"""
   *
  * *
 * * *
* * * *
"""
n=int(input("Enter the numberof rows "))#taking value from user
for i in range(1,n+1):
    cal=n-(i-1)
    count=0
    for j in range(1,n+n):
        if j>=cal and (j-cal)%2==0:#checking condition for printing shape at right place
            if (count<i):
                print("*", end="")
                count+=1
        else:
            print(" ", end="")
    print("\r")
        

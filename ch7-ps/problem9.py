# n = int(input())

# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if(i == (n-1) and j == (n-1)):
#             print(" ",end = " ")
#         else:
#             print("*",end = " ")
#     print()


n = int(input())

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end= "")
        print(" "* (n-2),end="")
        print("*", end = "")
    print("")
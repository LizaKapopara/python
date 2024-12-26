# n = int(input("enter number you want to print table for:"))

# for i in range(2, n):
#     if(n % i) == 0:
#         print("number is not prime.")
#         break
#     else:
#         print("number is prime.")

n = int(input("enter number:"))

for i in range(2, n+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i, end=" ")
            
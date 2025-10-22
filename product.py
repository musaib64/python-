n= int(input("Enter the number 1: "))
m= int(input("Enter the number 2: "))
def mul(a,b):
    if a==0 or b==0:
        return 0
    else :
        return a+mul(a,b-1)
print("The multiplication of two numbers is :",mul(n,m))
n=int(input("Enter a number: "))
def is_armstrong(num):
    sum = 0
    temp = num
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return sum == num

if is_armstrong(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
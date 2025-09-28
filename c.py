'''accumalation error '''
# a=0.1
# sum=0
# for i in range(10):
#     sum+=a
    

# print(sum)
'''rectifying the error'''
import math
a=0.1
sum=math.fsum([a]*10)
print(f'sum is: {sum}')


# table to print
# def table(n):
#     for i in range(1,10):
#         print(f"{n} * {i} = {n*i}")
# n=int(input("enter the number"))
# table(n)

'''decimal to binary conversion'''
# n = int(input("enter the number"))
# # s = ""
# # if n == 0:
# #     s = "0"
# # else:
# #     while n > 0:
# #         r = n % 2
# #         s = str(r) + s
# #         n = n // 2
# # print(s)

'''binary to decimal conversion'''
# n = input("enter the binary number: ")
# b = 0
# for i in range(len(n)):
#     b += int(n[-(i+1)]) * (2 ** i)
# print(b)
'''leetcode '''

nums=[1,1,2,2,3,1,4,4,5,5,6,7,8,8]
count =0
for  i in range(len(nums)):
    
    j=i+1
    if j <len(nums) and nums[i] == nums[j]:
        nums.pop(j) 
        print(nums[j])
        break  
    else:
        count+=1
print(count)

# '''new qs'''
# # reverse the integer and its shuld come in range 2^31 to 2^31-1
x=-123
s=""
for i in range (3):
    y=x%10
    
    x=x//10

print(s)
if int(s) < 2**31 and int(s) > -2**31:
    print("Valid")
else:
    print("Invalid")

# equation for  circle

x=int(input("enter the x coordinate "))
y=int(input("enter the y coordinate "))
r =int(input("enter the radius "))
h=0
k=0
z=r**2
k=((x+h)**2) + ((y+k)**2)
satisfy="inside"if k>z else "on" if k==z else "outside"

print(satisfy)


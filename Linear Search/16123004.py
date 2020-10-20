k = 4
l = [ 2,3,4,5,6,8]
flag=0
n = len(l)
for i in range(n):
    if l[i] == k:
        flag=1
        print("found")
        break
if(flag==0):
    print("the number is not in the list")



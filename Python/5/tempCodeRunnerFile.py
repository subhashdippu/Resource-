
num = 10
flag = True
for i in range(2, 5):
    if num%i==0:
        flag = False
        break
if flag is True:
    print("Yes")
else:
    print("No")
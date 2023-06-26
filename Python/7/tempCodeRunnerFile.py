while(True):
    num = int(input("Enter the no: "))

    def fac(num):
        prod = 1
        for i in range(1,num+1):
            prod = prod * i
        return prod
    f = fac(num)
    print(f)
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:  # else is going to run when the except is not going to run 
    print("We were successful")
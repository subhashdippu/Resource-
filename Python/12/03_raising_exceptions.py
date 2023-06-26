def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not true") # This will through an error which you want. it is called custum error set by you

a = increment('df364')
print(a)
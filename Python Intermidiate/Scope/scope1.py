# variable inside a function only available inside this function
def newfunc():
  i = 90
  print(i)

newfunc()

# print(i) # NameError
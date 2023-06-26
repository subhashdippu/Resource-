# Function inside another function scope available inside that function
def newfunc():
  i = 90
  # inner function
  def newinner():
      print(i)
  newinner()

newfunc()
# newinner() # NameError

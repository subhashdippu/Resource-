# Global Variable using global keyword
i = 90
def newfunc():
    global i
    i = 50
    print(i)

newfunc() # 50
print(i)  
  


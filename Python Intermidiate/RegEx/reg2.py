# Returning a list containing all matches
import re

newtext = "The rain rain rain in Germany and Spain"
x = re.findall("Brazil", newtext)

# decision if match or no
if x:
    print("Match")
else:
    print("No match")

# displaying
print(x)
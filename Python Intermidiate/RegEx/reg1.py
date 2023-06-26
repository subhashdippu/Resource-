#Searching string to see if it starts with "The" and ends with "Germany"
import re

newtext = "The match in Germany"
x = re.search("^The.*Germany$", newtext)
# print(x)
if x:
    print("Yes! We have a match")
else:
    print("No match")



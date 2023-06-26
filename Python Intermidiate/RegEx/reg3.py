# Searching for the first white-space using search()
import re

newtext = "The rain in Germany"
searching = re.search("\s", newtext)

print("The first white space is located in position:", searching.start())

# returning a list where the string has been split at each match
import re

newtext = "Python is a cross-platform language"
# newmatch = re.split("\s", newtext)

# Split string at first occurrence
newmatch = re.split("\s", newtext, 2) # Here the two element seprate with the ','

print(newmatch)

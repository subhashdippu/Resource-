# replacing the matches with the text of your choice
import re

newtext = "Python is a cross-platform language"
matching = re.sub("\s", "|", newtext)

print(matching)
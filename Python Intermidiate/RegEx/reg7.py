# replacing the matches with the text of your choice
import re

newtext = "Python is a cross-platform language"
# Control the number of replacements
matching = re.sub("\s", "&", newtext, 1)

print(matching)
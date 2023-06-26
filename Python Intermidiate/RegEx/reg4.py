# If no matches are found, the value None is returned
import re

newtext = "The rain in Germany"
matching = re.search("Brazil", newtext)

print(matching)
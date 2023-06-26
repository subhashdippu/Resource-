# Displaying start and end position of the first match occurrence
import re

newtext = "Python is a Cross-platform Language"
searching = re.search(r"\bL\w+", newtext)
# print(searching)
# print(searching.span())
# print(searching.string)
print(searching.group())



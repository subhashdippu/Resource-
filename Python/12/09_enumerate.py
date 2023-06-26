list1 = [3, 53, 2, False, 6.2, "Harry"]

# index = 1
# for item in list1:
#     print(item, index)
#     index += 1

for index, item in enumerate(list1,1): # enumerate second argumment is the counting no: starting point
    print(item, index)
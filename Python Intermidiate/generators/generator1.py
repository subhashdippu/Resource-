# # Building a simple generator function.
# def newGenerator():
#     print("First Result")
#     yield 20

#     # return

#     print("Second Result")
#     yield 40

#     print("Last Result")
#     yield 60

# # return values for each yield
# gen1 = newGenerator()
# print(next(gen1)) 
# print(next(gen1)) 
# print(next(gen1)) 

def generator():
    print("This is first")
    yield 4
    print("second")
    yield 6
    print("third")
    yield 7
ge = generator()
print(next(ge))
print(next(ge))
print(next(ge))
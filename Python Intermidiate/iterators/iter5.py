# Build iterator to return numbers, start from 1, and +1 each sequence
class NewNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 17:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

# Create Object based on NewNumbers class
newclass = NewNumbers()
newiter = iter(newclass)

# Displaying values one by one
# for x in newiter:
#     print(x)
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))

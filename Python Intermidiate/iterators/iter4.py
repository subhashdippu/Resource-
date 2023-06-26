# Build iterator to return numbers, start from 1, and +1 each sequence
class NewNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

# Create Object based on NewNumbers class
newclass = NewNumbers()
newiter = iter(newclass)

# Iterate over numbers
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
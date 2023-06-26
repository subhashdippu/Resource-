def calling():
    def returning():
        print("Hello from the inner")
    return returning

new = calling()

new()
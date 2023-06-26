while(True):
    print("Press q to quit")
    a = input("Enter a number: ")  # this will through an error without type casting because input always taken as string $ and it is called value error
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)  
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")
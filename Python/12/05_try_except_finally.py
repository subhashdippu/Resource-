while True:
    i = input("Enter a number: ")
    if i == 'q':
        break
    try:
        i = int(i)
        c = 1/i
    except Exception as e:
        print(e)
        exit()
    finally: # Whatever the cost finally will runs even when the program is exit() 
        print("We are done")

    # print("Thanks for using the program") 
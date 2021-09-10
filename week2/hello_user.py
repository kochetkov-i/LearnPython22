def hello_user():
    while True:
        try:
            user_say = str(input("How are you: "))
        except KeyboardInterrupt: 
            print("Bye!")
            break
        except ValueError:
            print("Input value error! Try again")
            continue
        if user_say == "Good":
            break

hello_user()

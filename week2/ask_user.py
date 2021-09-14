qvestions = {
    "How are you" : "Good",
    "What are you doing" : "Programming"
}

def ask_user():
    while True:
        user_qvestion = input("Ask me: ")
        if qvestions.get(user_qvestion) is not None and user_qvestion != "Exit":
            print(qvestions[user_qvestion])
        elif user_qvestion == "Exit":
            break
        else: 
            print("I don't know")

ask_user()

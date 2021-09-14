try:
    user_age = int(input("How old are you?: "))
except ValueError:
    print("Value error, try use integer next time")
    exit()

def get_action_by_age(age):
    answer = "You are too small for our actions"
    if age > 22:
        answer = "Your action is work"
    elif 22 >= age > 16:
        answer = "You are a student"
    elif 16 >= age > 6:
        answer = "You are a schoolboy"
    elif 6 >= age > 3:
        answer = "You goes to kindergarten"
    return answer

user_action = get_action_by_age(user_age)
print(user_action)

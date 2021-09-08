user_age = int(input("How old are you?: "))

def action_by_age(age):
    if age > 22:
        return "Your action is work"
    elif 22 >= age > 16:
        return "You are a student"
    elif 16 >= age > 6:
        return "You are a schoolboy"
    elif 6 >= age > 3:
        return "You goes to kindergarten"
    return "You are too small for our actions"

user_action = action_by_age(user_age)
print(user_action)

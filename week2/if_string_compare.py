def string_compare(string_first, string_second):
    if type(string_first) != str or type(string_second) != str:
        return 0
    elif string_first == string_second:
        return 1
    elif len(string_first) > len(string_second):
        return 2
    elif "learn" == string_second:
        return 3
    print("Something wrong")
    return 99

print(string_compare("learn","learn"))

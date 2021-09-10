def string_compare(string_first, string_second):
    if type(string_first) != str or type(string_second) != str:
        return 0
    elif string_first == string_second:
        return 1
    elif len(string_first) > len(string_second):
        return 2
    elif "learn" == string_second:
        return 3
    return 99

int_compare = string_compare("learn","learn")
if(int_compare == 99): 
    print("Something wrong")
print(int_compare)

def get_summ(one, two, delimiter = '&'):
    return f"{one}{delimiter}{two}"

string_combine = get_summ("Learn", "Python")
print(string_combine.upper())
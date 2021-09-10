#comment
user_name = input("what is your name: ")
print(f"Hello {user_name}, lets do some math")
x = 2
y = 10
z = 3
#let's some output
print(f"{x} + {x} = {x+x}")
print(f"{y} / {z} = {y/z}")

def compare_val(a, b):
    print(f"is X = {a} bigger then Y = {b} - {a > b}")


compare_val(x, y)
compare_val(z, x)
compare_val(y, y)

some_string = " Некоторая строка с кириллицей    ."

print(f"Длинна строки: {len(some_string)}")
print(some_string.strip().lower().capitalize())
for el in some_string.split(' '):
    print(el)

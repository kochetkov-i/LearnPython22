animals = ["dog", "cat", "chicken"]
print(len(animals))
animals.append("dog")
print(animals[-1])
print(animals[1:])
print(animals[:1])
print(animals.index("cat"))
print("rat" in animals)
print("cat" in animals)
animals.remove("cat")
print("cat" in animals)
print(animals[0])
def hello_world(name):
    if name == "":
        name = "World"
    return f"Hello {name}!"


text = input("Input your name: ")
print(hello_world(text))

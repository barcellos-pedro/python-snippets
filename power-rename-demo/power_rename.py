import os

print(os.getcwd())

path = os.getcwd()
init_text = "exercicio-1-letra-"

for dirpath, dirnames, files in os.walk(os.getcwd()):
    for file in files:
        file_name = os.path.splitext(file)[0]
        if file.endswith('.py'):
            continue
        current_name = "{}\{}.png".format(path, file_name)
        new_name = "{}\{}{}.png".format(path, init_text, file_name)
        try:
            os.rename(current_name, new_name)
        except Exception as error:
            print(error)

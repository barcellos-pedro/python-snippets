import os

"""
- - - - - - - - - - - -
"""

# print(dir(os))

# print(os.getcwd())

# os.chdir('exercicios-oop')

# print(os.getcwd())

"""
- - - - - - - - - - - -
"""

# print(os.listdir())

# os.mkdir('os-demo-2')
# os.makedirs('os-demo-3/sub-dir')
# os.mkdir('os-demo-to-delete')

# print(os.listdir('os-demo-2'))
# print(os.listdir('os-demo-3'))

# os.removedirs('os-demo-3/sub-dir')
# os.rmdir('os-demo-to-delete')
# os.rmdir('os-demo-2')

# print(os.listdir())

# os.makedirs('os-dir-example')
# os.rename('os-dir-example', 'os-dir-renamed')

# print(os.listdir())

"""
- - - - - - - - - - - -
"""

# from datetime import datetime

# print('info about this python file')
# print(f"Size: {os.stat('os_system.py').st_size}")

# time = datetime.fromtimestamp(os.stat('os_system.py').st_mtime)
# print(f"Time: {time}")

"""
- - - - - - - - - - - -
"""

# os.chdir('../')

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print("- - - - - - - - -")
#     print(f"Current path: {dirpath}")
#     print(f"Directories: {dirnames}")
#     print(f"Files: {filenames}")

"""
- - - - - - - - - - - -
"""

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), "test.txt")

# print(file_path)

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.splitext('/tmp/test.txt'))

# for dirname, basename in [os.path.split('/tmp/test.txt')]:
#     print('- - - - - -')
#     print(f"Dirname: {dirname}")
#     print(f"Basename: {basename}")
# print('- - - - - -')

# print(f"Path [{file_path}] exists? {os.path.exists(file_path)}")

# current_dir = os.getcwd()

# print(f"Is current dir directory? {os.path.isdir(current_dir)}")
# print(f"Is current dir file? {os.path.isfile(current_dir)}")

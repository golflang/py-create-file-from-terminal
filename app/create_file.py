import sys
import os
import datetime

print(sys.argv)
if "-d" in sys.argv and "-f" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f")
    if d_index < f_index:
        directories = sys.argv[d_index + 1:f_index]
        file_name = sys.argv[f_index + 1]
    else:
        directories = sys.argv[d_index + 1:]
        file_name = sys.argv[f_index + 1]
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    new_path = os.path.join(*directories, file_name)
elif "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    directories = sys.argv[d_index + 1:]
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    new_path = os.path.join(file_name)

if "-f" in sys.argv:
    new_file = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        else:
            new_file.append(user_input)

    is_empty = not os.path.exists(new_path) or os.path.getsize(new_path) == 0
    with open(new_path, "a") as f:
        if not is_empty:
            f.write("\n")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{date}\n")
        for index, string in enumerate(new_file):
            f.write(f"{index + 1} {string}\n")

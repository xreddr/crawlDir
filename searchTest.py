#Scandir test
import os
import stat

def search(target):
    print("Searching in: ", target)
    for entry in os.scandir(target):
        if entry.is_file():
            # yield entry.name
            print(entry.name)
        elif entry.is_dir():
            # yield entry.name
            print(entry.name)
            search(entry.path)

path = "c:/users/xreddr/repository"

search(path)
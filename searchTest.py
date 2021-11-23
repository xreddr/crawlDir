#Scandir test
import os
import stat

class scanner:
    def __init__(self, target):
        self.target = target
        
    def search(self):
        print("Searching in: ", self.target)
        for root, dirs, files in os.walk(self.target):
            for d in dirs:
                print(os.path.join(root, d))
            for f in files:
                print(os.path.join(root, f))
            break
        # for entry in os.scandir(self.target):
        #     if entry.is_file():
        #         # fc += 1
        #         # yield entry.name
        #         print(entry.name)
        #     elif entry.is_dir():
        #         # dc += 1
        #         # yield entry.name
        #         print(entry.name)
        #         self.target = entry.path
        #         scanner.search(self)
        # 
path = "c:/users/xreddr/repository"

s1 = scanner(path)
s1.search()

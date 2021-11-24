#Scandir test
import os
import stat

class scanner:
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
        self.dl = []
        self. fl = []
    def search(self):
        print("Searching in: ", self.target)
        for root, dirs, files in os.walk(self.target):
            for d in dirs:
                self.dl.append(os.path.join(root, d))
                # print(os.path.join(root, d))
            for f in files:
                self.fl.append(os.path.join(root, d))
                # print(os.path.join(root, f))
            break
        for i in self.dl:
            print(i)
            # s1.recurse()
    def recurse(self):
        i = self.target
        s1.search()
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

s1 = scanner(path, 1)
s1.search()

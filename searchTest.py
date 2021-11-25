#Scandir test
import os
import json
import stat

class scanner:
    root = []
    depth = []
    dl = []
    fl = []
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
        self.dl = []
        self.fl = []
    def search(self):
        if scanner.root == [] and scanner.depth == []:
            scanner.root.append(self.target)
            scanner.depth.append(self.depth)
        else:
            pass
        print("Searching in: ", self.target)
        for root, dirs, files in os.walk(self.target):
            for d in dirs:
                self.dl.append(os.path.join(root, d))
                scanner.dl.append(os.path.join(root, d))                
                # print(os.path.join(root, d))
            for f in files:
                self.fl.append(os.path.join(root, f))
                scanner.fl.append(os.path.join(root, f))
                # print(os.path.join(root, f))
            break
        if self.depth >= 1:
            self.depth -= 1
            x = scanner(self.target, self.depth)
            for i in self.dl:
                x.target = i
                x.search()
        else:
            data_report = {
                "Directories" : scanner.dl,
                "Files" : scanner.fl
            }
            global rp
            rp = json.dumps(data_report, indent=2)
            return

path = "c:/users/xreddr/repository"

s1 = scanner(path, 1)
s1.search()
print(rp)
print(scanner.root)
print(scanner.depth)

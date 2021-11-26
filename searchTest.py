#Scandir test
import os
import json

class scanner:
    root = []
    depth = []
    # dl = []
    # fl = []
    data = {
        "criteria" : [root, depth],
        "data" : {}
    }
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
                # scanner.dl.append(os.path.join(root, d))
                # scanner.data["data"].update({self.target : {"dirs" : self.dl,}})
            for f in files:
                self.fl.append(os.path.join(root, f))
                # scanner.fl.append(os.path.join(root, f))
                # scanner.data["data"].update({self.target : {"files" : self.fl,}})
            break
        scanner.data["data"].update({self.target : {"dirs" : self.dl, "files" : self.fl}})
        if self.depth >= 1:
            self.depth -= 1
            x = scanner(self.target, self.depth)
            for i in self.dl:
                x.target = i
                x.search()
        else:
            return

path = "c:/users/xreddr/repository/crawldir"

s1 = scanner(path, 1)
s1.search()
print(scanner.root)
print(scanner.depth)

print(json.dumps(scanner.data, indent=2))

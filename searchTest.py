#Scandir test
import os
import json

class scanner:
    root = []
    depth = []
    data = {
        "criteria" : [root, depth],
        "data" : {}
    }
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
    def search(self):
        dl = []
        fl = []
        if scanner.root == [] and scanner.depth == []:
            scanner.root.append(self.target)
            scanner.depth.append(self.depth)
        else:
            pass
        print("Searching in: ", self.target)
        for root, dirs, files in os.walk(self.target):
            for d in dirs:
                dl.append(os.path.join(root, d))
            for f in files:
                fl.append(os.path.join(root, f))
            break
        scanner.data["data"].update({self.target : {"dirs" : dl, "files" : fl}})
        if self.depth >= 1:
            self.depth -= 1
            x = scanner(self.target, self.depth)
            for i in dl:
                x.target = i
                x.search()
        else:
            global report
            scanner.report = json.dumps(scanner.data, indent=2)
            return

path = "c:/users/xreddr/repository/crawldir"

s1 = scanner(path, 1)
s1.search()

print(scanner.report)

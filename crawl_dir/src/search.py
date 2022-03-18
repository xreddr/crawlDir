# Search Engine
import os
import json
import datetime


def debug():
    ''' Takes hardcode to test Scanner object.'''

    path = "c:/users/xreddr/repos/"
    depth = 2

    s1 = Scanner(path, depth)
    s1.search()
    print(s1.report)


def scan(target, depth):
    ''' Takes user input. Returns json report.'''
    s = Scanner(target, depth)
    s.search()
    return s.report


class Scanner:
    data = {
        "criteria": {},
        "data": {}
    }

    def __init__(self, target, depth):
        self.target = target
        self.depth = depth

    def search(self):
        ''' Requires instance of object.'''
        dl = []
        fl = []
        if Scanner.data["criteria"] == {}:
            Scanner.data["criteria"]["target"] = (self.target)
            Scanner.data["criteria"]["depth"] = (self.depth)
            Scanner.data["criteria"]["timestamp"] = str(
                datetime.datetime.utcnow())

        for root, dirs, files in os.walk(self.target):
            for d in dirs:
                dl.append(os.path.join(root, d))
            for f in files:
                fl.append(os.path.join(root, f))
            break
        Scanner.data["data"].update({self.target: {"dirs": dl, "files": fl}})
        if self.depth >= 1:
            self.depth -= 1
            for i in dl:
                # t = self.target + "/" + i
                x = Scanner(i, self.depth)
                x.search()

        prep = json.dumps(Scanner.data, indent=2)
        tmp = prep.replace("\\", "/")
        self.report = tmp.replace("//", "/")

        if self.report:

            Scanner.data = {
                "criteria": {},
                "data": {}
            }


# s = json.loads(Scanner.report)
# print(s.keys())
# for i in s["data"].keys():
#     print(i)
if __name__ == '__main__':
    debug()

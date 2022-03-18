# CrawlDir by Ryan Henion 2021-2022 xreddr
from src import search


def main():
    welcome()


def welcome():
    while True:
        print("1) Start a new crawl\n2) Compare saved crawl")
        raw = input("Please select: ")
        valid = raw.lower()
        if valid == "1":
            print()
            print("New crawl starting...")
            # print(search.scan("c:/users/xreddr/repos/", 2))
            user_selection()
        if valid == "2":
            print()
            print("Saved crawl loading...")
            print("This feature is not yet available. Goodbye.")
            quit()


def user_selection():
    target = None
    depth = None
    while target is None:
        print("Please input the absolute path with '/' to a directory to crawl")
        raw = input(": ")
        target = raw
    while depth is None:
        print("How many sub-directories deep would you like to crawl?")
        raw = input(": ")
        depth = int(raw)
    print(search.scan(target, depth))


if __name__ == '__main__':
    main()

# CrawlDir by Ryan Henion 2021-2022 xreddr
from src import search, compare
import os
import json
import string
import re


def main():
    selection = None
    while selection is None:
        selection = welcome()
        if selection == "new":
            new_report = user_select_criteria()
            file_name = user_select_file_name()
            if new_report and file_name:

                save_file(new_report, file_name)

                selection = None
                continue

        elif selection == "compare":
            compare_file = user_select_compare_file()
            if compare_file:

                saved_object = open_file(compare_file)
                compare.compare_crawls(saved_object)

                selection = None
                continue

            # print(compare_file)

            # print(saves)


def save_file(data, file_name):
    ''' Takes file data, name. Saves .json to saves directory.'''
    prep = json.loads(data)
    path = "saves/" + file_name
    with open(path, 'w') as outfile:
        json.dump(prep, outfile, indent=4)
        outfile.close()
        print("File saved")


def open_file(file_name):
    ''' Takes file name. Opens from saves directory'''
    path = "saves/" + file_name
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
        print("File opened.")
    # compare_object = json.loads(data)
    print(type(data))
    return data


def welcome():
    selection = None
    while selection is None:
        print("1) Start a new crawl\n2) Compare saved crawl\n3) Quit")
        raw = input("Please select: ")
        valid = raw.lower()
        if valid == "1":
            print()
            print("New crawl starting...")
            selection = "new"
            return selection
        elif valid == "2":
            print()
            print("Saved crawls loading...")
            selection = "compare"
            return selection
        elif valid == "3":
            print("Goodbye")
            quit()


def user_select_criteria():
    target = None
    depth = None
    while target is None:
        print("Please input the absolute path with '/' to a directory to crawl")
        raw_target = input(": ")
        target = raw_target
    while depth is None:
        print("How many sub-directories deep would you like to crawl?")
        raw_depth = input(": ")
        depth = int(raw_depth)
    new_report = search.scan(target, depth)
    print(new_report)
    print(type(new_report))
    o = json.loads(new_report)
    print(type(o))
    return new_report


def user_select_file_name():
    file_name = None
    while file_name is None:
        raw = input(
            "\nPlease choose a name to save the crawl under \n(Special characters and spaces will be ignored): ")
        pattern = r'[' + string.punctuation + ']'
        tmp = re.sub(pattern, '', raw)
        tmp = tmp.replace(" ", "")
        valid = tmp + '.json'
        confirm = False
        while confirm == False:
            print(valid)
            ans = input("Is this filename OK? (Y/N): ").upper()
            if ans == "Y":
                file_name = valid
                confirm = True
            if ans == "N":
                break
    return file_name


def user_select_compare_file():
    saves = search.scan("saves", 0)
    prep = saves.replace("saves/", "")
    save_data = json.loads(prep)
    for file in save_data["data"]["saves"]["files"]:
        print(file)
    selection = None
    while selection is None:
        raw = input("Please select a saved crawl for comparison: ")
        extension = False
        if ".json" not in raw:
            raw = raw + ".json"
            extension = True
        elif ".json" in raw:
            extension = True
        if extension:
            saved_file = raw
            return saved_file


if __name__ == '__main__':
    main()

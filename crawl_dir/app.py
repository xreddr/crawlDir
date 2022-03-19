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

            compare_file = user_select_saved_file()

            if compare_file:

                saved_object = open_file(compare_file)

                if saved_object is None:
                    selection = None
                    continue

                compare.compare_crawls(saved_object)

                selection = None
                continue

        elif selection == "manage":

            selected_file = user_select_saved_file()
            if selected_file:

                file_manage_menu(selected_file)

                selection = None
                continue


def welcome():
    selection = None
    while selection is None:
        print(
            "\n1) Start a new crawl\n2) Compare saved crawl\n3) Manage saved crawls\n4) Quit")
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
            print()
            print("Saved crawls loading...")
            selection = "manage"
            return selection
        elif valid == "4":
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


def user_select_saved_file():
    saves = search.scan("saves", 0)
    prep = saves.replace("saves/", "")
    save_data = json.loads(prep)
    for file in save_data["data"]["saves"]["files"]:
        print(file)
    selection = None
    while selection is None:
        raw = input("Please select a saved crawl: ")
        extension = False
        if ".json" not in raw:
            raw = raw + ".json"
            extension = True
        elif ".json" in raw:
            extension = True
        if extension:
            saved_file = raw
            return saved_file


def file_manage_menu(file_name):
    loop = True
    while loop == True:
        raw_ans = input(
            "1) View crawl info\n2) Delete crawl file\n3) Return to menu\nWhat would you like to do? ")
        valid = raw_ans.lower()
        if valid == "1":
            data = open_file(file_name)
            print(json.dumps(data, indent=2))
            input("Press ENTER to continue")
            continue
        if valid == "2":
            ans = input(
                f"Are you sure you want to delete {file_name}? (Y/N): ").upper()
            if ans == "Y":
                path = "saves/" + file_name
                os.remove(path)
                loop = False
            elif ans == "N":
                continue
        if valid == "3":
            loop = False


def save_file(data, file_name):
    ''' Takes file data, name. Saves .json to saves directory.'''
    try:
        os.makedirs("saves")
    except OSError:
        pass
    prep = json.loads(data)
    path = "saves/" + file_name
    with open(path, 'w') as outfile:
        json.dump(prep, outfile, indent=4)
        outfile.close()
        print("File saved")


def open_file(file_name):
    ''' Takes file name. Opens from saves directory'''
    path = "saves/" + file_name
    try:
        with open(path, 'r') as infile:
            data = json.load(infile)
            infile.close()
            print("File opened.")
        # compare_object = json.loads(data)
        print(type(data))

        return data

    except FileNotFoundError:
        print("No such crawl is saved")
        return None


if __name__ == '__main__':
    main()

#File Crawler
"""
To count directories and files within another directory and
compare the results over time to track accumulating files.
To do:
Set up user input for "depth of search"
Bring compare function into loop?
"""
import sys #to use sys.exit() for UI
import os #to operate within directories
import datetime #to compare time stamps
import json #for file saving

#UI prompts
def welcome():
    user_input = input("Would you like to start a new crawl?")
    if user_input == "yes":
        pathInput()
    elif user_input == "no":
        print("Goodbye")
        print("<(^.^<) (>^.^)>")
        sys.exit()
    else:
        print("Please choose 'yes' or 'no'.")
        welcome()
#Depth of search using os.scandir()
def pathInput():
    global path_input
    path_input = input("Choose top directory: c:/")
    path_check = "c:/" + path_input + "/"
    print(path_check)
    global target_path
    target_path = path_check
    searchDepth()
    
def searchDepth():
    # global top_dir
    # global bottom_dir
    # top_dir = False
    # bottom_dir = False
    # print("Select depth of search:")
    # print("'top' - Search target directory")
    # print("'bottom' - Search target and all subdirectories")
    # search_depth = input("Choose depth of search:")
    # if search_depth == "top":
    #     top_dir = True
    # elif search_depth == "bottom":
    #     bottom_dir = True
    # else:
    #     print("Please choose 'top' or 'bottom'")
    #     searchDepth()
    search()
#Allowing argument for multiple sources
#Use scandir() for argument controlled recursion
def search():
    total_files = 0
    total_dirs = 0
    data_list = []
    for root, dirs, files in os.walk(target_path):
        print("Searching in : ", root)
        for directories in dirs:
            data_list.append(os.path.join(root, directories))
            #print(os.path.join(root, directories))
            #global total_dirs
            total_dirs += 1
        for Files in files:
            data_list.append(os.path.join(root, Files))
            #print(os.path.join(root, Files))
            #global total_files
            total_files += 1
        break
        # if top_dir == True:
        #     break
        # elif bottom_dir == True:
        #     pass
        # else:
        #     print("An error occured")
        #     welcome()
    if total_files + total_dirs == 0:
        print("Nothing located")
        welcome()
    else:
        #Uhh should search create the data_object?
        global data_object
        data_object = {
        "criteria" : target_path,
        "paths" : data_list,
        "files" : total_files,
        "directories" : total_dirs,
        "date" : str(datetime.datetime.now())
        }
        
        report_object = json.dumps(data_object, indent=2)
        print(report_object)
        
        epilogue()
    
def epilogue():
    save_input = input("Would you like to save?")
    if save_input == "yes":
        fileSave()
    elif save_input == "no":
        welcome()
    else:
        print("Please choose 'yes' or 'no'.")
        epilogue()

def fileSave():
    with open("crawlData.json", "w") as outfile:
        json.dump(data_object, outfile, indent=2)
    outfile.close()

    # f = open("crawlData.json", "r")
    # print(f.read())
    # f.close()
    
    print("File Saved")
    welcome()
    
print("o--(====> Welcome to CrawlDir <====)--o")
welcome()

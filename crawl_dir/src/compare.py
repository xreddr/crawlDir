# Compare crawled json objects!
import json
from src import search


def compare_crawls(saved_object):
    target_criteria = saved_object["criteria"]["target"]
    # print(target_criteria)
    depth_criteria = saved_object["criteria"]["depth"]
    # print(depth_criteria)
    new_string = search.scan(target_criteria, depth_criteria)
    new_object = json.loads(new_string)
    # print(type(saved_object), type(new_object))
    # print(saved_object["data"] == new_object["data"])
    # print(json.dumps(new_object, indent=2))
    saved_list = []
    new_list = []
    for k in saved_object["data"].keys():
        for d in saved_object["data"][k]["dirs"]:
            saved_list.append(d)
        for f in saved_object["data"][k]["files"]:
            saved_list.append(f)

    for j in new_object["data"].keys():
        for d in new_object["data"][j]["dirs"]:
            new_list.append(d)
        for f in new_object["data"][j]["files"]:
            new_list.append(f)

    # print(json.dumps(saved_list, indent=2))
    # print(json.dumps(new_list, indent=2))

    del_list = [item for item in saved_list if item not in new_list]
    add_list = [item for item in new_list if item not in saved_list]

    del_items = json.dumps(del_list, indent=2)
    add_items = json.dumps(add_list, indent=2)

    print(f"Deleted items: {del_items}")
    print(f"Added items: {add_items}")
    input("Press ENTER to continue")

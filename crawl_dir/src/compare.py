# Compare crawled json objects!
import json
from src import search


def compare_crawls(saved_object):
    target_criteria = saved_object["criteria"]["target"]
    print(target_criteria)
    depth_criteria = saved_object["criteria"]["depth"]
    print(depth_criteria)
    new_string = search.scan(target_criteria, depth_criteria)
    new_object = json.loads(new_string)
    # print(type(saved_object), type(new_object))
    # print(saved_object["data"] == new_object["data"])
    # print(json.dumps(new_object, indent=2))

    for k in saved_object["data"].keys():
        for j in new_object["data"].keys():
            print(k == j)

            del_list = [item for item in saved_object["data"]
                        [k] if item not in new_object["data"][j]]
            add_list = [item for item in new_object["data"]
                        [j] if item not in saved_object["data"][k]]

            print(del_list)
            print(add_list)

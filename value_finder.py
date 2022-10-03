import json
import argparse


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

    
def get_value(object,key):
    key_list = key.split("/")
    # print(key_list)
    for item in key_list:
        if item in object.keys():
            object = object[item]
        else:
            print("Incorrect Key provided: '" + item + "' is not a key")
    return object

    
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--object", type=str, default='{"a":{"b":{"c":"d"}}}')
    parser.add_argument("--key", type=str, default="a/b/c")
    args = parser.parse_args()
    object = args.object
    print(type(object))
    key = args.key
    # object = {"a":{"b":{"c":"d"}}}
    # key = "a/b/c"
    object_dict = to_dict(object)
    print(type(object_dict))
    value = get_value(object, key)
    print(value)

import os
import sys
import json

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=sort_keys)
        )

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("""
This is a CLI tool in Python that formats JSON
It takes a single argument. 

Usage: python3 jformat.py [path to json file]
        """)
        sys.exit(0)
    if "--no-sort" in sys.argv:
        no_sort = True
    else:
        no_sort = False
    main(sys.argv[-1], no_sort=no_sort)



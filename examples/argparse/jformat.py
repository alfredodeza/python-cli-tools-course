import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(args):
    with open(args.path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=args.sort)
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is the jformat tool")
    parser.add_argument("--sort", action="store_true", help="set the sorting")
    parser.add_argument("path", help="The path to a JSON file")
    args = parser.parse_args()
    main(args)



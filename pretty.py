#!/usr/bin/env python3

import os
import json

def iter_json_files():
    for dirpath, _, filenames in os.walk("."):
        for f in filenames:
            if f.endswith(".json"):
                yield os.path.join(dirpath, f)


if __name__ == "__main__":
    for f in iter_json_files():
        r = open(f, "r")
        c = json.loads(r.read())
        r.close()
        w = open(f, "w")
        w.write(json.dumps(c, indent=1, sort_keys=True))
        w.close()

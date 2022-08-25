import sys
import json

import lib.lexer as l

if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        data = json.load(f)
        l.loop(data)
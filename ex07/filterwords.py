import sys
import re

txt = sys.argv[1]
if len(sys.argv) != 3 or txt.isnumeric() or not sys.argv[2].isnumeric():
    print("ERROR")
    exit(0)
splitted = (re.split(r'[\W]+', sys.argv[1]))
i = 0
while i < len(splitted):
    if len(splitted[i]) <= int(sys.argv[2]):
        del splitted[i]
        i -= 1
    i += 1
print(splitted)

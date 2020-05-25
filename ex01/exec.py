import sys

str = ""
i = 0
for arg in sys.argv:
    if i == 1:
            str += arg
    elif i > 1:
            str += ' '
            str += arg
    i += 1
rep = str[::-1].swapcase()
if rep:
    print(rep)

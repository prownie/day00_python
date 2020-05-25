import sys

str = ""
i = 0
if (len(sys.argv) != 2):
    print("ERROR")
    sys.exit(0)
if (sys.argv[1].isnumeric()):
    nb = int(sys.argv[1])
    if (nb == 0):
        print("I'm Zero.")
    elif (nb % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("ERROR")
    sys.exit(0)

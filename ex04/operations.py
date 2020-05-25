import sys


def print_error():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
    return


if len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    print_error()
    exit(0)
elif len(sys.argv) == 1:
    print_error()
    exit(0)
elif len(sys.argv) < 3:
    print("InputError: not enough arguments\n")
    print_error()
    exit(0)
if sys.argv[1].isnumeric() is False or sys.argv[2].isnumeric() is False:
    print("InputError: only numbers\n")
    print_error()
    exit(0)
nb1 = int(sys.argv[1])
nb2 = int(sys.argv[2])
print("Sum:\t\t", nb1 + nb2)
print("Difference:\t", nb1 - nb2)
print("Product:\t", nb1 * nb2)
if nb2 == 0:
    print("Quotient:\t ERROR (div by zero)")
else:
    print("Quotient:\t", nb1 / nb2)
if nb2 == 0:
    print("Remainder:\t ERROR (div by zero)")
else:
    print("Remainder:\t", nb1 % nb2)

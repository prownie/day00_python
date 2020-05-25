t = (19, 42, 21)

print("The", len(t), "numbers are: ", end='')
count = 0
for i in t:
    print(i, end='')
    if count != len(t) - 1:
        print(", ", end="")
    count += 1

import sys


letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morse_lettr = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
               '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-',
               '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
morse_number = ['-----', '.----', '..---', '...--', '....-', '.....', '-....',
                '--...', '---..', '----.']

joined = ' '.join(sys.argv[1:]).lower()
for a in joined:
    if not a.isalnum() and not a.isspace():
        print("ERROR")
        exit(0)
cpt = 0
for i in joined:
    if i.isdigit():
        print(morse_number[int(i)], end='')
    elif i.isalpha():
        print(morse_lettr[ord(i) - ord('a')], end='')
    else:
        print("/", end='')
    cpt += 1
    if (cpt < len(joined)):
        print(" ", end='')

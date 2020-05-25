import string

def text_analyzer(*texts):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if (len(texts) == 0):
        text = input("What is the text to analyse?\n>> ")
    elif (len(texts) > 1):
        print("ERROR")
        return
    else:
        text = texts[0]
    upper = 0
    lower = 0
    punc = 0
    space = 0
    i = len(text) - 1
    nb_chara = i
    while (i >= 0):
        if (text[i].isupper()):
            upper += 1
        elif (text[i].islower()):
            lower += 1
        elif (text[i].isspace()):
            space += 1
        elif (text[i] in string.punctuation):
            punc += 1
        i = i - 1
    print ("The text contains", nb_chara, "characters:\n")
    print("-", upper, "upper letters\n")
    print("-", lower, "lower letters\n")
    print("-", punc, "punctuation marks\n")
    print("-", space, "spaces")
    return

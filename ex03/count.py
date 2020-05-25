import string


def text_analyzer(*texts):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if (len(texts) == 0):
        text = ""
        while text == "":
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
    for i in text:
        if (i.isupper()):
            upper += 1
        elif (i.islower()):
            lower += 1
        elif (i.isspace()):
            space += 1
        elif (i in string.punctuation):
            punc += 1
    print("The text contains", len(text), "characters:\n")
    print("-", upper, "upper letters\n")
    print("-", lower, "lower letters\n")
    print("-", punc, "punctuation marks\n")
    print("-", space, "spaces")
    return

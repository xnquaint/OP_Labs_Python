
def fillString():
    string_ = input("Enter the string: ")
    return string_


def fillSymbols():
    symb = input("Enter the symbols: ")
    return symb


def createWords(string_):
    list_words = string_.split(" ")
    return list_words


def findWords(list_words, symb):
    k = 0
    for x in list_words:
        if x[:len(symb)] == symb:
            k += 1
    return k


string = fillString()
symbols = fillSymbols()
words = createWords(string)
n = findWords(words, symbols)
print(f"The number of words starting with \"{symbols}\" is: {n}")
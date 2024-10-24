
def main():
    path = "books/frankenstein.txt"
    text = open_book(path)
    #print(text)
    wordcount = count_words(text)
    print(wordcount)
    chardictionary = count_characters(text)
    print(chardictionary)


def open_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    i = 0
    for word in text.split():
        i += 1
    return i

def count_characters(text):
    chardict = {}
    for char in text.lower():
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict



main()

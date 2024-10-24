
def main():
    path = "books/frankenstein.txt"
    text = open_book(path)
    #print(text)
    wordcount = count_words(text)
    print(wordcount)



def open_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    i = 0
    for word in text.split():
        i += 1
    return i


main()

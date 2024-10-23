
def main():
    path = "books/frankenstein.txt"
    text = open_book(path)
    print(text)



def open_book(path):
    with open(path) as f:
        return f.read()



main()


def main():
    path = "books/frankenstein.txt"
    text = open_book(path)
    #print(text)
    wordcount = count_words(text)
    #print(wordcount)
    chardictionary = count_characters(text)
    #print(chardictionary)
    sortedlist = chars_dict_to_sorted_list(chardictionary)


    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document")
    print()

    for item in sortedlist:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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
        if char.isalpha():
            if char in chardict:
                chardict[char] += 1
            else:
                chardict[char] = 1
    return chardict


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()

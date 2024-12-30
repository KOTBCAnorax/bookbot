book_path = "books/frankenstein.txt"
whitespaces = (' ', '\n')


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_characters(text):
    tmp_text = text.lower()
    dct = {}
    for c in tmp_text:
        if c not in whitespaces:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1

    return dct


def dictionary_to_list_of_dcitionaries(dct):
    lst = []
    for key in dct:
        lst.append({"name": key, "num": dct[key]})

    return lst


def print_list_of_dictionaries(lst):
    for dct in lst:
        c = dct["name"]
        n = dct["num"]
        print(f"The '{c}' character appeared {n} times")


def sort_on(dct):
    return dct["num"]
    


def main():
    text = get_book_text(book_path)
    characters = count_characters(text)
    list_of_characters = dictionary_to_list_of_dcitionaries(characters)
    list_of_characters.sort(reverse=True, key=sort_on)

    arr = text.split()
    print(f"----------Begin Report on {book_path}----------")
    print(f"There are {len(arr)} words in {book_path}")
    print("")
    print_list_of_dictionaries(list_of_characters)
    print("---------End Report----------")



main()

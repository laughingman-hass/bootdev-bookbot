def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    print_letter_report(letter_count)

    print("--- End report ---")


def get_book_content(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_count(text):
    letter = {}
    for c in text:
        if not c.isalpha():
            continue

        if c.lower() in letter:
            letter[c.lower()] += 1
        else:
            letter[c.lower()] = 1

    return letter


def sort_on(dict):
    return dict["count"]


def print_letter_report(letter_dict):
    letter_list = []
    for l in letter_dict:
        letter_list.append({"letter": l, "count": letter_dict[l]})

    letter_list.sort(reverse=True, key=sort_on)

    for l in letter_list:
        print(f"The '{l["letter"]}' character was found {l["count"]} times")


main()

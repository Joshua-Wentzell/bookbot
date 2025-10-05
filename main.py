from stats import count_words

def main ():
    book_path = "books/frankenstein.txt"
    book_text = read_contents(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    print_report(book_path, word_count, char_count)

def sort_on(dict):
    return dict["count"]

def read_contents (file_path):
    with open(file_path) as f:
        return f.read()

def count_characters (book_text):
    char_count = {}
    for char in book_text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

def print_report (book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {word_count} total words\n")
    list_chars = []
    for char in char_count:
        if char.isalpha():
            list_chars.append({"char":char, "count": char_count[char]})
    list_chars.sort(reverse=True, key=sort_on)
    for char in list_chars:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")

main()
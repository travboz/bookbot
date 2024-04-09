def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letter_frequency(text):
    char_counts = {}

    for ch in text.lower():
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1

    return char_counts


def sort_on_value(dict):
    return dict["num"]


def generate_report(book_path):
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    text_word_count = count_words(text)
    character_frequencies = count_letter_frequency(text)

    character_frequencies.sort(reverse=True, key=sort_on_value)

    print(f"--- Begin report of {book_path} ---")

    print(f"{text_word_count} words found in the document\n")

    for k, v in character_frequencies.items():
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_word_count = count_words(text)
    character_frequencies = count_letter_frequency(text)

    print(f"The number of words in the text: {text_word_count}")
    print(f"The frequencies of each character in the text: {character_frequencies}")


if __name__ == "__main__":
    main()

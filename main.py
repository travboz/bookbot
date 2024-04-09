def get_book_text(book_path):
    """Get the text content of a file returned as a string"""
    with open(book_path) as f:
        return f.read()


def count_words(text):
    """Count the words in text"""
    words = text.split()
    return len(words)


def count_letter_frequency(text):
    """Calculate the frequency of characters in a text"""
    char_counts = {}

    for ch in text.lower():
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1

    return char_counts


# callback function to sort by - sorting by the count of characters
def sort_on_value(dict):
    """Callback to sort by the count value of the dict"""
    return dict["count"]


def sort_chars_counts(cdict):
    """Sort the character dictionary in descending order by value"""
    chars = []
    for char, freq in cdict.items():
        if char.isalpha():
            chars.append({"char": char, "count": freq})

    chars.sort(reverse=True, key=sort_on_value)
    return chars


def generate_report(book_path):
    """Generate a highlight report of a book"""
    text = get_book_text(book_path)
    text_word_count = count_words(text)
    character_frequencies = count_letter_frequency(text)
    sorted = sort_chars_counts(character_frequencies)

    print(f"--- Begin report of {book_path} ---")
    print(f"{text_word_count} words found in the document\n")

    for info in sorted:
        print(f"The '{info["char"]}' character was found {info["count"]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    generate_report(book_path)


if __name__ == "__main__":
    main()

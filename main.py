def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


if __name__ == "__main__":
    main()

import string
import secrets
import random

import zxcvbn


def random_passphrase():
    """
    Creates a random passphrase primarily using the Python secrets module and
    specific books from Project Gutenberg.
    """

    # Book filenames relative location.
    filename_1 = "books/book_1.txt"
    filename_2 = "books/book_2.txt"
    filename_3 = "books/book_3.txt"
    filename_4 = "books/book_4.txt"

    # Try to open the book filenames as a string, replace digits and
    # punctuation, make words lowercase, and split words into list.
    try:
        with open(filename_1, encoding="utf-8") as f:
            book = f.read()
            for character in string.digits:
                book = book.replace(character, "")
            for character in string.punctuation:
                book = book.replace(character, "")
            word_list_1 = book.lower().split()
        with open(filename_2, encoding="utf-8") as f:
            book = f.read()
            for character in string.digits:
                book = book.replace(character, "")
            for character in string.punctuation:
                book = book.replace(character, "")
            word_list_2 = book.lower().split()
        with open(filename_3, encoding="utf-8") as f:
            book = f.read()
            for character in string.digits:
                book = book.replace(character, "")
            for character in string.punctuation:
                book = book.replace(character, "")
            word_list_3 = book.lower().split()
        with open(filename_4, encoding="utf-8") as f:
            book = f.read()
            for character in string.digits:
                book = book.replace(character, "")
            for character in string.punctuation:
                book = book.replace(character, "")
            word_list_4 = book.lower().split()
    # If book filenames cannot be found, show an error.
    except FileNotFoundError:
        print(
            "Error: A book file cannot be found. You may need to add a book text file."
        )
    # If reading book filenames were successful, choose a random list of words
    # from the secrets module, shuffle the position of the words using
    # the random module, and print the passphrase.
    else:
        random_word_1 = secrets.choice(word_list_1)
        random_word_2 = secrets.choice(word_list_2)
        random_word_3 = secrets.choice(word_list_3)
        random_word_4 = secrets.choice(word_list_4)

        # It appears the secrets module does not have a shuffle ability like
        # the random module, which is why it's being used here, but AFTER the
        # secrets module has run.
        random_words = [random_word_1, random_word_2, random_word_3, random_word_4]
        random.shuffle(random_words)

        passphrase = f"{random_words[0]} {random_words[1]} {random_words[2]} "
        passphrase += f"{random_words[3]}"

        return passphrase


def passphrase_strength(passphrase):
    """
    Uses zxcvbn-python to determine passphrase strength, and can give more
    information if needed.
    """

    # Follows the same principles as https://bitwarden.com/password-strength/
    passphrase_results = zxcvbn.zxcvbn(passphrase)
    crack_result = f"{passphrase_results['crack_times_display']['offline_slow_hashing_1e4_per_second'].title()}"

    return crack_result


def display_results():
    """
    Calls on random_passphrase() and passphrase_strength() functions and
    then displays the results.
    """

    TITLE = "Passphrase Generator"
    VERSION = "1.0.0"
    WEBSITE = "https://github.com/PyDevJohn/passphrase-generator"
    LICENSE = "MIT License"
    BUILT_WITH = "\t- PyInstaller (https://github.com/pyinstaller/pyinstaller)"
    BUILT_WITH += "\n\t- zxcvbn-python (https://github.com/dwolfhub/zxcvbn-python)"
    BOOKS_USED = "\t- Alice's Adventures in Wonderland by Lewis Carroll "
    BOOKS_USED += "(https://gutenberg.org/ebooks/11) \n\t- Frankenstein; Or, "
    BOOKS_USED += "The Modern Prometheus by Mary Wollstonecraft Shelley "
    BOOKS_USED += "(https://gutenberg.org/ebooks/84) \n\t- Winnie-the-Pooh by "
    BOOKS_USED += "A. A. Milne (https://www.gutenberg.org/ebooks/67098) \n\t- "
    BOOKS_USED += "A Manual or an Easy Method of Managing Bees by John M. "
    BOOKS_USED += "Weeks (https://www.gutenberg.org/ebooks/27065)"

    print(f"{TITLE}")
    print(f"Version: {VERSION}")
    print(f"Website: {WEBSITE}")
    print(f"License: {LICENSE}")
    print(f"Built with: \n{BUILT_WITH}")
    print(f"Books used for passphrases: \n{BOOKS_USED}")

    while True:
        passphrase = random_passphrase()
        crack_result = passphrase_strength(passphrase)

        print(f"\nPassphrase: {passphrase}")
        print(f"Estimated time to crack passphrase: {crack_result}\n")

        regenerate = input("Would you like to generate another passphrase? " "(y/n) ")
        if regenerate.lower().strip() == "n":
            break


# Run the below if this file is the main file being opened.
if __name__ == "__main__":
    display_results()

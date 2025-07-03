### 10-10. Common Words:

from pathlib import Path

def count_words(word,text):
    """By a given 'word', checks how many occurences are found in 'text'"""
    count = text.count(f"{word} ")
    count += text.count(f"{word}.")
    count += text.count(f"{word}(")
    return count


def count_books_words(word, book_name):
    """Opens a file of a book and matches and finds occurence of a word"""
    path = Path(book_name)

    try:
        book = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"{book_name} not found")
    else:
        print(f"Book '{book_name}' contains the word '{word}' {count_words(word, book.lower())} times.")


count_books_words("the", "text_files/monte_cristo.txt")
count_books_words("is", "text_files/monte_cristo.txt")
count_books_words("the", "Odyssey.txt")
count_books_words("the", "text_files/peloponnesian_war.txt")
count_books_words("war", "text_files/peloponnesian_war.txt")
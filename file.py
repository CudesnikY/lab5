import re

def read_first_sentence(filename):
    """Зчитує перше речення з текстового файлу."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'[.!?]', text)[0]  # Зчитує перше речення до першої крапки, знака оклику чи питання
            print("Перше речення:", first_sentence)
            return first_sentence
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except IOError:
        print("Помилка читання файлу.")
        return None

def sort_words(text):
    """Виводить слова, відсортовані по алфавіту з поділом на українські та англійські слова."""
    words = re.findall(r'\b\w+\b', text)  # Знаходить усі слова без пунктуації
    ukrainian_words = sorted([word for word in words if re.search(r'[а-яА-Я]', word)], key=str.lower)
    english_words = sorted([word for word in words if re.search(r'[a-zA-Z]', word)], key=str.lower)

    print("\nСлова на українській мові (в алфавітному порядку):", ukrainian_words)
    print("Слова на англійській мові (в алфавітному порядку):", english_words)
    print("\nЗагальна кількість слів:", len(words))

def main():
    filename = 'text.txt'  # Ім'я файлу з текстом
    first_sentence = read_first_sentence(filename)
    if first_sentence:
        sort_words(first_sentence)

if __name__ == "__main__":
    main()
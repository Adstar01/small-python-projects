from collections import Counter
import re


def get_frequency(text) -> list[tuple[str,int]]:
    lowered_text = text.lower()
    words = re.findall(r'\b\w+\b', lowered_text)
    word_counts = Counter(words)
    return word_counts.most_common()


def main() -> None:
    text = input("Enter your text: ").strip()
    word_frequencies = get_frequency(text)

    print(word_frequencies)


if __name__ == "__main__":
    main()
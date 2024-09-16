


def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyse(text: str) -> dict[str, int]:

    print("Text: ",text)
    result: dict[str, int]={
        "total_chars_incl_spaces": len(text),
        "total_chars_excl_spaces": len(text.replace(' ','')),
        "total_spaces": text.count(' '),
        "total_words": len(text.split())
    }

    return result

def main() -> None:
    text: str = open_file("note.txt")
    analysis: dict[str, int] = analyse(text)

    for key, value in analysis.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
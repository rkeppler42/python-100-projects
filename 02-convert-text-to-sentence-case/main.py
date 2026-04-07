def main() -> None:
    """Convert a text to Sentence Case."""
    with open("snowwhite.txt") as file:
        text = file.read()
    
    sentences = text.split(". ")

    list_of_sentences = [sentence.capitalize() for sentence in sentences]

    final_sentence = ". ".join(list_of_sentences) + "."
    
    with open("snowwhite_corrected.txt", "w") as file:
        file.write(final_sentence)

if __name__ == "__main__":
    main()
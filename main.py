def analyze_text(text, save_to_file=False, filename="text_analysis.txt"):
    text = text.lower()
    word_list = text.split()
    word_count = len(word_list)
    first_char = text[0]
    last_char = text[-1]
    reversed_words = ' '.join(word_list[::-1])
    contains_python = 'python' in text

    results = {
        "word_count": word_count,
        "first_character": first_char,
        "last_character": last_char,
        "reversed_word_order": reversed_words,
        "contains_python": contains_python
    }

    if save_to_file:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Text Analysis Results:\n")
            f.write(f"Total words: {word_count}\n")
            f.write(f"First character: {first_char}\n")
            f.write(f"Last character: {last_char}\n")
            f.write(f"Reversed word order: {reversed_words}\n")
            f.write(f"'python' found in text: {'Yes' if contains_python else 'No'}\n")

    return results

# Example usage
if __name__ == "__main__":
    user_input = input("Enter the text you want to analyze: ")
    analysis = analyze_text(user_input, save_to_file=True)
    
    # Print results to console
    print("\n--- Analysis Results ---")
    for key, value in analysis.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

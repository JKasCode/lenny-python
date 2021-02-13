def format_input(text):
    formatted = ""

    formatted = text.lower()
    for letter in "?!.,\"'":
        formatted = formatted.replace(letter, "")

    return formatted
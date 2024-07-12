# soundex.py

def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def generate_initial_soundex(name):
    if not name:
        return "", ""

    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def should_add_code(code, prev_code):
    return code != '0' and code != prev_code

def process_character(char, prev_code):
    code = get_soundex_code(char)
    if should_add_code(code, prev_code):
        return code, code
    return '', prev_code

def process_characters(name, first_letter_code):
    soundex = []
    prev_code = first_letter_code

    for char in name[1:]:
        code, prev_code = process_character(char, prev_code)
        if code:
            soundex.append(code)
        if len(soundex) == 3:  # Since the first letter is already included, we need only 3 more codes
            break

    return soundex

def pad_soundex(soundex):
    while len(soundex) < 3:  # Now we pad to ensure only 3 additional codes
        soundex.append('0')
    return ''.join(soundex)

def generate_soundex(name):
    first_letter, first_letter_code = generate_initial_soundex(name)
    soundex = process_characters(name, first_letter_code)
    return first_letter + pad_soundex(soundex)

def main():
    name = input("Enter a name to generate its Soundex code: ")
    print("Soundex code:", generate_soundex(name))

if __name__ == '__main__':
    main()

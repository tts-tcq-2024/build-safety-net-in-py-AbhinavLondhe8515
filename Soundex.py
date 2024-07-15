def get_soundex_code(c):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c.upper(), '0')  # Default to '0' for non-mapped characters

def generate_initial_soundex(name):
    if not name:
        return "", "0"

    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def process_characters(name, first_letter_code):
    soundex = []
    prev_code = first_letter_code

    for char in name[1:]:
        code = get_soundex_code(char)
        if code == '0':
            prev_code = '0'  # Reset prev_code if the current character is '0'
            continue
        if code != prev_code:
            soundex.append(code)
            prev_code = code
            if len(soundex) == 3:
                break

    return soundex

def pad_soundex(soundex):
    return ''.join(soundex).ljust(3, '0')

def generate_soundex(name):
    if not name:
        return "0000"

    first_letter, first_letter_code = generate_initial_soundex(name)
    soundex = process_characters(name, first_letter_code)
    return first_letter + pad_soundex(soundex)

def main():
    name = input("Enter a name to generate its Soundex code: ")
    print("Soundex code:", generate_soundex(name))

if __name__ == '__main__':
    main()

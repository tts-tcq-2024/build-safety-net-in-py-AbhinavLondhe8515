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

def process_remaining_characters(name, first_letter_code):
    soundex = [first_letter_code]
    prev_code = first_letter_code

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:
            break

    return soundex

def pad_soundex(soundex):
    while len(soundex) < 4:
        soundex.append('0')
    return ''.join(soundex)

def generate_soundex(name):
    first_letter, first_letter_code = generate_initial_soundex(name)
    soundex = process_remaining_characters(name, first_letter_code)
    return pad_soundex([first_letter] + soundex[1:])

def main():
    name = input("Enter a name to generate its Soundex code: ")
    print("Soundex code:", generate_soundex(name))

if __name__ == '__main__':
    main()

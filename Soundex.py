soundex_dict = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
}

def get_soundex_code(char):
    return soundex_dict.get(char.upper(), '')

def initialize_soundex(name):
    first_letter = name[0].upper()
    first_code = get_soundex_code(first_letter)
    return first_letter, first_code

def should_process_char(soundex, char):
    return len(soundex) < 4 and char.isalpha()

def update_soundex(soundex, prev_code, char):
    current_code = get_soundex_code(char)
    if current_code != prev_code and current_code != '':
        soundex += current_code
    return soundex, current_code

def finalize_soundex(soundex):
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not name:
        return ""

    soundex, prev_code = initialize_soundex(name)
    soundex = process_name(name, soundex, prev_code)
    return finalize_soundex(soundex)

def process_name(name, soundex, prev_code):
    for char in name[1:]:
        if should_process_char(soundex, char):
            soundex, prev_code = update_soundex(soundex, prev_code, char)
    return soundex

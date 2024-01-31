from translation_dict import english_to_morse, morse_to_english


def translateToMorse(english_string):
    morse_code = ''
    for letter in english_string:
        if letter == ' ':
            morse_code += ' / '
        else:
            morse_code += english_to_morse[letter]
            morse_code += ' '
    return morse_code


def translateToEnglish(morse_code):
    english_string = ''
    morse_code = morse_code.split()

    for code in morse_code:
        if code == '/':
            english_string += ' '
        else:
            english_string += morse_to_english[code]
    return english_string


while True:
    user_choice = input('Enter 1 to convert from English to Morse code, '
                        '2 to convert from Morse code to English, '
                        '3 to end the program: ')
    converted_output = False

    if user_choice == '3':
        print('Thank you, come again!')
        break
    elif user_choice == '1':
        english_input = input('Please enter the English sentence to convert: \n').upper()
        converted_output = translateToMorse(english_input)
    elif user_choice == '2':
        morse_input = input('Please enter the Morse code to convert: \n')
        converted_output = translateToEnglish(morse_input)

    if converted_output:
        print(f'The translated output is: \n{converted_output}')
    else:
        print('Invalid input, program ending')
        break

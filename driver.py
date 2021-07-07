from choose_from import choose_from_menu
from cipher import encode, decode, brute_force

def cipher():
    choices = ['Encode', 'Decode', 'Brute Force']

    message = input(f'\nWhat message would you like to encode/ decode? ').lower()
    method = choose_from_menu(choices, 'Would you like to Encode, Decode, or Brute Force your message? ')
    while True:
        try:
            shift = int(input(f'\nWhat number would you like to shift your message by? ').strip())
            break
        except ValueError:
            print(f'\nSorry, you may have inputed an invalid character!')

    if method == 'Encode':
        message = encode(message, shift)
        print(f'\nYour shift was: {shift}, and your message is: {message}')

    elif method == 'Decode':
        message = decode(message, shift)
        print(f'\nYour shift was: {shift}, and your message was: {message}')

    elif method == 'Brute Force':
        messages = brute_force(message)
        for shift,plaintext in messages:
            print(f'\nYour shift was: {shift}, and your message was: {plaintext}')

if __name__ == '__main__':
    cipher()
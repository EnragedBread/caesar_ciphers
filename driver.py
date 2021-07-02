from cipher import encode, decode, brute_force

def cipher():
    message = input(f'\nWhat message would you like to encode/ decode? ').lower()
    method = input(f'\nWould you like to decode, encode, or brute force your message? ').lower().strip()
    shift = int(input(f'\nWhat number would you like to shift your message by? ').lower().strip())

    if method == 'encode':
        message = encode(message, shift)
        print(f'\nYour shift was: {shift}, and your message is: {message}')

    elif method == 'decode':
        message = decode(message, shift)
        print(f'\nYour shift was: {shift}, and your message was: {message}')

    elif method == 'brute force':
        messages = brute_force(message)
        for shift,plaintext in messages:
            print(f'\nYour shift was: {shift}, and your message was: {plaintext}')

if __name__ == '__main__':
    cipher()
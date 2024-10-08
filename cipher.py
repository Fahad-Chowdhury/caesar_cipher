from ascii_art import caesar_cipher_art


def get_inputs():
    ''' Get the required inputs from the user. '''
    print(caesar_cipher_art)
    choice = ''
    while choice not in [1, 2]:
        print('Choose your option:')
        print('1. To Encrypt')
        print('2. To Decrypt')
        choice = input("Type your choice (1/2): ")
        choice = int(choice) if choice.isnumeric() else choice
    message = input("Type your message: ")
    shift_amount = ''
    while not shift_amount in range(0, 27):
        shift_amount = input("Type the shift number (0-26): ")
        shift_amount = int(shift_amount) if shift_amount.isnumeric() else shift_amount
    return choice, message, shift_amount


def ceaser(message, shift_amount, decrypt=False):
    ''' Encrypt / decrypt message by shifting each alphabetic character by 
    'shift_amount' using ascii values of characters. '''
    crypted_msg = []
    shift_amount = shift_amount * -1 if decrypt else shift_amount
    for ch in message:
        is_upper = True if ch.isupper() else False
        ascii_value = ord(ch.lower())
        if ascii_value in range(97, 123):
            shifted_value = ascii_value + shift_amount
            if decrypt and shifted_value < 97:
                shifted_value += 26
            elif shifted_value > 122:
                shifted_value -= 26
            crypted_ch = chr(shifted_value).upper() if is_upper else chr(shifted_value)
            crypted_msg.append(crypted_ch)
        else:
            crypted_msg.append(ch)
    return ''.join(crypted_msg)


def main():
    choice, message, shift_amount = get_inputs()
    if choice == 1:
        crypted_msg = ceaser(message, shift_amount)
        print(f"Here's the encrypted message: {crypted_msg}")
    if choice == 2:
        ceaser(message, shift_amount, decrypt=True)
        print(f"Here's the decrypted message: {crypted_msg}")


if __name__ == "__main__":
    main()

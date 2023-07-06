'''
SID:520154106
'''


def encode_message(message, key):
    '''
    This function gets a message and a key list, and encrpyt the message by
    replacing each charater in the message with the code in the key list.
    '''
    # ADD YOUR CODE HERE
    coded_msg = ""
    i = 0
    while i < len(message):
        j = 0
        while j < len(key):
            if message[i] == key[j][0]:
                coded_msg += key[j][1]
                break
            j += 1
        i += 1
    return coded_msg


def decode_message(message, key):
    '''
    This function gets a message and a key list, and decrpyt the message by
    replacing each code in the message with the alphabet from the key list.
    '''
    # ADD YOUR CODE HERE
    decoded_msg = ""
    i = 0
    while i < len(message):
        j = 0
        while j < len(key):
            if message[i:i + 4] == key[j][1]:
                decoded_msg += key[j][0]
                break
            j += 1
        i += 1
    return decoded_msg


def main():
    key = [['a', '1161'], ['b', '1162'], ['c', '1163'], ['d', '1164'], ['e', '1165'], ['f', '1166'], ['g', '1167'],
           ['h', '1268'], ['i', '1269'], ['j', '126a'], ['k', '126b'], ['l', '126c'], ['m', '126d'], ['n', '126e'],
           ['o', '126f'], ['p', '1370'], ['q', '1371'], ['r', '1372'], ['s', '1373'], ['t', '1374'], ['u', '1375'],
           ['v', '1376'], ['w', '1377'], ['x', '1378'], ['y', '1379'], ['z', '137a']]

    print("Welcome to crypto")
    print("Valid commands are: encrypt, decrypt and exit")
    while True:
        print("===========================================")
        task = input('Do you want to encrypt or decrypt? ')

        if task == 'encrypt':
            message = input('Enter the message to encrypt (only small letter english alphabets are allowed): ')
            encrypted = encode_message(message, key)
            print('Ciphertext of the secret message is: ', encrypted)

        elif task == 'decrypt':
            message = input('Enter the secret message to decrypt: ')
            decrypted = decode_message(message, key)
            print('Plaintext of the secret message is: ', decrypted)

        elif task == 'exit':
            print('Thank you for using our program.')
            break

        else:
            print('Invalid option: please enter encrpyt, decrypt or exit. ')


if __name__ == "__main__":
    main()
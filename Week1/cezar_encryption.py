alphabet_lower = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p',
                  'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
                  'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(message):
    encrypted_message = ""
    for i in message:
        if i == " ":
            encrypted_message += " "
        else:
            if i in alphabet_lower:
                alphabet_index = alphabet_lower.index(i)
                encrypted_message += alphabet_lower[(alphabet_index + 3) % len(alphabet_lower)]
            if i in alphabet_upper:
                alphabet_index = alphabet_upper.index(i)
                encrypted_message += alphabet_upper[(alphabet_index + 3) % len(alphabet_upper)]
    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    for i in message:
        if i == " ":
            decrypted_message += " "
        else:
            if i in alphabet_lower:
                alphabet_index = alphabet_lower.index(i)
                decrypted_message += alphabet_lower[(alphabet_index - 3) % len(alphabet_lower)]
            if i in alphabet_upper:
                alphabet_index = alphabet_upper.index(i)
                decrypted_message += alphabet_upper[(alphabet_index - 3) % len(alphabet_upper)]
    return decrypted_message


if __name__ == '__main__':
    message = input("Enter your message: ")
    encrypted_message = encrypt(message)
    print(encrypted_message)
    decrypted_message = decrypt(encrypted_message)
    print(decrypted_message)


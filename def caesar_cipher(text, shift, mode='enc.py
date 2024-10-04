def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:  # decrypt
                shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher program!")
    
    while True:
        mode = input("Would you like to encrypt or decrypt? (e/d): ").lower()
        if mode not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if mode == 'e':
            result = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {result}")
        
        again = input("Would you like to perform another operation? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Caesar Cipher program. bye!")
            break

if __name__ == "__main__":
    main()
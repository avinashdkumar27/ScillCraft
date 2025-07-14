def encrypt(text, shift):
    result= ""
    for char in text:
        if char.isupper():
            result +=chr((ord(char)+shift-65)%26+65)
        elif char.islower():
            result +=chr((ord(char)+shift-97)%26+97)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)

#Main Code
print("SkillCraft Task 1 - Caesar Cipher")
text = input("Enter text: ")
shift = int(input("Enter shift value: "))
choice = input("Do you want to encrypt or decrypt the text? (e/d): ").lower()

if choice == 'e':
    encrypted_text = encrypt(text, shift)
    print("Encrypted text:", encrypted_text)
    
elif choice == 'd':
    decrypted_text = decrypt(text, shift)
    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

# SkillCraft Task 1 - Caesar Cipher
# This code implements a simple Caesar cipher for encryption and decryption of text.
# The user can input text and a shift value, and choose whether to encrypt or decrypt the text.
# The code handles both uppercase and lowercase letters, while leaving non-alphabetic characters unchanged
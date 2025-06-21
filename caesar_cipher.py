# caesar_cipher.py
# Caesar Cipher Tool by Tarun Mehra

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Reverse the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Keep non-letter characters as they are

    return result


def brute_force_caesar(message):
    print("\n🧠 Brute Forcing Caesar Cipher (All 25 Possible Shifts):\n")
    for shift in range(1, 26):
        guess = caesar_cipher(message, shift, mode='decrypt')
        print(f"Shift {shift:2}: {guess}")


# Main program
if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool by Tarun Mehra")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute Force (Try all 25 shifts)")
    print("-------------------------------------")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        text = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (e.g. 3): "))
        encrypted = caesar_cipher(text, shift, mode='encrypt')
        print("\n✅ Encrypted Message:", encrypted)

    elif choice == '2':
        text = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value used to encrypt it: "))
        decrypted = caesar_cipher(text, shift, mode='decrypt')
        print("\n🔓 Decrypted Message:", decrypted)

    elif choice == '3':
        text = input("Enter the encrypted message: ")
        brute_force_caesar(text)

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

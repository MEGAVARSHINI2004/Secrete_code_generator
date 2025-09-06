# Function to encode a message
def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encoded_message += char  # Keep non-alphabetic characters unchanged
    return encoded_message

# Function to decode a message
def decode_message(message, shift):
    return encode_message(message, -shift)

# Function to display the menu and handle user choices
def menu():
    while True:
        print("\nSecret Code Generator Menu:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                print(f"Encoded message: {encode_message(message, shift)}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")

        elif choice == "2":
            message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                print(f"Decoded message: {decode_message(message, shift)}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main program execution
if __name__ == "__main__":
    menu()

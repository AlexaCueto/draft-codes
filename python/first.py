def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(b, 2)) for b in binary.split())

def save_binary_to_file(filename, binary_data):
    with open(filename, 'w') as file:
        file.write(binary_data)

def read_binary_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    message = input("Enter your secret message: ")
    binary_message = text_to_binary(message)
    
    filename = "secret_message.txt"
    save_binary_to_file(filename, binary_message)
    print(f"Binary message saved to {filename}")

    # Simulate opening the file later
    binary_data = read_binary_from_file(filename)
    decoded_message = binary_to_text(binary_data)

    print("\nDecoded message from file:")
    print(decoded_message)

if __name__ == "__main__":
    main()

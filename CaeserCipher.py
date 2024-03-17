def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char

    if mode == "decrypt":
        shift = -shift
    return result

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter the mode (encrypt/decrypt): ")

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
else:
    output = caesar_cipher(message, shift, mode)
    print("Output: ", output)
    
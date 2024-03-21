# Sensi Dehaarte

def encode(message):
    encoded_message = ""
    for char in message:
        encoded_message += str((int(char) + 3) % 10)
    return encoded_message


def main():
    while True:
        print("\nMenu:")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter your option: ")

        if choice == "1":
            message = input("Please enter your password to encode: ")
            encoded_message = encode(message)
            print("Your password has been encoded and stored!")
        if choice == "2":
            decoded_message = decode(encoded_message)
            print(f"The encoded password is {encoded_message}, and the original password is {decoded_message}")
        if choice == "3":
            break


if __name__ == "__main__":
    main()
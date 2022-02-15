alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(choice, cypher_text, shift_amount):
    message = []
    shift_amount = shift_amount % 26
    if choice == "encode":
        for char in cypher_text:
            if char in alphabet:
                letter_number = alphabet.index(char)
                letter_shift_number = letter_number + shift_amount
                if letter_shift_number < 26:
                    encoded_letter = alphabet[letter_shift_number]
                    message.append(encoded_letter)
                if letter_shift_number >= 26:
                    left_over = (letter_number + shift_amount) - 26
                    encoded_letter = alphabet[left_over]
                    message.append(encoded_letter)
            else:
                message.append(char)
        print(f"The encoded message is {''.join(message)}")

    if choice == "decode":
        for char in cypher_text:
            if char in alphabet:
                letter_number = alphabet.index(char)
                letter_shift_number = letter_number - shift_amount
                if letter_shift_number > 0:
                    decoded_letter = alphabet[letter_shift_number]
                    message.append(decoded_letter)
                if letter_shift_number <= 0:
                    left_over = 26 - abs((letter_number - shift_amount))
                    decoded_letter = alphabet[left_over]
                    message.append(decoded_letter)
            else:
                message.append(char)

        print(f"The decoded message is {''.join(message)}")


continue_game = True

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cypher_text=text, shift_amount=shift, choice=direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == "no":
        continue_game = False
        print("Goodbye!")

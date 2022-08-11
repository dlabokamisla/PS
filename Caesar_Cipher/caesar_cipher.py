# caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_amount, cipher_direction):
    output = ""
    # another way - if cipher_direction == "decode":
    # shift_amount *= -1

    for char in input_text:
        # symbols/space/numbers remain the same
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            # new_position = position + shift_amount
            output += new_letter
        else:
            output += char
    if cipher_direction == "encode":
        print(f"The encoded text is {output}")
    else:
        print(f"The decoded text is {output}")
    # another way print(f"The {cipher_direction}d text is {output}")


should_continue = True
# to continue encoding/decoding
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if the user enters number greater than the letters in the alphabet
    shift = shift % 26
    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye.")

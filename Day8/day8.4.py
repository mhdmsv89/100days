alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def cipher (text_i , shift_i):
#     cipher_text =""
#     for letter in text_i:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position+shift_i
#         elif direction == "decode":
#             new_position = position-shift_i
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the {direction}d message is {cipher_text} " )
#
# cipher(text_i=text, shift_i=shift)

def cesar (start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text +=char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
    if result =="no":
        should_continue = False
        print("Good bye")



# def encrypt (plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text +=new_letter
#     print(f"The encoded message is {cipher_text}")
#
# def decode (cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded message is {plain_text}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decode(cipher_text=text, shift_amount=shift)
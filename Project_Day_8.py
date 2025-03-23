alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Alternate way...if u r not willing to add limit of *if new_position > 25* :

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#This is the indirect method including step by step explanation of the process...
'''def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
         position = alphabet.index(letter)
         new_position = position + shift

         if new_position > 25:
             new_position -= 26

         encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}.")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift

        if new_position < 0:
            new_position += 26

        decrypted_text += alphabet[new_position]
    print(f"The decrypted text is {decrypted_text}")

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)'''

#This is the direct method of completion that includes summarized concept of the above written code...
def caesar(Given_text, shift_count, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_count *= -1
    for letter in Given_text:
        position = alphabet.index(letter)
        

        new_position = position + shift_count
        if cipher_direction == "decode" and shift_count < 0:
            new_position += 26
        else:
            new_position -= 26
        new_letter = alphabet[new_position]
        end_text += new_letter

    print(f"The {cipher_direction}d text is {end_text}.")
        
caesar(Given_text = text, shift_count = shift, cipher_direction = direction)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  text_list = list(text.strip(""))
  text_encoded = ""
  for char in text_list:
      current_index = alphabet.index(char)
      new_index = current_index + shift
      if new_index > 25:
                new_index = new_index - 26
      new_char = alphabet[new_index]
      text_encoded += new_char
  print(f"The encoded text is {text_encoded}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(text,shift):
  text_list = list(text.strip(""))
  text_encoded = ""
  for char in text_list:
      current_index = alphabet.index(char)
      new_index = current_index - shift
      if new_index < 0:
                new_index = 26 - new_index
      new_char = alphabet[new_index]
      text_encoded += new_char
  print(f"The decrypted text is {text_encoded}")

  

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


  
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction.lower() == "encode":
  encrypt(text,shift)
elif direction.lower() == "decode":
  decrypt(text,shift)
else:
  print("You have entered an invalid option")
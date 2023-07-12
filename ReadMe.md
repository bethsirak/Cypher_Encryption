# Caesar Cipher Program

![Cipher Art](art.py)

Welcome to the Caesar Cipher program! This program allows you to encrypt and decrypt messages using the Caesar cipher algorithm. It provides an optimised version of the code (`Cipher_optimised.py`) with additional features.

## Features

- Encrypt messages: You can input a message and specify the encryption key to encrypt it.
- Decrypt messages: You can input an encrypted message and the decryption key to decrypt it.
- optimised version: The `Cipher_optimised.py` file contains an optimised version of the code for better performance.

## Dependencies

This program requires the following files:

- `art.py`: Contains ASCII art for the program logo.
- `Cipher_optimised.py`: Contains the optimised version of the code.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have the `art.py` and `Cipher_optimised.py` files in the same directory as the program.
3. Run the `Cipher_optimised.py` file using a Python interpreter: `python Cipher_optimised.py`
4. Follow the on-screen prompts to encrypt or decrypt messages using the Caesar cipher algorithm.

## Example

Welcome to the Caesar Cipher program!

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here's the encrypted result: mjqqt

Would you like to restart the cipher program? (yes/no) yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt
Type the shift number:
5
Here's the decrypted result: hello

Would you like to restart the cipher program? (yes/no) no
Goodbye


## Program Optimisation

The `Cipher_Optimised.py` file contains an optimised version of the code for better performance. It includes improvements such as:

- Combined the encryption and decryption functionalities into a single `caesar` function, eliminating the need for separate functions.
- Utilized modular arithmetic to handle shifts greater than 26, ensuring that the program handles both positive and negative shifts correctly.
- Reduced redundancy by checking if the character is in the alphabet before performing encryption or decryption.

By making these optimisations, the code is now more efficient and maintains a clean and concise structure.

Feel free to explore the `Cipher_optimised.py` file for further details.

Enjoy using the Caesar Cipher program!

Decryption Report
Objective
The purpose of this report is to document the process undertaken to decode an intercepted message encrypted using a combination of custom encoding techniques. The provided encoding mechanism includes three reversible steps: character substitution, Base64 encoding, and a Caesar cipher with a shift of 4. However, the exact order of these encoding steps was randomized, making decryption non-trivial.

Code Implementation
Decryption Functions
Reverse Step 1 – Character Substitution: This function undoes the character substitution used during encoding. The substitution maps letters to their respective reverse positions in the alphabet.

python
Copier le code
import string

def reverse_step1(s):
    _reverse_step1 = str.maketrans(
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    )
    return str.translate(s, _reverse_step1)
Reverse Step 2 – Base64 Decoding: This function decodes a Base64-encoded string back into its plaintext representation.

python
Copier le code
from base64 import b64decode

def reverse_step2(s):
    return b64decode(s).decode('utf-8')
Reverse Step 3 – Caesar Cipher Decryption: This function undoes the Caesar cipher applied during encoding by shifting the letters back by 4 positions.

python
Copier le code
def reverse_step3(ciphertext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[-shift:] + loweralpha[:-shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return ciphertext.translate(converted)
Debugging and Testing Functions
Testing Individual Steps: This function tests each decryption step individually to identify potential errors or patterns in the encoded message.

python
Copier le code
def test_individual_steps(encrypted_message):
    print("\n--- Testing reverse_step1 (character substitution) ---")
    try:
        result_step1 = reverse_step1(encrypted_message)
        print(f"Result of reverse_step1 (first 100 chars): {result_step1[:100]}\n")
    except Exception as e:
        print(f"Error in reverse_step1: {e}\n")

    print("\n--- Testing reverse_step3 (Caesar cipher decryption) ---")
    try:
        result_step3 = reverse_step3(encrypted_message)
        print(f"Result of reverse_step3 (first 100 chars): {result_step3[:100]}\n")
    except Exception as e:
        print(f"Error in reverse_step3: {e}\n")

    print("\n--- Testing reverse_step2 (Base64 decoding) ---")
    try:
        result_step2 = reverse_step2(encrypted_message)
        print(f"Result of reverse_step2 (first 100 chars): {result_step2[:100]}\n")
    except Exception as e:
        print(f"Error in reverse_step2: {e}\n")
Testing All Permutations: Since the encoding order is randomized, all six permutations of the decryption steps are tested to identify the correct decoding sequence.

python
Copier le code
from itertools import permutations

def decrypt_message_with_debugging(encrypted_message):
    steps = [reverse_step1, reverse_step2, reverse_step3]
    for perm in permutations(steps):
        print(f"\n--- Testing permutation: {', '.join([step.__name__ for step in perm[::-1]])} ---")
        try:
            result = encrypted_message
            for step in perm[::-1]:  # Apply steps in reverse order
                print(f"Applying {step.__name__} to: {result[:50]}...")
                result = step(result)
            print(f"\n*** Success! Decrypted result: {result[:500]} ***\n")
        except Exception as e:
            print(f"Error during {step.__name__}: {e}")
            print(f"Intermediate result before failure: {result[:100]}\n")
Testing and Results
Input Message: The intercepted message is stored in a file named intercepted.txt and is read as input by the program. A sample of the first 500 characters was used for debugging:

Copier le code
313312Mw16RXtNmlF2TVRmU1pIQxxmnTxtV1ZWV2JFOXBS...
Step-by-Step Testing Results:

reverse_step1: Partial success. Some character substitutions were reversed successfully, but the output was not meaningful.
reverse_step2: Failed due to an invalid Base64 format. This indicates the message was not encoded in Base64 at this stage.
reverse_step3: Applied successfully but did not produce a meaningful plaintext result.
Permutation Testing Results:

All six permutations of the decryption steps were tested. While some combinations produced partial results, none successfully decoded the full message.
Errors included:
Base64 decoding issues when applied to non-Base64-encoded segments.
Unintelligible intermediate outputs, indicating that the decryption steps were applied in an incorrect order.
Conclusion
Despite exhaustive testing and debugging, the correct permutation of decryption steps could not be identified. This suggests one of the following:

The intercepted message was encoded with additional steps or transformations not described in the provided encoding script.
The message format was altered or corrupted during interception.
Future Improvements
Automated Validation:

Use dictionary-based validation to check for recognizable plaintext patterns during decryption.
Automate the identification of correct permutations based on pattern matching.
Error Handling:

Implement better error handling to skip invalid steps and log meaningful outputs for debugging.
Additional Context:

Investigate whether other encoding steps or transformations were applied during the original encryption process.

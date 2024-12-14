import string
from base64 import b64decode

# Reverse step1 (character substitution)
def reverse_step1(s):
    _reverse_step1 = str.maketrans(
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    )
    return str.translate(s, _reverse_step1)

# Reverse step2 (Base64 decoding)
def reverse_step2(s):
    return b64decode(s).decode('utf-8')

# Reverse step3 (Caesar cipher decryption)
def reverse_step3(ciphertext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[-shift:] + loweralpha[:-shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return ciphertext.translate(converted)

# Test individual steps
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

# Test all permutations of decryption steps
def decrypt_message_with_debugging(encrypted_message):
    steps = [reverse_step1, reverse_step2, reverse_step3]
    from itertools import permutations
    for perm in permutations(steps):
        print(f"\n--- Testing permutation: {', '.join([step.__name__ for step in perm[::-1]])} ---")
        try:
            result = encrypted_message
            for step in perm[::-1]:  # Apply steps in reverse order
                print(f"Applying {step.__name__} to: {result[:50]}...")  # Display first 50 chars for context
                result = step(result)
            print(f"\n*** Success! Decrypted result: {result[:500]} ***\n")
        except Exception as e:
            print(f"Error during {step.__name__}: {e}")
            # Save intermediate results even if the step fails
            print(f"Intermediate result before failure: {result[:100]}\n")

if __name__ == "__main__":
    # Load the intercepted message
    with open('intercepted.txt', 'r') as f:
        intercepted_message = f.read().strip()

    # Test a subset of the message to simplify debugging
    sample = intercepted_message[:500]  # Use only the first 500 characters for debugging

    print("\n======================== INDIVIDUAL STEP TESTS ========================")
    test_individual_steps(sample)

    print("\n======================== PERMUTATION TESTS ========================")
    decrypt_message_with_debugging(sample)


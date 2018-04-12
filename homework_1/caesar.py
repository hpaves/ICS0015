import string

# define what alphabet means
# this method has a problem in that it skips over the umlauts
alphabet = string.ascii_lowercase

# read input from the file for testing purposes
def read_file():
    """Reads from a file."""
    with open('text_garbled') as file_contents:
        text = file_contents.read()
        return(text)

# ask for method
def ask_method():
    while True:
        method = input("Encrypt or decrypt? (e or d): ")
        if method.lower() not in ('e', 'd'):
            print("Invalid choice.")
        else:
            return method

# ask for input
def ask_text():
    while True:
        text = input("Please enter the message: ")
        if len(text) == 0:
            continue
        else:
            return text

# ask for shift
def ask_shift():
    while True: # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659
        try:
            shift = int(input("Please enter the shift (0-25): "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue


        if shift < 0:
            print("Not within range.")
            continue
        elif shift > 25:
            print("Not within range.")
            continue
        else:
            #shift was successfully parsed!
            #we're ready to exit the loop.
            return shift

# encrypt
def caesar(text,shift):
    """Applies the Caesar cypher.""" # from help with Python-Narrative-Journey from Udemy
    # placeholder
    encrypted_text = list(range(len(text)))

    # shifted alphabet
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i,letter in enumerate(text.lower()):
        
        # check punctuation
        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter
    
    return ''.join(encrypted_text)

# decrypt
def uncaesar(text,shift):
    """Deapplies the Caesar cypher.""" # from help with Python-Narrative-Journey from Udemy
    # placeholder
    decrypted_text = list(range(len(text)))

    # shifted alphabet
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i,letter in enumerate(text.lower()):
        
        # check punctuation
        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter
    
    return ''.join(decrypted_text)


if __name__ == "__main__":
    method = ask_method()
    text = ask_text()
    shift = ask_shift()
    if method == 'e':
        print(caesar(text,shift))
    elif method == 'd':
        print(uncaesar(text,shift))
    else:
        print('You found a bug. Make a pull request if you figure out what it was.')

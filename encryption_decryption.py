from cryptography.fernet import Fernet

key = Fernet.generate_key()

msg = "beans".encode()

fernet = Fernet(key)

encrypted_msg = fernet.encrypt(msg)

decrypted_msg = fernet.decrypt(encrypted_msg)

print("Your file:", encrypted_msg)
print("To decrypt your file, say the secret phrase.")

secret_phrase = "helix"
tries = 0
max_tries = 3

while True:
    phrase_input = input("Enter phrase: ").lower()

    if phrase_input != secret_phrase:
        print("Wrong phrase.")
        tries = tries + 1
        if tries == max_tries:
            print("Out of tries!")
            break
    elif phrase_input == secret_phrase:
        print("Correct phrase! File decrypted.")
        print(decrypted_msg)

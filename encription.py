import random
import string

def main():

    chars =" " + string.punctuation + string.digits +string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    print(f"the first {chars}")
    print(f" after shuffle {key}")
    #encrypt
    given_text= input("enter the message")
    cipher_text = ""
    for letter in given_text:
        index = chars.index(letter)
        cipher_text += key[index]
    print(f"encrypted message{cipher_text}")
    #decrypt
    encrypted = input("enter your encrypted message")
    actual_message= ""
    for letter in encrypted:
        index = key.index(letter)
        actual_message += chars[index]
    print(f"the decrpted message is {actual_message}")
if __name__=="__main__":
    main()
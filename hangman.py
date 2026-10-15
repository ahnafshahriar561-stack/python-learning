#dictionary jeta 0 theke 6
import random


words =("apple","pineapple","banana","coconut","grape","orange")
hangman_art={0:("     ",
                "     ",
                "     "),

             1: ("  O   ",
                 "     ",
                 "     "),

             2: ("  O   ",
                 "  |   ",
                 "     "),

             3: ("  0   ",
                 " /|   ",
                 "     "),

             4: ("  O   ",
                 " /|\\    ",
                 "     "),

             5: ("  O   ",
                 " /|\\    ",
                 " /    "),
             6:("   O   ",
                 " /|\\    ",
                 "  /\\    "),
             }
def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print (line)
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_running = True
    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input(("enter a letter")).lower()
        if len(guess) != 1 or not guess.isalpha() :
            print("you can guess exactly one letter")
            continue

        if guess in guessed_letter:
            print("You already guessed that")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:

                    hint[i] = guess
                    guessed_letter.add(guess)
        else:
            wrong_guess += 1
            guessed_letter.add(guess)
        if '_' not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("you win")
            is_running = False
        if wrong_guess == 6:
            print("you lose")
            display_man(wrong_guess)
            is_running =False



if __name__=='__main__':
    main()
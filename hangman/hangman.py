import random
from hangman_words import word_list
from hangman_arts import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

correct_letters = []
guessed_letters = []

is_game_over = False
while not is_game_over:

    print(f"********{lives}/6 LIVES LEFT********")

    guess = input("Make your guess: ").lower()
    display = ""

    if guess in guessed_letters:
        print(f"you have guesses {guess} before!")

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life. ")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    if lives == 0:
        is_game_over = True
        print(chosenword)
        print("you loose!")

    if lives == 0:
        is_game_over = True

    if "_" not in display:
        Game_over = True
        print("You win!")

    print(stages[::-1][lives])
    print(display)
    print(f"###### you have {lives} left! ######")



# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.




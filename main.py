import random
from word_list import word_list
from art import stages, logo

lives = 6

word = random.choice(word_list)

print(f"For debugging, the word is {word}")

print(logo)

word = list(word)

display = []

for letter in word:
    display.append("_")

print(display)

guessed_letters = []

while "_" in display:

    print(stages[lives])

    if lives == 0:
        print(f"Game Over! The word was {''.join(word)}")
        break
    
    guess = ''
    while len(guess) != 1 or not guess.isalpha():
        guess = input('Guess a letter: ').casefold()

    if guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess not in word:
            print(f"{guess} is not in the word.")
            lives -= 1
    else:
        print(f"You have already guessed {guess}")

    for x in range(len(word)):
        if word[x] in guessed_letters:
            display[x] = word[x]
        else:
            display[x] = "_"

    print(display)
else:
    print("Well done! You guessed the word.")
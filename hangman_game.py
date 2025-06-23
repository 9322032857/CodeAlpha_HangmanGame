import random

# Step 1: Predefined list of words
words = ["apple", "banana", "grape", "mango", "peach"]

# Step 2: Randomly choose one word
word = random.choice(words)

# Step 3: Create placeholders
guessed_word = ['_'] * len(word)

# Step 4: Set allowed wrong attempts
lives = 6

# Step 5: Track guessed letters
guessed_letters = []

# Step 6: Game loop
while lives > 0 and '_' in guessed_word:
    print("\nCurrent word: " + ' '.join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

# Step 7: Result
if '_' not in guessed_word:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)

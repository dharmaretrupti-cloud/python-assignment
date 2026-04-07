


from random import sample

x = ["java", "nodejs", "react", "angular"]
score = 0

for word in x:
    scrambled = ''.join(sample(word, len(word)))
    print("Scrambled word:", scrambled)
    guess = input("Your guess: ")
    if guess == word:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct word was:", word)

print("Final score:", score)


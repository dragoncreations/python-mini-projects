print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time!")
    exit()

print("Great! Let's start the quiz.")
score = 0

answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

answer = input("What is 5 + 7? ")
if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 12.")

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Jupiter.")

answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is H2O.")

print(f"You got {score} out of 4 questions correct!")
print(f"You got {(score / 4) * 100}%.")
print("Thanks for playing the Quiz Game!")
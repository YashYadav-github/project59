x = 74
num_of_guesses = 1
print("Welcome to guess the number")
print("Number of guesses is limited to only 6 times: ")
while (num_of_guesses <= 6):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 74:
        print("Please Increase the number")
    elif guess_number > 74:
        print("Please Decrease the number")
    else:
        print("You win🎉 🎉 ")
        print(num_of_guesses, "guesses you took to finish.")
        break
    print(6 - num_of_guesses,"guesses left")
    num_of_guesses = num_of_guesses + 1

if(num_of_guesses > 9):
    print("Game Over:( Try again")
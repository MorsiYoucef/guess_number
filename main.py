
import random
def computer_guess(x):
    low = 1
    high = 10
    guess = random.randint(1, 10)
    print(guess)

    K = 'p'  # Initialize K to 'P'

    while (guess != x or guess==x) and (K == 'p' or K == 'g'):  # Corrected variable name 'K' and 'k' to 'K'
        if guess > x:
            K = str(input("Too high (G),Too Loo Low (P), Correct (C): "))
            high = guess - 1

        elif guess < x:
            K = str(input("Too high (G),Too Loo Low (P), Correct (C): "))

            low = guess + 1  # Corrected low adjustment
        else:

            K = str(input("Too high (G),Too Loo Low (P), Correct (C): "))
            if K!='c':
                print("must be the correct number!!!")
                break

            s = f"Congratulations, the number is {guess}"
            print(s)
            break  # Exit the loop if the guess is correct

        guess = random.randint(low, high)
        print(guess)

computer_guess(x=int(input("the number is :")))


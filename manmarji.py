  

import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100 for the first level
computer = random.randint(1, 100)

# Ask the player to input their initial money for the game
money = int(input("Enter your money :$ "))

# Initialize the number of attempts to 0
attempts = 0

# Start a loop that allows up to 10 attempts for the first level
while attempts <= 10:
    # Ask the player to guess the number for the first level
    guess = int(input("guess the number for first level : "))
    
    # Increase the number of attempts
    attempts += 1
    
    # Check if the guess is higher than the computer's number
    if guess > computer:
        print("Hint: guess lower number")  # Tell the player to guess a lower number
    # Check if the guess is lower than the computer's number
    elif guess < computer:
        print("Hint: guess upper number")  # Tell the player to guess a higher number
    # If the guess is correct, the player wins the first level
    else:
        print(f"You have won! first level")
        
        # Ask the player if they want to proceed to the second level
        choose = input("Do you want to play for 2nd level (Y/N) : ")
        
        # If the player chooses to continue to the second level
        if choose == "Y":
            # Generate a random number between 101 and 150 for the second level
            computer = random.randint(101, 150)
            
            # Initialize the number of attempts for the second level to 0
            attempt2 = 0
            
            # Start a loop that allows up to 7 attempts for the second level
            while attempt2 <= 7:
                # Ask the player to guess the number for the second level
                guess = int(input("guess the number : "))
                
                # Increase the number of attempts for the second level
                attempt2 += 1
                
                # Check if the guess is higher than the computer's number
                if guess > computer:
                    print("Hint: guess lower number")  # Tell the player to guess a lower number
                # Check if the guess is lower than the computer's number
                elif guess < computer:
                    print("Hint: guess upper number")  # Tell the player to guess a higher number
                # If the guess is correct, the player wins the second level
                else:
                    print("You have won.")
                    
                    # Ask the player if they want to proceed to the final level
                    choose = input("Do you want to play for final level (Y/N) : ")
                    
                    # If the player chooses to continue to the final level
                    if choose == "Y":
                        # Generate a random number between 151 and 200 for the final level
                        computer = random.randint(151, 200)
                        
                        # Initialize the number of attempts for the final level to 0
                        attempt3 = 0
                        
                        # Start a loop that allows up to 5 attempts for the final level
                        while attempt3 <= 5:
                            # Ask the player to guess the number for the final level
                            guess = int(input("guess the number : "))
                            
                            # Increase the number of attempts for the final level
                            attempt3 += 1
                            
                            # Check if the guess is higher than the computer's number
                            if guess > computer:
                                print("Hint: guess lower number")  # Tell the player to guess a lower number
                            # Check if the guess is lower than the computer's number
                            elif guess < computer:
                                print("Hint: guess upper number")  # Tell the player to guess a higher number
                            # If the guess is correct, the player wins the final level
                            else:
                                print(f"Congratulations! You have won in final level: got prize $ {5 * money}")
                                break  # End the game if the player wins
                            
                            
                            if attempt3 > 5:   # If the player uses all 5 attempts, end the game
                                print("game over")
                            break    
                    
                    
                    elif choose == "N":   # If the player chooses not to play the final level, they win a smaller prize
                        print(f"You have won prize $ {3 * money}")
                        break
                
                
                if attempt2 > 7:   # If the player uses all 7 attempts in the second level, end the game
                    print("game over")
                break
        
        
        elif choose == "N":     # If the player chooses not to play the second level, they win a smaller prize
            print(f"You have won prize $ {2 * money}")
            break
    
    
    if attempts >= 10:   # If the player uses all 10 attempts in the first level, end the game
        print("game over")
        break




       




           
print('Prof\"iyanuology\n@@@@@@@@@@\n#################')

import random

print('ROCK PAPER SCISSIOR GAME! \n' + 
        'Game Rules \n' +
        'Rock vs Paper --> Paper wins \n' +
        'Rock vs Scissior --> Rock wins \n' +
        'Paper vs Scissor --> Scissor wins \n')

while True:
    print('Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor')

    choice=int(input('Enter you choice: '))

    while choice>3 or choice<1:
        choice=int(input('Enter a valid choice please: '))
        
    if choice==1:
            choice_name='Rock'
    elif choice==2:
            choice_name='Paper'
    else:
            choice_name='Scissor'
    
    print('User choice is: ', choice_name)
    print('Now its computers turn!')

    comp_choice=random.randint(1,3)
    while comp_choice== choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'
    print("Computer choice is: ",comp_choice_name)
    print(choice_name,' VS ',comp_choice_name)

    
    if choice==comp_choice:
        print('Draw', end='')
        result='Draw'
    
    if (choice==1 and comp_choice==2):
        print('Paper wins: ',end='')
        result='Paper'
    elif(choice==2 and comp_choice==1):
        print('Paper wins:', end='')
        result='Paper'

    if (choice==1 and comp_choice==3):
        print('Rock wins: ',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins: ',end= "")
        result='Rock'

    if (choice==2 and comp_choice==3):
        print('Scissors wins: ',end="")
        result='Scissor'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins: ',end="")
        result='Scissor'
    
    if result == 'Draw':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")

    else:
        print("<== Computer wins ==>")

    answer = input('Do you want to play again? (Y/N): ')
    if answer =='n':
        print("Thanks for playing")
        break
        
    else:
        continue


##############################################
print('new option\'s ')
### Rock-Paper-Scissors Game in Python

# To create a Rock-Paper-Scissors game that allows the player to compete against the computer, follow these steps:

# ---

# ### **Step-by-Step Implementation**

# 1. **Import the `random` module:**
#    - To allow the computer to randomly select between Rock, Paper, and Scissors.

# 2. **Define the rules:**
#    - Rock beats Scissors.
#    - Scissors beat Paper.
#    - Paper beats Rock.

# 3. **Get the user's input:**
#    - Allow the player to choose Rock, Paper, or Scissors.

# 4. **Generate the computer's choice:**
#    - Use the `random.choice()` method to select one of the options.

# 5. **Compare the inputs:**
#    - Determine the winner based on the rules.

# 6. **Handle invalid inputs:**
#    - Ensure the user inputs valid choices (Rock, Paper, or Scissors).

# 7. **Repeat the game:**
#    - Use a loop to allow multiple rounds.

# ---

# ### **Code Example**

# ```python
import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'Rock', 'Paper', or 'Scissors' to play. Type 'quit' to exit.")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        # Get user input
        user_choice = input("Enter your choice: ").capitalize()
        
        # Exit condition
        if user_choice == "Quit":
            print("Thanks for playing!")
            break
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
        
        # Generate computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            print("You win!")
        else:
            print("You lose!")
        
        print()  # Blank line for better readability

# Run the game
rock_paper_scissors()

# ### **How It Works**

# 1. **User Input:**
#    - The user enters their choice, which is converted to a capitalized string for consistency.

# 2. **Computer's Choice:**
#    - The computer randomly selects from `["Rock", "Paper", "Scissors"]`.

# 3. **Winner Determination:**
#    - Using conditional statements, the program determines if the user won, lost, or tied.

# 4. **Invalid Input Handling:**
#    - If the user enters anything other than Rock, Paper, or Scissors, they are prompted to try again.

# 5. **Game Loop:**
#    - The game runs in a loop until the user types `quit`.

# ---

# ### **Sample Output**

# ```
# Welcome to Rock-Paper-Scissors!
# Instructions: Type 'Rock', 'Paper', or 'Scissors' to play. Type 'quit' to exit.

# Enter your choice: Rock
# Computer chose: Scissors
# You win!

# Enter your choice: Paper
# Computer chose: Rock
# You win!

# Enter your choice: Scissors
# Computer chose: Scissors
# It's a tie!

# Enter your choice: quit
# Thanks for playing!
# ```

# ---

# ### **Possible Enhancements**

# 1. **Scoring System:**
#    - Track the number of wins, losses, and ties.

# 2. **Multiple Rounds:**
#    - Allow the player to set the number of rounds they want to play.

# 3. **Enhanced Input Handling:**
#    - Accept lowercase inputs and strip whitespace.

# 4. **UI Enhancements:**
#    - Use emojis or colored text to make the game more engaging.

# This code provides a simple yet functional Rock-Paper-Scissors game with robust input handling and clear instructions.
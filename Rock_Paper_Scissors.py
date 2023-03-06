import random

# Define the valid moves
moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Set the initial scores to zero
player_score = 0
computer_score = 0

# Loop until one player reaches five wins
while player_score < 5 and computer_score < 5:
    # Get the user's move
    player_move = input("Choose rock, paper, or scissors: ").lower()

    # Make sure the user's move is valid
    while player_move not in moves.keys():
        player_move = input("Invalid move. Choose rock, paper, or scissors: ").lower()

    # Generate the computer's move
    computer_move = random.choice(list(moves.keys()))

    # Determine the winner of this round
    if moves[player_move] == computer_move:
        print("You win!")
        player_score += 1
    elif moves[computer_move] == player_move:
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie!")

    # Print the current scores
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

# Determine the overall winner
if player_score > computer_score:
    print("You win the game!")
else:
    print("Computer wins the game!")

# Ask if the user wants to play again
play_again = input("Play again? (y/n)").lower()
while play_again == "y":
    # Reset the scores
    player_score = 0
    computer_score = 0

    # Play the game again
    while player_score < 5 and computer_score < 5:
        player_move = input("Choose rock, paper, or scissors: ").lower()
        while player_move not in moves.keys():
            player_move = input("Invalid move. Choose rock, paper, or scissors: ").lower()
        computer_move = random.choice(list(moves.keys()))

        if moves[player_move] == computer_move:
            print("You win!")
            player_score += 1
        elif moves[computer_move] == player_move:
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print("You win the game!")
    else:
        print("Computer wins the game!")

    play_again = input("Play again? (y/n)").lower()

print("Thanks for playing!")

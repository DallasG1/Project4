import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


value = roll()
# print(f"You rolled a {value}.")

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

# print(players)

max_score = 50
players_scores = [0 for _ in range(players)]

print(players_scores)

while max(players_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn.\n")
        print(f"Your total score is : {players_scores[player_index]}")
        current_score = 0
        while True:

            should_roll = input("Do you want to roll? (y/n): ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print("You rolled a 1, you lose your turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}.")

            print(f"Your current score is: {current_score}.")
        players_scores[player_index] += current_score
        print(f"Your total score is:, {players_scores[player_index]}")
max_score = max(players_scores)
winner_index = players_scores.index(max_score)
print(f"\n Player {winner_index + 1} wins with a score of {max_score}!")

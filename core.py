import random

class Player:
    def __init__(self, name):
        self.name = name
        self.rows = {
            "row 1": [0, 0, 0],
            "row 2": [0, 0, 0],
            "row 3": [0, 0, 0]
        }
        
    def print_rows(self):
        for row in self.rows:
            print(f"{row}: {self.rows[row]}")
        return
    
    def score_row(self, row='row 1'):
        score = 0
        dice_values = self.rows[row]

        occurrences = {}
        for die in dice_values:
            occurrences[die] = occurrences.get(die, 0) + 1

        for die in dice_values:  # Use set to iterate over unique die values
            count = occurrences[die]
            if count == 2:
                score += die * 2
            elif count >= 3:
                score += die * 3
            else:
                score += die

        return score

    def score_board(self):
        total_score = 0
        for row_name in self.rows.keys():
            total_score += self.score_row(row_name)
        return total_score
    
    def assign(self, die_value=1):
        empty_rows =[]
        for row in self.rows:
            for die in self.rows[row]:
                if die == 0:
                    empty_rows.append(row)
                    break
        while True:
            print("")
            selected_row = input(f'Which row would you like to place the {die_value} in? ({empty_rows})').strip().lower()

            if selected_row in empty_rows:
                for i in range(len(self.rows[selected_row])):
                    if self.rows[selected_row][i] == 0:
                        self.rows[selected_row][i] = die_value
                        return  # Exit the loop once a valid row is found and die is assigned
            else:
                print("Incorrect row selected, please try again.")

def roll_die():
    die = random.randint(1,6)
    return die

def play_game(player):
    while any(0 in row for row in player.rows.values()):
        die_value = roll_die()
        player.assign(die_value)
    print("All rows filled. Final score:", player.score_board())
    player.print_rows()

def auto_game(player):
    while any(0 in row for row in player.rows.values()):
        for row_name, row_values in player.rows.items():
            if 0 in row_values:
                die_value = roll_die()
                empty_indices = [i for i, value in enumerate(row_values) if value == 0]
                selected_index = random.choice(empty_indices)
                player.rows[row_name][selected_index] = die_value
    print("All rows filled. Final score:", player.score_board())
    player.print_rows()

def versus_game_mode(player):
    bot = Player('Bot')
    while any(0 in row for row in player.rows.values()) or any(0 in row for row in bot.rows.values()):
        # Player's turn
        print("\nPlayer's Turn:")
        player_die = roll_die()
        player.assign(player_die)
        print(f"Player rolled: {player_die}")

        # Bot's turn
        print("\nBot's Turn:")
        bot_die = roll_die()
        empty_bot_rows = [row for row in bot.rows if 0 in bot.rows[row]]
        if empty_bot_rows:
            bot_row = random.choice(empty_bot_rows)
            bot.rows[bot_row][bot.rows[bot_row].index(0)] = bot_die
        else:
            print("Bot has no empty rows left.")
            break

        print(f"Bot rolled: {bot_die}")

        # Check if player's or bot's die value matches opponent's row and remove opponent's dice
        for row_name in player.rows.keys():
            if player.rows[row_name] != [0, 0, 0] and bot.rows[row_name] != [0, 0, 0]:
                for i in range(3):
                    if player.rows[row_name][i] == bot.rows[row_name][i]:
                        bot.rows[row_name][i] = 0

        # Display both boards
        print("Player's Board:".ljust(30), "Bot's Board:")
        for row_name in player.rows.keys():
            print(f"{row_name}: {player.rows[row_name]}".ljust(30), end=" ")
            print(f"{row_name}: {bot.rows[row_name]}")

    # Display final scores
    player_score = player.score_board()
    bot_score = bot.score_board()

    print("\nPlayer's Final Score:", player_score)
    print("Bot's Final Score:", bot_score)

    if player_score > bot_score:
        print("Congratulations! You win!")
    elif player_score < bot_score:
        print("You lose! Better luck next time.")
    else:
        print("It's a tie!")

test = Player("Test")
versus_game_mode(test)
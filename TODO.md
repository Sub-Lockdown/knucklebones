Current status: 
* class player contains someone's board and the actions
* class player.__init__ takes a name and gives them an empty board of three rows
* class player.print_rows prints out all three rows
* class player.roll rolls out a six sided die
* class player.assin takes a die value, and verifies which rows are empty and confirms if able to place the die there
* iterating through the board seems to be something that needs to be it's own def, as it comes up in several game actions
* scoring of the rows, including doubles and triples
* making a game state, and verifying that it ends when board is full
* making an opponent, randomly having it place dice, comparing score at full board

TODO:
* having dice eliminate the opposite board
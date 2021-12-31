import math
import random 

class Player: 
    def __init__(self, letter) -> None:
        self.letter = letter #letter is o or x

    # we want all players to get their next move given a game
    def get_move(self, game) -> None:
        pass

class RandomComputerPlayer(Player): 
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> None:
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> None:
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we're going to check that this a correct value by trying to cast
            # it to integer, and if it's not, then we say its invalid
            # if that spot is not avaliable on the board, we also say it invalid
            try: 
                val = int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square = True # thành công
            except ValueError:
                print('Invalid vale, try again.')

        return val
from boggle_board_randomizer import randomize_board
import ex12_utils as utils


class Boggel_Model():
    def __init__(self, file_path):
        self.board = randomize_board()
        self.words = utils.load_words_dict(file_path)
        self.score = 0
        self.current_str = ""
        self.guessed_words = []
        self.current_guess = []

    def check_path(self, path):
        return utils.is_valid_path(self.board, path, self.words)

    def place_guess(self):
        word = self.check_path(self.current_guess)
        if word is not None:
            self.score += len(word) ** 2
            self.guessed_words.append(word)
            self.current_guess = []
            self.current_str = ""
        else:
            self.current_guess = []
            self.current_str = ""

    def choose_cube(self, cube_coord):
        self.current_guess.append(cube_coord)
        self.current_str += self.board[cube_coord[0]][cube_coord[1]]









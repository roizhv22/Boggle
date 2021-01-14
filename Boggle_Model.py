import ex12_utils as utils


class Boggle_Model():
    def __init__(self, file_path, board):
        self.board = board
        self.dict_of_letters_and_coords = {}
        self.create_ltr_and_coord_dict()
        self.words = utils.load_words_dict(file_path)
        self.score = 0
        self.current_str = ""
        self.guessed_words = []
        self.current_guess = []

    def check_path(self, path):
        return utils.is_valid_path(self.board, path, self.words)

    def create_ltr_and_coord_dict(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                val = self.board[i][j]
                self.dict_of_letters_and_coords.update({(i, j): val})

    def return_all_neighbors(self, cube_coord):
        row = cube_coord[0]
        col = cube_coord[1]
        lst_of_neighbors = []

        if row == 0:
            if col == 0:
                lst_of_neighbors += [(row + 1, col), (row + 1, col + 1),
                                     (row, col + 1)]
                return lst_of_neighbors
            if col == 3:
                lst_of_neighbors += [(row + 1, col), (row + 1, col - 1),
                                     (row, col - 1)]
                return lst_of_neighbors
            else:
                lst_of_neighbors += [(row + 1, col), (row + 1, col + 1),
                                     (row, col + 1), (row, col - 1),
                                     (row + 1, col - 1)]
                return lst_of_neighbors

        elif row == 3:
            if col == 0:
                lst_of_neighbors += [(row - 1, col), (row - 1, col + 1),
                                     (row, col + 1)]
                return lst_of_neighbors
            if col == 3:
                lst_of_neighbors += [(row - 1, col), (row - 1, col - 1),
                                     (row, col - 1)]
                return lst_of_neighbors
            else:
                lst_of_neighbors += [(row - 1, col), (row - 1, col + 1),
                                     (row, col + 1), (row, col - 1),
                                     (row - 1, col - 1)]
                return lst_of_neighbors

        else:
            lst_of_neighbors += [(row - 1, col), (row - 1, col + 1),
                                 (row, col + 1), (row, col - 1),
                                 (row - 1, col - 1), (row + 1, col + 1),
                                 (row + 1, col), (row + 1, col - 1)]
            return lst_of_neighbors

    def place_guess(self):
        word = self.check_path(self.current_guess)
        if word is not None:
            self.score += len(word) ** 2
            self.current_guess = []
            return True, word
        else:
            self.current_guess = []
            return False, None

    def choose_cube(self, cube_coord):
        self.current_guess.append(cube_coord)
        self.current_str += self.board[cube_coord[0]][cube_coord[1]]

    def get_hint(self):
        hints = []
        for i in range(3, 7):
            a = utils.find_length_n_words(i, self.board, self.words)
            if not a:
                continue
            else:
                hints.append(a[0][0])
        return hints






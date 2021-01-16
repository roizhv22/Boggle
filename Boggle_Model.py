import ex12_utils as utils


class Boggle_Model:
    """
    The boggle model class. This class includes some of the logic on the game.
    """
    def __init__(self, file_path, board):
        """
        Constructor method.
        :param file_path: words file path.
        :param board: board (2D matrix).
        """
        self.board = board
        self.dict_of_letters_and_coords = {}
        self.create_ltr_and_coord_dict()
        self.words = utils.load_words_dict(file_path)
        self.score = 0
        self.current_str = ""
        self.guessed_words = []
        self.current_guess = []

    def check_path(self, path):
        """
        Checks if path is valid via the utils function.
        :param path: list of coords
        :return:
        """
        return utils.is_valid_path(self.board, path, self.words)

    def create_ltr_and_coord_dict(self):
        """
        A method that create dict of ltr and coords of a given board.
        :return: None.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                val = self.board[i][j]
                self.dict_of_letters_and_coords.update({(i, j): val})

    def return_all_neighbors(self, cube_coord):
        """
        A method that returns all the neighbors of a given coord on the board.
        :param cube_coord: cube coordinate
        :return: list of neighbors.
        """
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
        """
        Place guess is a method that checks if a given guess is correct and
        perform changes accordingly.
        :return: a tuple of a bool val and the word or None.
        """
        word = self.check_path(self.current_guess)
        if word is not None:
            self.score += len(word) ** 2
            self.current_guess = []
            return True, word
        else:
            self.current_guess = []
            return False, None

    def choose_cube(self, cube_coord):
        """
        editing the guess str.
        :param cube_coord: a cube coordinate
        :return: None
        """
        self.current_guess.append(cube_coord)
        self.current_str += self.board[cube_coord[0]][cube_coord[1]]

    def get_hint(self):
        """
        generate a small hints list from the find_length_n_words function of
        the utils script.
        :return: hints list.
        """
        hints = []
        for i in range(3, 7):
            a = utils.find_length_n_words(i, self.board, self.words)
            if not a:
                continue
            else:
                hints.append(a[0][0])
        return hints

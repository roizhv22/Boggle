from boggle_board_randomizer import *


def load_words_dict(file_path):
    """
    Loading all the relevant words from a file to a dict.
    :param file_path: words file path.
    :return: a dictionary with words as key and True as value.
    """
    words_dict = {}
    f = open(file_path, "r")
    for line in f.readlines():
        words_dict[line[:-1]] = True
    f.close()
    return words_dict


def is_word_valid(word, words):
    """
    A function that checks if a given word in the word dict that was given.
    :param word: str
    :param words: word dict
    :return: bool value.
    """
    if word in words.keys():
        return True


def is_valid_path(board, path, words):
    """
    This function checks if the path that was given is valid, by checking if
    the word that is being created by the path and board in the words dict.
    :param board: a 2D matrix representing the playing board.
    :param path: a list of coords on the board.
    :param words: words dict.
    :return: The word if on the dict or None.
    """
    word = ""
    used_coord = []
    if check_if_path_is_valid(path):
        for coord in path:
            if coord in used_coord:
                return None
            letter = board[coord[0]][coord[1]]
            word += letter
            used_coord.append(coord)
        if word in words:
            return word
        else:
            return None
    else:
        return None


def check_if_path_is_valid(path):
    """
    helepr function that check if a given path is valid by the given
    instructions.
    :param path: list of coords
    :return: Bool value
    """
    for i in range(1, len(path)):
        first_row, first_col = path[i - 1]
        sec_row, sec_col = path[i]
        if abs(first_row - sec_row) > 1 or abs(first_col - sec_col) > 1:
            return False
    return True


def find_length_n_words(n, board, words):
    """
    Recursive function that find all the n lengthened words that are currently
    on the board. Due to high number of calculations that is needed,
    running time might be high.
    :param n: length of a general word
    :param board: 2D matrix representing the playing board.
    :param words: words dict.
    :return:
    """
    letters_dict = dict()
    for row in range(len(board)):
        for col in range(len(board[0])):
            letters_dict[(row, col)] = board[row][col]
    all_words = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            _find_length_helper(letters_dict, n, board, words, [(i, j)],
                                all_words, i, j, letters_dict[(i, j)])
    return all_words


def _find_length_helper(letters_dict, n, board, words: dict, path, all_words,
                        row, col, the_word):
    """
    Helper function that perform the recursion.
    :param letters_dict: A dict that bind coords to letters on the board.
    :param n: length of the word
    :param board: Board as 2d matrix
    :param words: words dict
    :param path: coords path
    :param all_words: list of the final product.
    :param row: num of row
    :param col: num of col
    :param the_word: the word that is being generated.
    :return: None
    """
    if not 0 <= row <= 3 or not 0 <= col <= 3:
        return
    if (row, col) in path[:-1]:
        return
    if len(the_word) == n:
        if the_word in words.keys():
            all_words.append((the_word, path))
        return
    if col + 1 < 4:
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row, col + 1)],
                            all_words, row, col + 1,
                            the_word + letters_dict[(row, col + 1)])
    if (col + 1 < 4) and (row + 1 < 4):
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row + 1, col + 1)], all_words, row + 1,
                            col + 1,
                            the_word + letters_dict[(row + 1, col + 1)])
    if row + 1 < 4:
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row + 1, col)],
                            all_words, row + 1, col,
                            the_word + letters_dict[(row + 1, col)])
    if row - 1 > -1:
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row - 1, col)],
                            all_words, row - 1, col,
                            the_word + letters_dict[(row - 1, col)])
    if col - 1 > -1:
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row, col - 1)],
                            all_words, row, col - 1,
                            the_word + letters_dict[(row, col - 1)])
    if (row + 1 < 4) and (col - 1 > -1):
        _find_length_helper(letters_dict, n, board, words,
                            path + [(row + 1, col - 1)], all_words, row + 1,
                            col - 1,
                            the_word + letters_dict[(row + 1, col - 1)])
    if (row - 1 > -1) and (col - 1 > -1):
        _find_length_helper(letters_dict, n, board, words, path +
                            [(row - 1, col - 1)], all_words, row - 1, col - 1,
                            the_word + letters_dict[(row - 1, col - 1)])
    if (row - 1 > -1) and (col + 1 < 4):
        _find_length_helper(letters_dict, n, board, words, path +
                            [(row - 1, col + 1)], all_words, row - 1, col + 1,
                            the_word + letters_dict[(row - 1, col + 1)])


if __name__ == '__main__':
    pass


from boggle_board_randomizer import *

def load_words_dict(file_path):
    words_dict = {}
    f = open(file_path, "r")
    for line in f.readlines():
        words_dict[line[:-1]] = True
    f.close()
    return words_dict


def is_valid_path(board, path, words):
    word = ""
    used_coord = []
    if check_if_path_is_valid(path):
        for coord in path:
            if coord in used_coord:
                return None
            letter = board[coord[0]][coord[1]]
            word += letter
            used_coord.append(coord)
        if word in words.keys():
            return word
        else:
            return None
    else:
        return None


def check_if_path_is_valid(path):
    for i in range(1, len(path)):
        first_row, first_col = path[i-1]
        sec_row, sec_col = path[i]
        if abs(first_row - sec_row) > 1 or abs(first_col - sec_col) > 1:
            return False
    return True


def find_length_n_words(n, board, words):
    pass

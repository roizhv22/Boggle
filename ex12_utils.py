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
        first_row, first_col = path[i - 1]
        sec_row, sec_col = path[i]
        if abs(first_row - sec_row) > 1 or abs(first_col - sec_col) > 1:
            return False
    return True


def find_length_n_words(n, board, words):
    all_words = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            _find_length_helper(n, board, words, [(i, j)], all_words, i, j, [])
    return all_words


def _find_length_helper(n, board, words, path, all_words, row, col, used_cubes):
    if not 0 <= row <= 3 or not 0 <= col <= 3:
        return
    # if (row, col) in used_cubes:
    #     return
    # else:
    #     used_cubes.append((row, col))
    if len(path) == n:
        word = is_valid_path(board, path, words)
        if word in words.keys():
            all_words.append((word, path))
        return
    _find_length_helper(n, board, words, path + [(row, col + 1)], all_words,
                        row, col + 1, used_cubes)
    _find_length_helper(n, board, words, path + [(row + 1, col + 1)],
                        all_words,row + 1, col + 1, used_cubes)
    _find_length_helper(n, board, words, path + [(row + 1, col)], all_words,
                        row + 1, col, used_cubes)
    _find_length_helper(n, board, words, path + [(row - 1, col)], all_words,
                        row - 1, col, used_cubes)
    _find_length_helper(n, board, words, path + [(row, col - 1)], all_words,
                        row, col - 1, used_cubes)
    _find_length_helper(n, board, words, path + [(row + 1, col - 1)],
                        all_words,
                        row + 1, col - 1, used_cubes)
    _find_length_helper(n, board, words, path + [(row - 1, col - 1)],
                        all_words,
                        row - 1, col - 1, used_cubes)
    _find_length_helper(n, board, words, path + [(row - 1, col + 1)],
                        all_words,
                        row - 1, col + 1, used_cubes)


def get_score_from_word(word):
    return len(word) ** 2


dict = load_words_dict("boggle_dict.txt")
board = [['W', 'L', 'I', 'L'],
         ['D', 'E', 'W', 'N'],
         ['M', 'E', 'U', 'F'],
         ['P', 'E', 'H', 'O']]
for line in board:
    print(line)

for i in range(1, 17):
    print(find_length_n_words(i, board, dict))
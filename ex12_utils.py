from boggle_board_randomizer import *

def load_words_dict(file_path):
    words_dict = {}
    f = open(file_path, "r")
    for line in f.readlines():
        words_dict[line[:-1]] = True
    f.close()
    return words_dict


def is_word_valid(word, words):
    if word in words.keys():
        return True


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
        if word in words:
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

    # dict1 = load_words_dict("boggle_dict.txt")
    # dict2 = {"A": True, "AA":True, "AAA": True, "AAAA":True, "AAAAA": True, "AAAAAA": True,"AAAAAAA":True, "AAAAAAAA" : True, "AAAAAAAAA": True, "AAAAAAAAAA" : True,
    # "AAAAAAAAAAA" : True, "AAAAAAAAAAAA" : True,"AAAAAAAAAAAAA": True, "AAAAAAAAAAAAAA": True,
    #          "AAAAAAAAAAAAAAA": True, "AAAAAAAAAAAAAAAAAA": True}
    # board = [['A', 'A', 'A', 'A'],
    #          ['A', 'A', 'A', 'A'],
    #          ['A', 'A', 'A', 'A'],
    #          ['A', 'A', 'A', 'A']]
    # board1 = randomize_board()
    # for line in board1:
    #     print(line)
    # start = time.time()
    # for i in range(8,12):
    # print(find_length_n_words1(5, board1, dict1))
    # end = time.time()
    # print(end - start)




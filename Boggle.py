from Boggle_GUI import BoggleGui
from ex12_utils import *
from boggle_board_randomizer import *


class BoggleController:
    def __init__(self):
        self.board = randomize_board()
        self.gui = BoggleGui(self.board)

        for cube in self.gui.get_cubes():
            action = self.create_button_action(cube)
            self.gui.set_cube_cmd(cube, action)

    def create_button_action(self, cube_txt):
        def action():
            self.gui.change_guess_box(cube_txt)

        return action

    def check_word(self):
        pass

    def run(self):
        self.gui.run()

a = BoggleController()
a.gui.get_cubes()


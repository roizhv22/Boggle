from Boggle_GUI import BoggleGui
from Boggle_Model import Boggle_Model
from ex12_utils import *
from boggle_board_randomizer import *


class BoggleController:
    def __init__(self):
        self.board = randomize_board()
        self.gui = BoggleGui(self.board)
        self.model = Boggle_Model("boggle_dict.txt", self.board)

        for cube in self.gui.get_cubes():
            action = self.create_button_action(cube)
            self.gui.set_cube_cmd(cube, action)

        self.submit_action()
        self.gui.play_again = self.play_again

        self.clock_flag = True

    def create_button_action(self, cube_cord):
        def action():
            self.gui.change_guess_box(self.model.dict_of_letters_and_coords[cube_cord])
            neighbors = self.model.return_all_neighbors(cube_cord)
            if self.clock_flag:
                self.gui.clock_animate()
                self.clock_flag = False
            for cube in self.gui.cubes.keys():
                if cube in self.model.current_guess:
                    self.gui.cubes[cube]["state"] = "disabled"
                    self.gui.cubes[cube].config(bg="gray")
                    self.gui.cubes[cube]["disabledforeground"] = "gray"

                elif cube in neighbors and cube not in self.model.current_guess:
                    self.gui.cubes[cube]["state"] = "normal"
                    self.gui.cubes[cube].configure(fg="lime green")

                else:
                    self.gui.cubes[cube]["state"] = "disabled"
                    self.gui.cubes[cube]["disabledforeground"] = "red3"
            self.model.current_guess.append(cube_cord)

        return action

    def submit_action(self):
        def sub_action():
            x = self.model.place_guess()
            if x[0]:
                if x[1] in self.model.guessed_words:
                    self.gui.clear_guess_box()
                    self.gui.pop_up_guess(2)
                    self.set_gui_buttons_to_defualt()

                else:
                    self.gui.change_score_screen(self.model.score)
                    self.gui.clear_guess_box()
                    self.gui.pop_up_guess(0)
                    self.gui.add_to_guessed(x[1])
                    self.set_gui_buttons_to_defualt()
                    self.model.guessed_words.append(x[1])

            else:
                self.gui.clear_guess_box()
                self.gui.pop_up_guess(1)
                self.set_gui_buttons_to_defualt()

        self.gui.submit_button["command"] = sub_action

    def set_gui_buttons_to_defualt(self):
        for cube in self.gui.cubes.keys():
            self.gui.cubes[cube]["state"] = "normal"
            self.gui.cubes[cube].configure(fg="black", bg="floral white")

    def run(self):
        self.gui.run()

    def restart(self):
        self.board = randomize_board()
        self.gui = BoggleGui(self.board)
        self.model = Boggle_Model("boggle_dict.txt", self.board)

        for cube in self.gui.get_cubes():
            action = self.create_button_action(cube)
            self.gui.set_cube_cmd(cube, action)

        self.submit_action()
        self.gui.play_again = self.play_again

        self.gui.root.mainloop()

    def play_again(self):
        self.gui.gui_destroy()
        self.restart()




a = BoggleController()
a.run()



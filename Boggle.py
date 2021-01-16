# roizhv22,tzvi.simons
from Boggle_GUI import BoggleGui
from Boggle_Model import Boggle_Model
from boggle_board_randomizer import randomize_board
import tkinter as tk


class BoggleController:
    """
    The controller class for the Boggle game. Will create the main
     functionality of the game and integrate the model and GUI elements.
    """

    def __init__(self):
        """
        The constructor for the class, all relevant instances will be generate
        via this init method.
        """
        self.board = randomize_board()
        self.gui = BoggleGui(self.board)
        self.model = Boggle_Model("boggle_dict.txt", self.board)

        for cube in self.gui.get_cubes():
            action = self.create_button_action(cube)
            self.gui.set_cube_cmd(cube, action)

        self.submit_action()
        self.gui.play_again = self.play_again

        self.clock_flag = True
        self.hints = self.model.get_hint()

        self.create_menu()

    def create_menu(self):
        """
        The create menu method is designed to build the game menus.
        :return: None
        """
        menubar = tk.Menu(self.gui.root)
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="Hint me!", command=self.get_hints)
        game_menu.add_command(label="Restart Game", command=self.play_again)
        game_menu.add_command(label="Quit", command=self.gui.gui_destroy)
        self.gui.root.config(menu=menubar)

    def get_hints(self):
        """
        Get hints method creating adding the hints to the GUI.
        :return: None
        """
        self.gui.hints = ""
        flag = False
        if len(self.hints) > 0:
            flag = True
        for hint in self.hints[:5]:
            self.gui.hints += f"{hint}, "

        self.gui.hints = self.gui.hints[:-2]

        self.gui.hint_pop_up(flag)

    def create_button_action(self, cube_cord):
        """
        One of the controller main methods, this method was designed
        to wire all the relevant actions for each button.
        :param cube_cord: A cube coordinate on the board
        :return: The relevant function for each button press. Currying process
        is implemented to perform this task.
        """

        def action():
            self.gui.change_guess_box(
                self.model.dict_of_letters_and_coords[cube_cord])
            neighbors = self.model.return_all_neighbors(cube_cord)
            if self.clock_flag:
                self.gui.clock_animate()
                self.clock_flag = False
            for cube in self.gui.cubes.keys():
                if cube in self.model.current_guess:
                    self.gui.cubes[cube]["state"] = "disabled"
                    self.gui.cubes[cube].config(bg="DarkOrange4")

                    self.gui.cubes[cube]["disabledforeground"] = "DarkOrange4"

                elif cube in neighbors and cube not in self.model.current_guess:
                    self.gui.cubes[cube]["state"] = "normal"
                    self.gui.cubes[cube].configure(fg="white")

                else:
                    self.gui.cubes[cube]["state"] = "disabled"
                    self.gui.cubes[cube]["disabledforeground"] = "red3"

            self.model.current_guess.append(cube_cord)

        return action

    def submit_action(self):
        """
        This method is designed to create the submit button action.
        The method will bind the event to the relveant button in the GUI.
        :return: None
        """

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
        """
        This method returns all the buttons on the board to normal after
        each iteration. This function is called by the submit action.
        :return: None
        """
        for cube in self.gui.cubes.keys():
            self.gui.cubes[cube]["state"] = "normal"
            self.gui.cubes[cube].configure(fg="white", bg="Orange")

    def run(self):
        """
        The game runner.
        :return: None
        """
        self.gui.run()

    def restart(self):
        """
        The restart method, that reinitialize the game when called.
        :return: None
        """
        self.board = randomize_board()
        self.gui = BoggleGui(self.board)
        self.model = Boggle_Model("boggle_dict.txt", self.board)

        for cube in self.gui.get_cubes():
            action = self.create_button_action(cube)
            self.gui.set_cube_cmd(cube, action)

        self.submit_action()
        self.gui.play_again = self.play_again
        self.clock_flag = True
        self.create_menu()
        self.hints = self.model.get_hint()
        self.run()

    def play_again(self):
        """
        A helper method for the restart method.
        :return: None
        """
        self.gui.gui_destroy()
        self.restart()


if __name__ == "__main__":
    a = BoggleController()
    a.run()

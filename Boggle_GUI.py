import tkinter as tk
# from os import environ
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as game

TEST_BOARD = [['D', 'S', 'O', 'R'],
              ['T', 'E', 'W', 'E'],
              ['O', 'E', 'U', 'T'],
              ['M', 'I', 'A', 'O']]

DEFAULT_COLOR = "orange"
DEFAULT_FONT = "Gisha"
MAIN_BUT_ACTIVE_BG = "lime green"


class BoggleGui:
    def __init__(self, board=TEST_BOARD):
        self.root = tk.Tk()
        game.init()
        self.board = board
        self.set_root()

        self.play_button = tk.Button(text="play", font=(DEFAULT_FONT, 26),
                                     bg="azure",
                                     activebackground=MAIN_BUT_ACTIVE_BG,
                                     command=self.show_main_game_screen)
        self.boggle_img = tk.PhotoImage(file="Welcome pic.png")
        self.boggle_img = self.boggle_img.subsample(3)

        self.welcome_label = tk.Label(image=self.boggle_img,
                                      text="Let's play Boggle",
                                      font=(DEFAULT_FONT, 36),
                                      bg=DEFAULT_COLOR)
        self.place_welcome_win()

        self.displays_frame = tk.Frame(self.root, bg="ivory2",
                                       highlightthickness=5,
                                       highlightbackground="azure3")
        self.grid_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5
                                   , highlightbackground="azure3")
        self.top_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5,
                                  highlightbackground="azure3", relief="ridge")

        self.submit_button = tk.Button(self.top_frame)
        self.guess_box = tk.Label(self.top_frame)
        self.clock_label = tk.Label(self.displays_frame)

        self.score_label = tk.Label(self.displays_frame)
        self.guessed_words = tk.Label(self.displays_frame)

        self.cubes = {}
        self.create_board()

        self.clock_after_id = ""

        self.play_again = ""

        self.hints = ""

    def place_welcome_win(self):
        self.play_button.place(x=250, y=410)
        self.welcome_label.place(x=125, y=5)

    def set_root(self):
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.title("Boggle!")
        self.root["bg"] = DEFAULT_COLOR

    def run(self):
        self.root.mainloop()

    def show_main_game_screen(self):
        self.play_button.place_forget()
        self.welcome_label.place_forget()
        game.mixer_music.load("sounds/start_game.mp3")
        game.mixer_music.play()
        self.top_frame.place(height=100, width=600)
        self.grid_frame.place(height=400, width=400, y=100)
        self.displays_frame.place(height=400, width=200, x=400, y=100)
        self.add_displays()
        self.add_top_display()

    def create_board(self):
        for i in range(4):
            tk.Grid.columnconfigure(self.grid_frame, i, weight=1)
            tk.Grid.rowconfigure(self.grid_frame, i, weight=1)
        for i in range(4):
            for j in range(4):
                self.make_cube(i, j)

    def make_cube(self, i, j):
        cube = tk.Button(self.grid_frame, text=self.board[i][j],
                         font=(DEFAULT_FONT, 24), fg="white", bg=DEFAULT_COLOR,
                         activebackground="DarkOrange2")
        cube.grid(row=i, column=j, sticky=tk.NSEW)
        self.cubes[(i, j)] = cube

    def get_cubes(self):
        return list(self.cubes.keys())

    def set_cube_cmd(self, cube, cmd):
        button = self.cubes[cube]
        button.configure(command=cmd)

    def add_clock(self):
        self.clock_label.config(text="3:00", font=(DEFAULT_FONT, 24),
                                bg="azure",
                                borderwidth=5, relief="ridge",
                                highlightcolor="black")
        self.clock_label.place(height=80, width=190)

    def clock_animate(self):
        clock_time = self.clock_label["text"]
        if clock_time == "0:00":
            self.go_to_finish_screen()
            return
        elif clock_time[2:] == "00":
            min = int(clock_time[0]) - 1
            clock_time = str(min) + ":59"
        elif clock_time[2:] != "00":
            if int(clock_time[2:]) <= 10:
                clock_time = clock_time[:2] + "0" + str(
                    int(clock_time[2:]) - 1)
                if clock_time[0] == "0" and int(clock_time[2:]) < 10:
                    self.clock_label["fg"] = "red"
            else:
                clock_time = clock_time[:2] + str(int(clock_time[2:]) - 1)
        self.clock_label["text"] = clock_time
        self.clock_after_id = self.root.after(1000, self.clock_animate)
        # Clock after settings - 1000 for 1 sec.

    def add_displays(self):
        self.add_clock()
        self.score_label.config(text="0",
                                font=(DEFAULT_FONT, 24), bg="azure", fg="red",
                                borderwidth=5,
                                relief="ridge", highlightcolor="black")
        self.score_label.place(y=80, height=100, width=190)
        self.guessed_words.config(text="",
                                  font=(DEFAULT_FONT, 15), bg="azure",
                                  borderwidth=5,
                                  relief="ridge", anchor="nw",
                                  wraplength=190, justify="left")
        self.guessed_words.place(y=180, height=210, width=190)

    def add_top_display(self):
        self.submit_button.config(text="Submit", font=(DEFAULT_FONT, 30),
                                  bg=DEFAULT_COLOR,
                                  activebackground="DarkOrange2")
        self.submit_button.place(x=400, height=90, width=190)
        self.guess_box.config(font=(DEFAULT_FONT, 24), borderwidth=5,
                              relief="ridge")
        self.guess_box.place(height=90, width=400)

    def change_guess_box(self, chr):
        current_str = self.guess_box.cget("text")
        current_str += chr
        self.guess_box.configure(text=current_str)

    def clear_guess_box(self):
        self.guess_box["text"] = ""

    def add_to_guessed(self, word):
        self.guessed_words["text"] += f"{word},  "

    def hint_pop_up(self, flag):
        def destroy():
            pop_up.destroy()

        pop_up = tk.Toplevel(borderwidth=20)
        pop_up.title("Hints!")
        popup_label = tk.Label(pop_up, text="Here are some random words "
                                            "you can find on the board: ",
                               font=(DEFAULT_FONT, 15))

        if flag:
            hints_label = tk.Label(pop_up, text=self.hints,
                               font=(DEFAULT_FONT, 15))
        else:
            hints_label = tk.Label(pop_up, text="No valid hints, try harder!",
                                   font=(DEFAULT_FONT, 15))
        popup_label.pack()
        hints_label.pack()

        pop_up.after(2000, destroy)

    def pop_up_guess(self, flag):
        def destroy():
            pop_up.destroy()

        pop_up = tk.Toplevel(borderwidth=15)
        popup_label = tk.Label(pop_up, text="",
                               font=(DEFAULT_FONT, 15))
        popup_label.pack()
        pop_up.after(500, destroy)
        if flag == 0:
            pop_up.title("Correct!")
            popup_label.config(text="You got a word! "
                                    "Keep going")
            game.mixer_music.load("sounds/correct.mp3")
            game.mixer_music.play()
        elif flag == 1:
            pop_up.title("Wrong!")
            popup_label.config(text="Wrong, keep trying!")
            game.mixer_music.load("sounds/neg 2.mp3")
            game.mixer_music.play()
        elif flag == 2:
            pop_up.title("Guessed")
            popup_label.config(text="You already guessed this word!")
            game.mixer_music.load("sounds/neg 1.mp3")
            game.mixer_music.play()

    def change_score_screen(self, score):
        self.score_label.config(text=str(score))

    def go_to_finish_screen(self):
        out_of_time_win = tk.Toplevel(borderwidth=100, bg=DEFAULT_COLOR)
        out_of_time_win.title("OUT OF TIME")
        self.root.wm_attributes("-disabled", True)
        out_of_time_win.protocol("WM_DELETE_WINDOW", self.gui_destroy)

        def pop_pressed():
            out_of_time_win.destroy()
            self.root.destroy()

        popup_label = tk.Label(out_of_time_win, text="Time's up!",
                               font=(DEFAULT_FONT, 24), bg=DEFAULT_COLOR)
        popup_label.pack()
        score_label = tk.Label(out_of_time_win,
                               text="Your final score is " +
                                    str(self.score_label.cget("text")),
                               font=(DEFAULT_FONT, 36), bg=DEFAULT_COLOR)
        play_again_pop_up = tk.Button(out_of_time_win, text="play again",
                                      bg="azure",
                                      activebackground=MAIN_BUT_ACTIVE_BG,
                                      command=self.play_again,
                                      font=(DEFAULT_FONT, 24))
        popup_button2 = tk.Button(out_of_time_win, text="Quit",
                                  command=pop_pressed, font=(DEFAULT_FONT, 24),
                                  bg="azure", activebackground=
                                  MAIN_BUT_ACTIVE_BG)
        score_label.pack()
        if self.score_label.cget("text") != "0":
            game.mixer_music.load("sounds/kids_cheering.mp3")
            game.mixer_music.play()
        else:
            game.mixer_music.load("sounds/Kids Booing Sound Effect "
                                  "(320 kbps).mp3")
            game.mixer_music.play()

        play_again_pop_up.pack(side="left")
        popup_button2.pack(side="right")

    def gui_destroy(self):
        try:
            self.root.after_cancel(self.clock_after_id)
        except ValueError:
            pass
        finally:
            self.root.destroy()


if __name__ == "__main__":
    pass

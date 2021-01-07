import tkinter as tk

TEST_BOARD = [['D', 'S', 'O', 'R'],
              ['T', 'E', 'W', 'E'],
              ['O', 'E', 'U', 'T'],
              ['M', 'I', 'A', 'O']]


class BoggleGui():
    def __init__(self, board=TEST_BOARD):
        self.root = tk.Tk()
        self.board = board
        self.get_root()

        self.play_button = tk.Button(text="play", font=("gisha", 26),
                                     bg="peachpuff3",
                                     command=self.show_main_game_screen)
        self.welcome_label = tk.Label(text="welcome to the \nboggle jungle!!",
                                      font=("gisha", 36), bg="peachpuff2")
        self.place_welcome_win()

        self.displays_frame = tk.Frame(self.root, bg="ivory2",
                                       highlightthickness=5,
                                       highlightbackground="azure3")
        self.grid_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5
                                   , highlightbackground="azure3")
        self.top_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5,
                                  highlightbackground="black")

        self.submit_button = tk.Button(self.top_frame)
        self.guess_box = tk.Label(self.top_frame)
        self.clock_label = tk.Label(self.displays_frame)
        self.score = 0


    def place_welcome_win(self):
        self.play_button.place(x=260, y=260)
        self.welcome_label.place(x=140, y=100)

    def get_root(self):
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.title("2021-Boggle!")
        self.root["bg"] = "peachpuff2"

    def run(self):
        self.root.mainloop()

    def show_main_game_screen(self):
        self.play_button.place_forget()
        self.welcome_label.place_forget()
        self.top_frame.place(height=100, width=600)
        self.grid_frame.place(height=400, width=400, y=100)
        self.displays_frame.place(height=400, width=200, x=400, y=100)
        self.create_board()
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
                         font=("gisha", 24), \
                         bg="floral white")
        cube.grid(row=i, column=j, sticky=tk.NSEW)

    def cube_pressed(self):
        pass

    def add_clock(self):
        self.clock_label.config(text="3:00", font=("crackman", 24),
                                bg="light grey",
                                borderwidth=5, relief="flat",
                                highlightcolor="grey")
        self.clock_label.place(height=80, width=190)
        self.clock_animate()

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
        self.root.after(10, self.clock_animate)

    def add_displays(self):
        self.add_clock()
        score_label = tk.Label(self.displays_frame, text="42,780",
                               font=("crackman", 24), bg="yellow")
        score_label.place(y=80, height=100, width=190)
        your_words = tk.Label(self.displays_frame, text="your words: ",
                              font=("crackman", 24), bg="blue")
        your_words.place(y=180, height=40, width=190)
        guessed_words = tk.Label(self.displays_frame, text="bla ,nope ",
                                 font=("crackman", 24), bg="blue")
        guessed_words.place(y=220, height=170, width=190)

    def add_top_display(self):
        self.submit_button.config(text="submit", font=("arial", 24),
                                  bg="green")
        self.submit_button.place(x=400, height=90, width=190)
        self.guess_box.config(font=("gisha", 24))
        self.guess_box.place(height=90, width=390)

    def go_to_finish_screen(self):
        out_of_time_win = tk.Toplevel(borderwidth=200)
        out_of_time_win.title("OUT OF TIME")
        self.root.wm_attributes("-disabled", True)

        def pop_pressed():
            out_of_time_win.destroy()
            self.root.wm_attributes("-disabled", False)
            self.go_to_exit()

        popup_label = tk.Label(out_of_time_win, text="Time's up!",font=("arial", 24))
        popup_label.pack()
        score_label = tk.Label(out_of_time_win, text="your final score is " + str(self.score), font=("arial", 24))
        popup_button = tk.Button(out_of_time_win, text="play again", command=pop_pressed, font=("ariel", 30))
        score_label.pack()
        popup_button.pack()

    def go_to_exit(self):
        pass





BoggleGui().run()
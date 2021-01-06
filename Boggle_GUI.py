import tkinter as tk

class BoggleGui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.title("2021-Boggle!")
        self.root["bg"] = "peachpuff2"
        self.welcome_label = tk.Label(text="welcome to the \nboggle jungle!!",
                                      font=("gisha", 36), bg="peachpuff2")
        self.play_button = tk.Button(text="play", font=("gisha", 26),
                                     bg="peachpuff3",
                                     command=self.show_main_game_screen)
        self.play_button.place(x=260, y=260)
        self.welcome_label.place(x=140, y=100)
        self.top_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5,
                                  highlightbackground="black")
        self.grid_frame = tk.Frame(self.root, bg="ivory2", highlightthickness=5
                                   , highlightbackground="purple")
        self.displays_frame = tk.Frame(self.root, bg="ivory2",
                                       highlightthickness=5,
                                       highlightbackground="purple")
        self.guess = ""

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
        cube = tk.Button(self.grid_frame, text="a", font=("gisha", 24), bg="darkseagreen", command=self.add_to_guess)
        cube.grid(row=i, column=j, sticky=tk.NSEW)

    def add_to_guess(self):
        self.guess += "a"

    def add_displays(self):
        clock_label = tk.Label(self.displays_frame, text="3:00",font=("arial", 24),bg="green")
        clock_label.place(height=80, width=190)
        score_label = tk.Label(self.displays_frame, text="42,780", font=("arial", 24),bg="yellow")
        score_label.place(y=80, height=100, width=190)
        your_words = tk.Label(self.displays_frame, text="your words: ",font=("arial", 24),bg="blue")
        your_words.place(y=180,height=40, width=190)
        guessed_words = tk.Label(self.displays_frame, text="bla ,nope ",font=("arial", 24),bg="blue")
        guessed_words.place(y=220, height=170, width=190)

    def add_top_display(self):

        submit_buttoon = tk.Button(self.top_frame, text="submit", font=("arial", 24),bg="green")
        submit_buttoon.place(x=400,height=90, width=190)
        current_guesse = tk.Label(self.top_frame, text=self.guess, font=("gisha", 24))
        current_guesse.place(height=90,width=390)


BoggleGui().run()
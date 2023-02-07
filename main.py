import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("500x500")
        self.resizable(False, False)
        self.scoreInit()
        self.createNewGame()
    

    def createNewGame(self):
        #create a 4x12 grid of buttons
        for i in range(4):
            self.grid = tk.columnconfigure(self, 0, weight=1)

        colors = ["yellow", "red", "blue", "green"]
        for i in range(12):
            for color in colors:
                self.numberbutton(i, color)
                numberbutton.grid(row=i, column=colors.index(color), sticky="nsew")

    def numberbutton(self, number, color):

        self.button = tk.Button(self, text=number, bg=color, command=lambda: self.scoreUpdate(number, color))
        self.button.pack()

    def scoreInit(self):

        self.scoreYellow = 0
        self.scoreRed = 0
        self.scoreBlue = 0
        self.scoreGreen = 0

        self.scoreLabelYellow = tk.Label(self, text="Yellow: " + str(self.scoreYellow))
        self.scoreLabelYellow.pack()

        self.scoreLabelRed = tk.Label(self, text="Red: " + str(self.scoreRed))
        self.scoreLabelRed.pack()

        self.scoreLabelBlue = tk.Label(self, text="Blue: " + str(self.scoreBlue))
        self.scoreLabelBlue.pack()

        self.scoreLabelGreen = tk.Label(self, text="Green: " + str(self.scoreGreen))
        self.scoreLabelGreen.pack()


    def scoreUpdate(self, number, color):
        if color == "yellow":
            self.scoreYellow += number
        elif color == "red":
            self.scoreRed += number
        elif color == "blue":
            self.scoreBlue += number
        elif color == "green":
            self.scoreGreen += number

        self.scoreLabelYellow.config(text="Yellow: " + str(self.scoreYellow))

if __name__ == "__main__":
    app = App()
    app.mainloop()
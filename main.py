import tkinter as tk
import numpy as np

from tkinter.messagebox import showinfo


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("500x500")
        self.resizable(False, False)
        self.scoreInit()
        self.createNewGame()
    

    def createNewGame(self):

        for i in range(13):
            self.columnconfigure(i, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)

        
        
        for i in range(11):
            self.newButton = self.numberbutton(i+2, "yellow")
            self.newButton.grid(row=0, column=i, sticky="nsew")

            self.newButton = self.numberbutton(i+2, "red")
            self.newButton.grid(row=1, column=i, sticky="nsew")

            self.newButton = self.numberbutton(i+2, "blue")
            self.newButton.grid(row=2, column=i, sticky="nsew")

            self.newButton = self.numberbutton(i+2, "green")
            self.newButton.grid(row=3, column=i, sticky="nsew")

        self.endButtonYellow = self.endButton("yellow")
        self.endButtonYellow.grid(row=0, column=11, sticky="nsew")

        self.endButtonRed = self.endButton("red")
        self.endButtonRed.grid(row=1, column=11, sticky="nsew")

        self.endButtonBlue = self.endButton("blue")
        self.endButtonBlue.grid(row=2, column=11, sticky="nsew")

        self.endButtonGreen = self.endButton("green")
        self.endButtonGreen.grid(row=3, column=11, sticky="nsew")

        


        self.scoreLabelYellow.grid(row=0, column=12, sticky="nsew")
        self.scoreLabelRed.grid(row=1, column=12, sticky="nsew")
        self.scoreLabelBlue.grid(row=2, column=12, sticky="nsew")
        self.scoreLabelGreen.grid(row=3, column=12, sticky="nsew")
        


    def numberbutton(self, number, color):

        self.button = tk.Button(self, text=number, bg=color, command=lambda: self.scoreUpdate(number, color))
        
        return self.button

    def endButton(self, color):

        self.button = tk.Button(self, text="End", bg=color, command=lambda: self.endRow(color))
        self.button.config(state="disabled")

        return self.button
    

    def failButton(self):

        self.button = tk.Button(self, text="Fail", bg="black", command=lambda: self.failsUpdate()) 
        self.button.config(state="normal")

        return self.button
    
    def failsUpdate(self):
            
            self.fails += 1
            self.failButton().grid(row=4, column=11, sticky="nsew")
            self.button.config(state="disabled")
    
    def updateEndButton(self, color):

        
        if color == "yellow":
            self.endButtonYellow = self.endButton("yellow")
            self.button.config(state="normal")
            self.endButtonYellow.grid(row=0, column=11, sticky="nsew")
        elif color == "red":
            self.endButtonRed = self.endButton("red")
            self.button.config(state="normal")
            self.endButtonRed.grid(row=1, column=11, sticky="nsew")
        elif color == "blue":
            self.endButtonBlue = self.endButton("blue")
            self.button.config(state="normal")
            self.endButtonBlue.grid(row=2, column=11, sticky="nsew")
        elif color == "green":
            self.endButtonGreen = self.endButton("green")
            self.button.config(state="normal")
            self.endButtonGreen.grid(row=3, column=11, sticky="nsew")

        return self.button

    def scoreInit(self):
        
        self.scoreYellow = self.numberYellow = 0
        self.scoreRed = self.numberRed = 0
        self.scoreBlue = self.numberBlue = 0
        self.scoreGreen = self.numberGreen = 0
        self.fails = 0

        self.rowsCompleted = 0

        self.scoreLabelYellow = tk.Label(self, text="Yellow: " + str(self.scoreYellow))
        #self.scoreLabelYellow.pack()

        self.scoreLabelRed = tk.Label(self, text="Red: " + str(self.scoreRed))
        #self.scoreLabelRed.pack()

        self.scoreLabelBlue = tk.Label(self, text="Blue: " + str(self.scoreBlue))
        #self.scoreLabelBlue.pack()

        self.scoreLabelGreen = tk.Label(self, text="Green: " + str(self.scoreGreen))
        #self.scoreLabelGreen.pack()


    def scoreUpdate(self, number, color):

        if color == "yellow":
            self.numberYellow += 1
            self.scoreYellow = self.scoreFormula(self.numberYellow)

            if self.numberYellow >= 4:
                self.updateEndButton("yellow")

            updateButton = self.numberbutton(number, "yellow")
            updateButton.config(state="disabled")
            updateButton.grid(row=0, column=number-2, sticky="nsew")

        elif color == "red":
            self.numberRed += 1
            self.scoreRed = self.scoreFormula(self.numberRed)

            if self.numberRed >= 4:
                self.updateEndButton("red")

            updateButton = self.numberbutton(number, "red")
            updateButton.config(state="disabled")
            updateButton.grid(row=1, column=number-2, sticky="nsew")


        elif color == "blue":
            self.numberBlue += 1
            self.scoreBlue = self.scoreFormula(self.numberBlue)

            if self.numberBlue >= 4:
                self.updateEndButton("blue")

            updateButton = self.numberbutton(number, "blue")
            updateButton.config(state="disabled")
            updateButton.grid(row=2, column=number-2, sticky="nsew")

        elif color == "green":
            self.numberGreen += 1
            self.scoreGreen = self.scoreFormula(self.numberGreen)

            if self.numberGreen >= 4:
                self.updateEndButton("green")

            updateButton = self.numberbutton(number, "green")
            updateButton.config(state="disabled")
            updateButton.grid(row=3, column=number-2, sticky="nsew")


        self.scoreLabelYellow.config(text="Yellow: " + str(self.scoreYellow))
        self.scoreLabelRed.config(text="Red: " + str(self.scoreRed))
        self.scoreLabelBlue.config(text="Blue: " + str(self.scoreBlue))
        self.scoreLabelGreen.config(text="Green: " + str(self.scoreGreen))

    def scoreFormula(self, number):

        return np.sum(np.arange(1, number+1))
    
    def disableRow(self, color):

        if color == "yellow":
            for i in range(10):
                self.newButton = self.numberbutton(i+2, "yellow")
                self.newButton.config(state="disabled")
                self.newButton.grid(row=0, column=i, sticky="nsew")

        elif color == "red":
            for i in range(10):
                self.newButton = self.numberbutton(i+2, "red")
                self.newButton.config(state="disabled")
                self.newButton.grid(row=1, column=i, sticky="nsew")

        elif color == "blue":
            for i in range(10):
                self.newButton = self.numberbutton(i+2, "blue")
                self.newButton.config(state="disabled")
                self.newButton.grid(row=2, column=i, sticky="nsew")

        elif color == "green":
            for i in range(10):
                self.newButton = self.numberbutton(i+2, "green")
                self.newButton.config(state="disabled")
                self.newButton.grid(row=3, column=i, sticky="nsew")


    def endRow(self, color):
            
            self.disableRow(color)
    
            if color == "yellow":
                self.endButtonYellow.config(state="disabled")
                self.numberYellow += 1
                self.scoreYellow = self.scoreFormula(self.numberYellow)

                self.scoreLabelYellow.config(text="Yellow: " + str(self.scoreYellow))

            elif color == "red":
                self.endButtonRed.config(state="disabled")
                self.numberRed += 1
                self.scoreRed = self.scoreFormula(self.numberRed)

                self.scoreLabelRed.config(text="Red: " + str(self.scoreRed))

            elif color == "blue":
                self.endButtonBlue.config(state="disabled")
                self.numberBlue += 1
                self.scoreBlue = self.scoreFormula(self.numberBlue)

                self.scoreLabelBlue.config(text="Blue: " + str(self.scoreBlue))

            elif color == "green":
                self.endButtonGreen.config(state="disabled")
                self.numberGreen += 1
                self.scoreGreen = self.scoreFormula(self.numberGreen)

                self.scoreLabelGreen.config(text="Green: " + str(self.scoreGreen))

    
            self.rowsCompleted += 1
    
            if self.rowsCompleted == 2:
                self.endGame()

    def endGame(self):

        self.totalScore = self.scoreYellow + self.scoreRed + self.scoreBlue + self.scoreGreen
        message = showinfo("Game Over", "Final Score: " + str(self.totalScore))

if __name__ == "__main__":
    app = App()
    app.mainloop()
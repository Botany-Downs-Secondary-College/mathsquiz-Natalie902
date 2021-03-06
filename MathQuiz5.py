from tkinter import*
import tkinter as ttk

class MathQuiz:
    def __init__(self,parent):

        self.Welcome = Frame(parent)
        self.Welcome.grid(row = 0, column = 0)

        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
         bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NextButton = Button(self.Welcome, text = "next", command = self.show_Questions)
        self.NextButton.grid(row = 8, column = 1)

    #Labels
        self.NameLabel = Label(self.Welcome, text = "Name", anchor = W,
        fg = "black", width = 10, padx = 30, pady =10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)

        self.AgeLabel = Label(self.Welcome, text = "Age", anchor = W,
        fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.AgeLabel.grid(row = 3, column = 0)

    #Entry for Login
        self.NameEntry = Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row =  2, column = 1, columnspan = 2)

        self.AgeEntry = Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row = 3, column = 1)
    #Warning labels
        self.WarningLabel = Label(self.Welcome, text = "", anchor = W,
        fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 4, columnspan = 2)


    #Difficulty Select
        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty Level", anchor = W, 
         fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set = (0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], 
            anchor = W, padx = 50, width = 5, height = 2)
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)


     #Different Page

        self.Questions = Frame(parent)
        self.Questions.grid(row = 0, column = 1)
        self.Questions.grid_remove()

        self.QuestionsLabel = Label(self.Questions,text = "Quiz Questions", 
        bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
        font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.HomeButton = Button(self.Questions, text = "Next", command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 1)

    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_Questions(self):

        try:
            #Checks for empty and non text entries for Name
            if self.NameEntry.get() == "":
                self.WarningLabel.configure(text = " Please enter name")
                self.NameEntry.focus()
            elif self.NameEntry.get().isalpha() == False:
                self.WarningLabel.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
            #Checks for empty and age limit cases
            elif self.AgeEntry.get() == "":
                self.WarningLabel.configure(text = "Please enter age")
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) > 12:
                self.WarningLabel.configure(text = "You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 0:
                self.WarningLabel.configure(text = "You are too old")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 7:
                self.WarningLabel.configure(text = "You are too young")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            else: 
                self.Welcome.grid_remove()
                self.Questions.grid()

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0,END)
            self.AgeEntry.focus()
        



if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
from tkinter import *
from tkinter import messagebox
from random import *

class menuGUI:
    def __init__(self, menu):
        self.menu = menu
        menu.geometry("250x120")
        menu.title("Guess Who!")
        menu.grid()

        self.introlabel = Label(menu, font=(15), text="Welcome to GUESS WHO!", justify = "center")
        self.introlabel.grid(column = 0, row = 0)

        self.play_button = Button(menu, text="Play", command=play)
        self.play_button.grid(column = 0, row = 1, sticky = "W,E")

        self.highscores_button = Button(menu, text="High Scores", command=highscores)
        self.highscores_button.grid(column = 0, row = 2, sticky = "W,E")

        self.close_button = Button(menu, text="Close", command=root.destroy)
        self.close_button.grid(column = 0, row = 3, sticky = "W,E")


class gameGUI:
    def __init__(self, game):
        self.game = game
        game.geometry("600x600")
        game.title("Guess Who!")
        game.grid()

        rules = "Instructions: \n The computer will pick a character from the grid on the left and you must ask the computer about the features of the character to deduct who it is. Use the field below to select features to ask about"

        self.titlelabel = Label(game, font=("Helvetica", 20), text="GUESS WHO!")
        self.titlelabel.grid(column = 0, row = 0, sticky = "W", columnspan = 4)

        self.rules = Label(game, font=("Helvetica", 10), text = rules, wraplength = 200, justify = "left")
        self.rules.grid(column = 0, row = 1, sticky = "W", columnspan = 3, rowspan = 3)

        self.questionlabel = Label(game, font=("Helvectica", 15), text = "Question Zone", wraplength = 200, justify = "left")
        self.questionlabel.grid(column = 0, row = 4, pady = 20, columnspan = 3)

        self.questionprefix = Label(game, font=("Helvectica", 10), text = "Does the character have...", wraplength = 200, justify = "left")
        self.questionprefix.grid(column = 0, row = 5, columnspan = 3)

        self.malebutton = Button(game, text = "Male", command=maleselect)
        self.malebutton.grid(column = 0, row = 6, sticky = "W,E")

        self.femalebutton = Button(game, text = "Female", command=femaleselect)
        self.femalebutton.grid(column = 1, row = 6, sticky = "W,E")

        self.blackbutton = Button(game, text = "Black", command=blackselect)
        self.blackbutton.grid(column = 2, row = 6, sticky = "W,E")

        self.glassesbutton = Button(game, text = "Glasses", command=glassesselect)
        self.glassesbutton.grid(column = 0, row = 7, sticky = "W,E")

        self.oldbutton = Button(game, text = "Old", command=oldselect)
        self.oldbutton.grid(column = 1, row = 7, sticky = "W,E")

        self.hatbutton = Button(game, text = "Hat", command=hatselect)
        self.hatbutton.grid(column = 2, row = 7, sticky = "W,E")

        self.facialhairbutton = Button(game, text = "Facial Hair", command=facialhairselect)
        self.facialhairbutton.grid(column = 0, row = 8, sticky = "W,E")

        self.longhairbutton = Button(game, text = "Long Hair", command=longhairselect)
        self.longhairbutton.grid(column = 1, row = 8, sticky = "W,E")

        self.blondebutton = Button(game, text = "Blonde", command=blondeselect)
        self.blondebutton.grid(column = 2, row = 8, sticky = "W,E")

        self.questionanswerspace = Label(game, font=("Helvectica", 10), text = "", wraplength = 200, justify = "left")
        self.questionanswerspace.grid(column = 0, row = 9, pady = 20, columnspan = 3)

        self.back_button = Button(game, text = "Back", command=menuGUIfunc)
        self.back_button.grid(column = 0, row = 11, sticky = "W,E", columnspan = 3)

        self.close_button = Button(game, text="Close", command=root.destroy)
        self.close_button.grid(column = 0, row = 12, sticky = "W,E", columnspan = 3)

        char1image = PhotoImage(file = char1["path"])
        self.char1label = Button(game, image = char1image, command=self.userselection)
        self.char1label.image = char1image
        self.char1label.grid(column = 3 , row = 1)

        char2image = PhotoImage(file = char2["path"])
        self.char2label = Button(game, image = char2image, command=self.userselection)
        self.char2label.image = char2image
        self.char2label.grid(column = 4 , row = 1)

        char3image = PhotoImage(file = char3["path"])
        self.char3label = Button(game, image = char3image, command=self.userselection)
        self.char3label.image = char3image
        self.char3label.grid(column = 5 , row = 1)

        char4image = PhotoImage(file = char4["path"])
        self.char4label = Button(game, image = char4image, command=self.userselection)
        self.char4label.image = char4image
        self.char4label.grid(column = 6 , row = 1)

        char5image = PhotoImage(file = char5["path"])
        self.char5label = Button(game, image = char5image, command=self.userselection)
        self.char5label.image = char5image
        self.char5label.grid(column = 3 , row = 2)

        char6image = PhotoImage(file = char6["path"])
        self.char6label = Button(game, image = char6image, command=self.userselection)
        self.char6label.image = char6image
        self.char6label.grid(column = 4 , row = 2)

        char7image = PhotoImage(file = char7["path"])
        self.char7label = Button(game, image = char7image, command=self.userselection)
        self.char7label.image = char7image
        self.char7label.grid(column = 5 , row = 2)

        char8image = PhotoImage(file = char8["path"])
        self.char8label = Button(game, image = char8image, command=self.userselection)
        self.char8label.image = char8image
        self.char8label.grid(column = 6 , row = 2)

        char9image = PhotoImage(file = char9["path"])
        self.char9label = Button(game, image = char9image, command=self.userselection)
        self.char9label.image = char9image
        self.char9label.grid(column = 3 , row = 3)

        char10image = PhotoImage(file = char10["path"])
        self.char10label = Button(game, image = char10image, command=self.userselection)
        self.char10label.image = char10image
        self.char10label.grid(column = 4 , row = 3)

        char11image = PhotoImage(file = char11["path"])
        self.char11label = Button(game, image = char11image, command=self.userselection)
        self.char11label.image = char11image
        self.char11label.grid(column = 5 , row = 3)

        char12image = PhotoImage(file = char12["path"])
        self.char12label = Button(game, image = char12image, command=self.userselection)
        self.char12label.image = char12image
        self.char12label.grid(column = 6 , row = 3)

        char13image = PhotoImage(file = char13["path"])
        self.char13label = Button(game, image = char13image, command=self.userselection)
        self.char13label.image = char13image
        self.char13label.grid(column = 3 , row = 4)

        char14image = PhotoImage(file = char14["path"])
        self.char14label = Button(game, image = char14image, command=self.userselection)
        self.char14label.image = char14image
        self.char14label.grid(column = 4 , row = 4)

        char15image = PhotoImage(file = char15["path"])
        self.char15label = Button(game, image = char15image, command=self.userselection)
        self.char15label.image = char15image
        self.char15label.grid(column = 5 , row = 4)

        char16image = PhotoImage(file = char16["path"])
        self.char16label = Button(game, image = char16image, command=self.userselection)
        self.char16label.image = char16image
        self.char16label.grid(column = 6 , row = 4)

        generatenumber()

    def userselection(self):
        self.decidelabel = Label(root, font=("Helvectica", 10), text = "Are you sure?", wraplength = 200, justify = "left")
        self.decidelabel.grid(column = 4, row = 6, columnspan = 2)

        self.yesbutton = Button(root, text = "Yes", command=endfunc)
        self.yesbutton.grid(column = 4, row = 7, sticky = "W,E")

        self.nobutton = Button(root, text = "No", command=self.optionno)
        self.nobutton.grid(column = 5, row = 7, sticky = "W,E")

    def optionno(self):
        self.decidelabel.grid_remove()
        self.yesbutton.grid_remove()
        self.nobutton.grid_remove()

class highscoresGUI:
    def __init__(self, HS):
        self.HS = HS
        HS.geometry("200x275")
        HS.title("Guess Who!")
        HS.grid()

        self.titlelabel = Label(HS, font=("Helvectica", 20), text = "High Scores")
        self.titlelabel.grid(column = 0, row = 0)

        self.HStable = Listbox(HS)

        textfile = open("E:\PROJECT\highscores.txt", "r")
        highscoreslist = textfile.readlines()

        highscoreslist.sort(key=lambda x:int(x.split()[0]))

        for item in highscoreslist:
            self.HStable.insert(END, item)

        self.HStable.grid(column = 0, row = 1)

        self.back_button = Button(HS, text = "Back", command=menuGUIfunc)
        self.back_button.grid(column = 0, row = 6, sticky = "W,E")

        self.close_button = Button(HS, text="Close", command=root.destroy)
        self.close_button.grid(column = 0, row = 7, sticky = "W,E")

class endGUI:
    def __init__(self, end):
        self.end = end
        end.geometry("250x300")
        end.title("Game Over!")
        end.grid()

        self.textlabel = Label(end, text = "The answer was...", font=("Helvectica", 15), wraplength = 200, justify = "left")
        self.textlabel.grid(column = 0, row = 0)

        randomcharimage = PhotoImage(file = randomchar["path"])
        self.randomcharlabel = Label(end, image = randomcharimage)
        self.randomcharlabel.image = randomcharimage
        self.randomcharlabel.grid(column = 0 , row = 1)

        self.pointscount = Label(end, text = "You're score was " + str(points), font=("Helvectica", 10), wraplength = 200, justify = "left")
        self.pointscount.grid(column = 0, row = 2)

        self.highscorelabel = Label(end, text = "Please enter your name for the highscores table:", font=("Helvectica", 10), wraplength = 200, justify = "left")
        self.highscorelabel.grid(column = 0, row = 3)

        global HSfield
        HSfield = Entry(end)
        HSfield.grid(column = 0, row = 4)

        self.entrybutton = Button(end, text = "Enter", command = highscoreexport)
        self.entrybutton.grid(column = 0, row = 5, sticky = "W,E")

        self.back_button = Button(end, text = "Back", command=menuGUIfunc)
        self.back_button.grid(column = 0, row = 6, sticky = "W,E")

        self.close_button = Button(end, text="Close", command=root.destroy)
        self.close_button.grid(column = 0, row = 7, sticky = "W,E")

def play():
    clearscreen()
    gameGUI(root)

def highscores():
    clearscreen()
    highscoresGUI(root)

def menuGUIfunc():
    clearscreen()
    menuGUI(root)

def generatenumber():
    global randomchar
    randomnumber = randint(0, 15)
    randomchar = characters[randomnumber]

def maleselect():
    global points
    if randomchar["male"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def femaleselect():
    global points
    if randomchar["female"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def blackselect():
    global points
    if randomchar["black"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def glassesselect():
    global points
    if randomchar["glasses"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def oldselect():
    global points
    if randomchar["old"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def hatselect():
    global points
    if randomchar["hat"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def facialhairselect():
    global points
    if randomchar["facial_hair"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def longhairselect():
    global points
    if randomchar["long_hair"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def blondeselect():
    global points
    if randomchar["blonde"] == "t":
        points += 1
        yesvar = messagebox.showinfo("Answer", "Answer: YES!")
    else:
        points += 1
        novar = messagebox.showinfo("Answer", "Answer: NO!")

def endfunc():
    clearscreen()
    endGUI(root)

def highscoreexport():
    global points
    export = str(points) + " - " + str(HSfield)
    with open("E:\\PROJECT\\highscores.txt",'a') as f:
        f.write(export + "\n")

def clearscreen():
    for widget in root.winfo_children():
        widget.destroy()

char1 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char1.gif",
"male" : "t",
"female" : "f",
"black" : "t",
"glasses" : "f",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "f",
"blonde" : "t"}

char2 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char2.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "t",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "f"}

char3 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char3.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "f",
"old" : "t",
"hat" : "f",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char4 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char4.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "f",
"old" : "f",
"hat" : "t",
"facial_hair" : "f",
"long_hair" : "f",
"blonde" : "t"}

char5 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char5.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "t",
"old" : "f",
"hat" : "f",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char6 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char6.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "f",
"old" : "t",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "f"}

char7 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char7.gif",
"male" : "t",
"female" : "f",
"black" : "t",
"glasses" : "f",
"old" : "f",
"hat" : "t",
"facial_hair" : "f",
"long_hair" : "f",
"blonde" : "f"}

char8 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char8.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "f",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "t"}

char9 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char9.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "f",
"old" : "f",
"hat" : "t",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char10 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char10.gif",
"male" : "f",
"female" : "t",
"black" : "t",
"glasses" : "f",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "f",
"blonde" : "t"}

char11 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char11.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "f",
"old" : "t",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "f"}

char12 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char12.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "t",
"old" : "f",
"hat" : "f",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char13 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char13.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "f",
"old" : "f",
"hat" : "t",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char14 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char14.gif",
"male" : "f",
"female" : "t",
"black" : "t",
"glasses" : "f",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "f"}

char15 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char15.gif",
"male" : "t",
"female" : "f",
"black" : "f",
"glasses" : "f",
"old" : "t",
"hat" : "f",
"facial_hair" : "t",
"long_hair" : "f",
"blonde" : "f"}

char16 = {
"path" : "E:\\PROJECT\\Images\\Resized\\rsz_char16.gif",
"male" : "f",
"female" : "t",
"black" : "f",
"glasses" : "t",
"old" : "f",
"hat" : "f",
"facial_hair" : "f",
"long_hair" : "t",
"blonde" : "f"}

characters = [char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14, char15, char16]

points = 0

root = Tk()
menuGUIfunc()
root.mainloop()

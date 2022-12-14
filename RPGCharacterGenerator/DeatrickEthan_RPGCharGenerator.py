"""
Ethan Deatrick
12/14/2022
RPG Character Generator

This program will let you generate a simplified character sheet to be used in tabletop RPGs. It does this by letting
a user choose their name, race, class, and various stats. The stats selected apply various bonuses, such as +1 damage
for every +1 strength. There is a help button to open a window with a brief explanation of the application.
"""
from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("RPG Character Generator")  # add title
root.resizable(False, False)  # makes the main window not resizable

class CharacterGenerator:
    """Main menu with a couple logos and three buttons to navigate the app. The start button will open a new window
    to begin character creation. The help button will open a new window with a brief explanation of the app. The
    exit button will close the application."""
    def __init__(self, master):
        # create main menu window for app
        self.master = master
        self.frame = tk.Frame(self.master, width=300, height=400, bg="light blue")
        self.frame.pack()

        # create widgets for main menu window.
        # Two photos, one as a logo and the other as a space filler to make the menu look nicer.
        self.logo = tk.PhotoImage(file="logo.png")
        self.logoLabel = tk.Label(image=self.logo)
        self.logo2 = tk.PhotoImage(file="fighter.png")
        self.logo2Label = tk.Label(image=self.logo2)
        # labels
        self.startLabel = tk.Label(self.frame, text="Create new character", bg="light blue", font=14)
        self.helpLabel = tk.Label(self.frame, text="How it works", bg="light blue", font=14)
        # buttons with commands to navigate through the application
        self.startButton = tk.Button(self.frame, text="Start", height=1, width=10, font=12, bg="white",
                                     command=self.startnew)
        self.helpButton = tk.Button(self.frame, text="Help", height=1, width=10, font=12, bg="white",
                                    command=self.helpbutton)
        self.exitButton = tk.Button(self.frame, text="Exit", height=1, width=10, font=12, bg="white",
                                    command=self.exit)

        # Place widgets on main window according to x, y values
        # photos
        self.logoLabel.place(x=20, y=20)
        self.logo2Label.place(x=105, y=65)
        # labels
        self.startLabel.place(x=70, y=168)
        self.helpLabel.place(x=97, y=228)
        # buttons
        self.startButton.place(x=95, y=190)
        self.helpButton.place(x=95, y=250)
        self.exitButton.place(x=95, y=310)

    def startnew(self):
        """Opens the character creation window when start button is clicked"""
        self.start = CreateCharacterWindow()
        self.start.window.mainloop()

    def helpbutton(self):
        """Opens the help menu when help button is clicked"""
        self.help = helpScreen()
        self.help.helpWindow.mainloop()

    def exit(self):
        """Closes the program if you press exit button"""
        exit()


class CreateCharacterWindow:
    """Opens the create new character window to start creation. Creates two dictionaries to hold stats of character.

    dictionary to hold stats:
    charStats
    keys: "Hit Points", "Mana Points", "damage", "critical strike", "Strength", "Agility", "Endurance", "Intelligence"

    Dictionary to hold Other character info:
    charInfo
    keys: "Name", "Race", "Class"

    """
    def __init__(self):
        #  Create new window
        self.window = tk.Toplevel()
        self.window.resizable = (False, False)  # Sets x and y resizable to false
        self.frame = tk.Frame(self.window, width=300, height=400)  # set window size
        self.frame.pack()

        # create widgets for start new character window
        self.charNameEntry = tk.Entry(self.window, width=15)
        self.nameNext = tk.Button(self.window, text="Confirm", command=self.choosename)
        self.mainLabel = tk.Label(self.window, text="Enter a name for your character", font=("bold", 12))
        self.exitCreate = tk.Button(self.window, text="Exit to Main Menu", command=self.exitCreateMenu)

        # place widgets on window
        self.charNameEntry.place(x=95, y=140)
        self.nameNext.place(x=115, y=170)
        self.mainLabel.place(x=38, y=100)
        self.exitCreate.place(x=90, y=360)

        # create dictionaries to hold character stats and information. Set starting values.
        self.charStats = {"Hit Points": 10, "Mana Points": 10, "Damage": 1, "Critical Chance": 5, "Strength": 1,
                          "Agility": 1, "Endurance": 1, "Intelligence": 1}
        self.charInfo = {"Name": "", "Race": "", "Class": ""}

    def choosename(self):
        """Stores character name and makes sure field is not empty when button is pressed."""
        if self.charNameEntry.get() == "":  # input validation with error message if empty
            messagebox.showwarning("Warning!", "Hold up! Please enter a character name to continue")
        else:  # If character name field isn't empty, store the name in charInfo dictionary
            self.charInfo["Name"] = str(self.charNameEntry.get())
            self.raceSelectionMenu()

    def raceSelectionMenu(self):
        """Closes name window widgets and creates new widgets including radio buttons for a user to select
        a race for their character. There are four different choices, and one must be selected before moving
        on to the next screen, or they will get an error message."""
        # Clear widgets
        self.clearNameMenu()

        # Label
        self.mainLabel = tk.Label(self.window, text="Choose a Race", font=("bold", 14))

        # race int variable determines what race is picked when a radio button is picked from below
        self.race = IntVar()

        #  radio buttons with values attached.
        self.humanButton = Radiobutton(self.window, text="Human", variable=self.race, value=1)
        self.orcButton = Radiobutton(self.window, text="Orc", variable=self.race, value=2)
        self.elfButton = Radiobutton(self.window, text="Elf", variable=self.race, value=3)
        self.dwarfButton = Radiobutton(self.window, text="Dwarf", variable=self.race, value=4)
        # Next button that will only work after a race is selected
        self.raceNext = tk.Button(self.window, text="Next", command=self.chooseRace)

        # place widgets
        self.mainLabel.place(x=70, y=60)
        self.humanButton.place(x=100, y=100)
        self.orcButton.place(x=100, y=140)
        self.elfButton.place(x=100, y=180)
        self.dwarfButton.place(x=100, y=220)
        self.raceNext.place(x=120, y=290)

    def chooseRace(self):
        """Stores character race as charRace by checking value of radio buttons in raceSelectionMenu
        with if else statements, also makes sure that at least one was picked before moving on.
        Dictionary value affected:
        charInfo["Race"]
        """
        # if else statements use race variable made in raceSelectionMenu to determine what race the user chose.
        if self.race.get() == 1:
            self.charInfo["Race"] = "Human"  # Uses charInfo dictionary to store race
            self.classSelectionMenu()  # move on to class selection
        elif self.race.get() == 2:
            self.charInfo["Race"] = "Orc"
            self.classSelectionMenu()
        elif self.race.get() == 3:
            self.charInfo["Race"] = "Elf"
            self.classSelectionMenu()
        elif self.race.get() == 4:
            self.charInfo["Race"] = "Dwarf"
            self.classSelectionMenu()
        else:  # input validation to make sure a radio button was selected.
            messagebox.showwarning("Warning!", "Woah there! Please pick a race to continue.")

    def classSelectionMenu(self):
        """Clears the race selection menu widgets and opens new widgets to show the class selection screen.
        This screen is similar to the previous screen, but it has one less radio button. User must select one of
        the three classes before they can move on to the next screen."""
        self.clearRaceMenu()

        # main label
        self.mainLabel = tk.Label(self.window, text="Choose a Class", font=("bold", 14))

        # charclass variable made to store what class choice is
        self.charclass = IntVar()

        # Radio buttons for user to click, then click next button to finalize choice.
        self.fighterButton = Radiobutton(self.window, text="Fighter", variable=self.charclass, value=1)
        self.wizardButton = Radiobutton(self.window, text="Wizard", variable=self.charclass, value=2)
        self.rogueButton = Radiobutton(self.window, text="Rogue", variable=self.charclass, value=3)
        self.classNext = tk.Button(self.window, text="Next", command=self.chooseClass)

        # Place the widgets on screen
        self.mainLabel.place(x=70, y=60)
        self.fighterButton.place(x=100, y=100)
        self.wizardButton.place(x=100, y=140)
        self.rogueButton.place(x=100, y=180)
        self.classNext.place(x=120, y=290)

    def chooseClass(self):
        """If else statements to determine character class by checking radio button values in classSelectionMenu
        creates the charClass variable
        Dictionary value affected:
        charInfo["Class"]
        """
        # charclass created in classSelectionMenu after radio button picked, used here to decide what choice was
        if self.charclass.get() == 1:
            self.charInfo["Class"] = "Fighter"  # Uses charInfo dictionary to store class choice
            self.statSelectionMenu()
        elif self.charclass.get() == 2:
            self.charInfo["Class"] = "Wizard"
            self.statSelectionMenu()
        elif self.charclass.get() == 3:
            self.charInfo["Class"] = "Rogue"
            self.statSelectionMenu()
        else:
            messagebox.showwarning("Warning!", "Woah, Nelly! Please pick a class to continue.")

    def statSelectionMenu(self):
        """Lets user spend 10 points on their 4 primary attributes to complete character creation. Uses + and - buttons
        to let users decide which stats to adjust. Finalize button will only become available when
        all points are spent."""
        # Clear last menu widgets
        self.clearClassMenu()

        # remaining points to spend on attributes, will control when finalize button becomes available
        self.remainingPoints = 10

        # Creates 2 labels for each stat to show attribute name as well as a number to show what current value is
        self.mainLabel = tk.Label(self.window, text="Disperse your stat points", font=("bold", 14))
        self.strLabel = tk.Label(self.window, text="Strength", font=12)
        self.strNum = tk.Label(self.window, text=str(self.charStats["Strength"]), font=("bold", 15))
        self.agiLabel = tk.Label(self.window, text="Agility", font=12)
        self.agiNum = tk.Label(self.window, text=str(self.charStats["Agility"]), font=("bold", 15))
        self.endLabel = tk.Label(self.window, text="Endurance", font=12)
        self.endNum = tk.Label(self.window, text=str(self.charStats["Endurance"]), font=("bold", 15))
        self.intLabel = tk.Label(self.window, text="Intelligence", font=12)
        self.intNum = tk.Label(self.window, text=str(self.charStats["Intelligence"]), font=("bold", 15))
        # label to show how many points remaining to spend on stats
        self.remainingLabel = tk.Label(self.window, text="Remaining points:", font=15)
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))

        # Create a + and a - button for each stat to increase and decrease stat. Will adjust remaining points to spend.
        self.strUp = tk.Button(self.window, text="+", command=self.strUp)
        self.strDown = tk.Button(self.window, text="-", command=self.strDown)
        self.strDown["state"] = DISABLED
        self.agiUp = tk.Button(self.window, text="+", command=self.agiUp)
        self.agiDown = tk.Button(self.window, text="-", command=self.agiDown)
        self.agiDown["state"] = DISABLED
        self.endUp = tk.Button(self.window, text="+", command=self.endUp)
        self.endDown = tk.Button(self.window, text="-", command=self.endDown)
        self.endDown["state"] = DISABLED
        self.intUp = tk.Button(self.window, text="+", command=self.intUp)
        self.intDown = tk.Button(self.window, text="-", command=self.intDown)
        self.intDown["state"] = DISABLED

        # finalize button to complete character creation. Only becomes enabled after remainingPoints reach 0
        self.finalizeButton = tk.Button(self.window, text="Finalize", command=self.charSheet)
        self.finalizeButton["state"] = DISABLED

        # Place the widgets
        # Strength
        self.strLabel.place(x=30, y=55)
        self.strNum.place(x=150, y=55)
        self.strUp.place(x=175, y=55)
        self.strDown.place(x=125, y=55)
        # Agility
        self.agiLabel.place(x=30, y=105)
        self.agiNum.place(x=150, y=100)
        self.agiUp.place(x=175, y=100)
        self.agiDown.place(x=125, y=100)
        # Endurance
        self.endLabel.place(x=30, y=155)
        self.endNum.place(x=150, y=150)
        self.endUp.place(x=175, y=150)
        self.endDown.place(x=125, y=150)
        # Intelligence
        self.intLabel.place(x=30, y=205)
        self.intNum.place(x=150, y=200)
        self.intUp.place(x=175, y=200)
        self.intDown.place(x=125, y=200)
        # main label
        self.mainLabel.place(x=40, y=10)
        # finalize button
        self.finalizeButton.place(x=118, y=300)
        # remaining points label
        self.remainingLabel.place(x=20, y=260)
        self.remainingNumber.place(x=155, y=256)


    def strUp(self):
        """Increases strength by 1 and reduces available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints -= 1
        self.charStats["Strength"] += 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.strNum.destroy()
        self.strNum = tk.Label(self.window, text=str(self.charStats["Strength"]), font=("bold", 15))
        self.strNum.place(x=150, y=55)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # make sure stat can't go below 1
        self.strDown["state"] = NORMAL
        if self.charStats["Strength"] == 1:
            self.strDown["state"] = DISABLED
        # if remaining points run out after button press, disables all other "+" buttons.
        if self.remainingPoints == 0:
            self.finalizeButton["state"] = NORMAL
            self.strUp["state"] = DISABLED
            self.agiUp["state"] = DISABLED
            self.endUp["state"] = DISABLED
            self.intUp["state"] = DISABLED

    def strDown(self):
        """Reduces strength by 1 and increases available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints += 1
        self.charStats["Strength"] -= 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.strNum.destroy()
        self.strNum = tk.Label(self.window, text=str(self.charStats["Strength"]), font=("bold", 15))
        self.strNum.place(x=150, y=55)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # Makes sure stat selected can't go below 0 by disabling button when stat = 1
        if self.charStats["Strength"] == 1:
            self.strDown["state"] = DISABLED
        elif self.charStats["Strength"] > 1:
            self.strDown["state"] = NORMAL
        # ensures the "+" buttons are enabled if remaining points are above 0
        if self.remainingPoints != 0:
            self.finalizeButton["state"] = DISABLED
            self.strUp["state"] = NORMAL
            self.agiUp["state"] = NORMAL
            self.endUp["state"] = NORMAL
            self.intUp["state"] = NORMAL

    def agiUp(self):
        """Increases agility by 1 and reduces available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints -= 1
        self.charStats["Agility"] += 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.agiNum.destroy()
        self.agiNum = tk.Label(self.window, text=str(self.charStats["Agility"]), font=("bold", 15))
        self.agiNum.place(x=150, y=100)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # make sure stat can't go below 1
        self.agiDown["state"] = NORMAL
        if self.charStats["Agility"] == 1:
            self.agiDown["state"] = DISABLED
        # if remaining points run out after button press, disables all other "+" buttons.
        if self.remainingPoints == 0:
            self.finalizeButton["state"] = NORMAL
            self.strUp["state"] = DISABLED
            self.agiUp["state"] = DISABLED
            self.endUp["state"] = DISABLED
            self.intUp["state"] = DISABLED

    def agiDown(self):
        """Reduces agility by 1 and increases available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints += 1
        self.charStats["Agility"] -= 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.agiNum.destroy()
        self.agiNum = tk.Label(self.window, text=str(self.charStats["Agility"]), font=("bold", 15))
        self.agiNum.place(x=150, y=100)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # Makes sure stat selected can't go below 0 by disabling button when stat = 1
        if self.charStats["Agility"] == 1:
            self.agiDown["state"] = DISABLED
        elif self.charStats["Agility"] > 1:
            self.agiDown["state"] = NORMAL
        # ensures the "+" buttons are enabled if remaining points are above 0
        if self.remainingPoints != 0:
            self.finalizeButton["state"] = DISABLED
            self.strUp["state"] = NORMAL
            self.agiUp["state"] = NORMAL
            self.endUp["state"] = NORMAL
            self.intUp["state"] = NORMAL

    def endUp(self):
        """Increases endurance by 1 and reduces available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints -= 1
        self.charStats["Endurance"] += 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.endNum.destroy()
        self.endNum = tk.Label(self.window, text=str(self.charStats["Endurance"]), font=("bold", 15))
        self.endNum.place(x=150, y=150)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # make sure stat can't go below 1
        self.endDown["state"] = NORMAL
        if self.charStats["Endurance"] == 1:
            self.endDown["state"] = DISABLED
        # if remaining points run out after button press, disables all other "+" buttons.
        if self.remainingPoints == 0:
            self.finalizeButton["state"] = NORMAL
            self.strUp["state"] = DISABLED
            self.agiUp["state"] = DISABLED
            self.endUp["state"] = DISABLED
            self.intUp["state"] = DISABLED

    def endDown(self):
        """reduces endurance by 1 and increases available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints += 1
        self.charStats["Endurance"] -= 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.endNum.destroy()
        self.endNum = tk.Label(self.window, text=str(self.charStats["Endurance"]), font=("bold", 15))
        self.endNum.place(x=150, y=150)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # Makes sure stat selected can't go below 0 by disabling button when stat = 1
        if self.charStats["Endurance"] == 1:
            self.endDown["state"] = DISABLED
        elif self.charStats["Endurance"] > 1:
            self.endDown["state"] = NORMAL
        # ensures the "+" buttons are enabled if remaining points are above 0
        if self.remainingPoints != 0:
            self.finalizeButton["state"] = DISABLED
            self.strUp["state"] = NORMAL
            self.agiUp["state"] = NORMAL
            self.endUp["state"] = NORMAL
            self.intUp["state"] = NORMAL

    def intUp(self):
        """Increases intelligence by 1 and reduces available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints -= 1
        self.charStats["Intelligence"] += 1
        # change the number widgets on screen representing the attribute selected and remaining points
        self.intNum.destroy()
        self.intNum = tk.Label(self.window, text=str(self.charStats["Intelligence"]), font=("bold", 15))
        self.intNum.place(x=150, y=200)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # make sure stat can't go below 1
        self.intDown["state"] = NORMAL
        if self.charStats["Intelligence"] == 1:
            self.intDown["state"] = DISABLED
        # if remaining points run out after button press, disables all other "+" buttons.
        if self.remainingPoints == 0:
            self.finalizeButton["state"] = NORMAL
            self.strUp["state"] = DISABLED
            self.agiUp["state"] = DISABLED
            self.endUp["state"] = DISABLED
            self.intUp["state"] = DISABLED


    def intDown(self):
        """Reduces intelligence by 1 and increases available points by 1 on button click."""
        # adjust remaining points and attribute selected
        self.remainingPoints += 1
        self.charStats["Intelligence"] -= 1
        # Update stat selected and remaining points widgets
        self.intNum.destroy()
        self.intNum = tk.Label(self.window, text=str(self.charStats["Intelligence"]), font=("bold", 15))
        self.intNum.place(x=150, y=200)
        self.remainingNumber.destroy()
        self.remainingNumber = tk.Label(self.window, text=self.remainingPoints, font=("bold", 15))
        self.remainingNumber.place(x=155, y=256)
        # Makes sure stat selected can't go below 0 by disabling button when stat = 1
        if self.charStats["Intelligence"] == 1:
            self.intDown["state"] = DISABLED
        elif self.charStats["Intelligence"] > 1:
            self.intDown["state"] = NORMAL
        # ensures the "+" buttons are enabled if remaining points are above 0
        if self.remainingPoints != 0:
            self.finalizeButton["state"] = DISABLED
            self.strUp["state"] = NORMAL
            self.agiUp["state"] = NORMAL
            self.endUp["state"] = NORMAL
            self.intUp["state"] = NORMAL

    def charSheet(self):
        # Clear last menu
        self.clearStatMenu()
        # apply stat bonuses to stats. such as 1 strength resulting in +1 damage
        self.addStatBonus()

        # create label widgets to show all the user selected character info
        self.nameLabel = tk.Label(self.window, text="Name: "+self.charInfo["Name"], font=("bold", 14))
        self.classLabel = tk.Label(self.window, text="Level 1 " + self.charInfo["Race"] + " " + self.charInfo["Class"],
                                   font=("bold", 14))
        self.hitPointLabel = tk.Label(self.window, text="Health:    " + str(self.charStats["Hit Points"]), font=13)
        self.manaPointLabel = tk.Label(self.window, text="Mana:     " + str(self.charStats["Mana Points"]), font=13)
        self.damageLabel = tk.Label(self.window, text="Damage:     " + str(self.charStats["Damage"]), font=13)
        self.criticalLabel = tk.Label(self.window, text="Critical:     " + (str(self.charStats["Critical Chance"]) +
                                                                               "%"), font=13)
        self.strengthLabel = tk.Label(self.window, text="Strength:         " + str(self.charStats["Strength"]), font=13)
        self.agilityLabel = tk.Label(self.window, text="Agility:             " + str(self.charStats["Agility"]), font=13)
        self.enduranceLabel = tk.Label(self.window, text="Endurance:     " + str(self.charStats["Endurance"]), font=13)
        self.intelligenceLabel = tk.Label(self.window, text="Intelligence:    " + str(self.charStats["Intelligence"]),
                                          font=13)
        # Place label widgets on screen
        self.nameLabel.place(x=25, y=20)
        self.classLabel.place(x=25, y=45)
        self.hitPointLabel.place(x=25, y=85)
        self.manaPointLabel.place(x=25, y=103)
        self.damageLabel.place(x=160, y=155)
        self.criticalLabel.place(x=160, y=180)
        self.strengthLabel.place(x=25, y=155)
        self.agilityLabel.place(x=25, y=180)
        self.enduranceLabel.place(x=25, y=205)
        self.intelligenceLabel.place(x=25, y=230)

    def addStatBonus(self):
        """Applies the stat bonuses.
        Endurance = +5 hp
        Intelligence = +5 mp
        Strength = +1 damage
        Agility = +1 crit chance"""
        self.charStats["Hit Points"] += (self.charStats["Endurance"] * 5)
        self.charStats["Mana Points"] += (self.charStats["Intelligence"] * 5)
        self.charStats["Damage"] += self.charStats["Strength"]
        self.charStats["Critical Chance"] += self.charStats["Agility"]

    # The rest of the methods are to clear the various menus of their widgets
    def clearNameMenu(self):
        """clears widgets on the name selection menu"""
        self.mainLabel.destroy()
        self.nameNext.destroy()
        self.charNameEntry.destroy()

    def clearRaceMenu(self):
        """Clears widgets on race selection window"""
        self.mainLabel.destroy()
        self.humanButton.destroy()
        self.orcButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.raceNext.destroy()

    def clearClassMenu(self):
        """Clears widgets on class selection window"""
        self.mainLabel.destroy()
        self.fighterButton.destroy()
        self.wizardButton.destroy()
        self.rogueButton.destroy()
        self.classNext.destroy()

    def clearStatMenu(self):
        """Clears widgets on the stat selection window"""
        self.strLabel.destroy()
        self.strNum.destroy()
        self.strUp.destroy()
        self.strDown.destroy()
        self.endLabel.destroy()
        self.endNum.destroy()
        self.endUp.destroy()
        self.endDown.destroy()
        self.agiLabel.destroy()
        self.agiNum.destroy()
        self.agiUp.destroy()
        self.agiDown.destroy()
        self.intLabel.destroy()
        self.intNum.destroy()
        self.intUp.destroy()
        self.intDown.destroy()
        self.finalizeButton.destroy()
        self.remainingLabel.destroy()
        self.remainingNumber.destroy()
        self.mainLabel.destroy()


    def exitCreateMenu(self):
        """Exits to main menu from create window"""
        self.window.destroy()


class helpScreen:
    """The help screen will be displayed after a user clicks the "help" button on the main screen.
    It will display a brief discription of the application, and will have a button to exit to the
    main menu."""
    def __init__(self):
        # This is the message that will be displayed on the help screen.
        self.helpText = """
This program will allow you to create a 
character to be used in a tabletop RPG. 
First you will be asked to choose a name, 
then a race, and finally a class. After 
that, you will have 10 stat points to 
spend on your four main attributes. After 
you click finalize, a character sheet will 
be generated with various information.
                
The stats you choose will have an effect 
on the final character sheet. You start
with 10 health, 10 mana, 1 damage, and 
5% critical strike chance.
+1 Strength = +1 damage
+1 Agility = +1% crit chance
+1 Endurance = +5 health
+1 Intelligence = +5 mana
                """
        #  Create new window
        self.helpWindow = tk.Toplevel()
        self.helpWindow.resizable = (False, False)  # Sets x and y resizable to false
        self.frame = tk.Frame(self.helpWindow, width=300, height=400)  # set window size
        self.frame.pack()
        # create exit button and help message
        self.exitHelp = tk.Button(self.helpWindow, text="Exit to Main Menu", command=self.exitHelpMenu)
        self.helpLabel = tk.Label(self.helpWindow, text=self.helpText, font=("bold", 12))
        # place widgets
        self.exitHelp.place(x=90, y=360)
        self.helpLabel.place(x=2, y=10)


    def exitHelpMenu(self):
        """Exits to main menu from help window"""
        self.helpWindow.destroy()

if __name__ == "__main__":
    window = CharacterGenerator(root)
    root.mainloop()

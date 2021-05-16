#!/usr/bin/env python3
import os, time, sys, pymysql, platform
import StartupNotes, iodecor
from StartupNotes import mycursor, addnote, removenote
from iodecor import centertext, colorText
from Note import *






# Will find a way to exclude 'clear' code block on the first run so then we can see ^^ direct/indirect execution statements from all referenced files
clean = ""
if platform.system() == "Windows":
   clean = "cls"
else:
   clean = "clear"

# VARIABLES
line = "\n" + iodecor.colorText("[[cyan]]#" * os.get_terminal_size().columns) + "\n"
db = "Notes"



# DISPLAY LIST OF NOTES
def displaynotes():
   print(line)
   StartupNotes.mycursor.execute("SELECT * FROM " + db)
   for note in StartupNotes.mycursor:
      print(iodecor.colorText("[[white]]" + str(note[0])) + ". " + iodecor.colorText("[[white]]" + note[1]))
   print(line + iodecor.colorText("[[RESET]]"))

# CONFIRM TO ADD/REMOVE NOTE
def confirmation():
   confirm = input("Confirm! (y/n)")
   if confirm == "y":
      return True
   else:
      return False

# INTERFACE: USER INPUT
def askUserForNote():
   noteinput = input("Note: ")
   noteID = 1
   StartupNotes.mycursor.execute("SELECT * FROM " + db)
   # Finds the last inserted noteID in the database
   for note in StartupNotes.mycursor:
      noteID = note[0] + 1
   # New note object created
   newNote = Note(noteID, noteinput)
   StartupNotes.addnote(newNote)

def askUserToRemoveNote():
   valid = False
   print("Enter the number of a note...")
   # Input validation: integer only
   while valid != True:
      try:
         noteID = int(input("#: "))
         valid = True
      except ValueError:
         print("This is not a valid ID #.")
   StartupNotes.mycursor.execute("SELECT * FROM " + db)
   # Assures noteID exists in the database
   for note in StartupNotes.mycursor:
      if int(noteID) != note[0]:
         print("Note does not exist.") # loops many times; will find another way to display this 
      elif int(noteID) == note[0]:
         # Confirm to remove note (y/n)
         if confirmation() == True:
            StartupNotes.removenote(noteID)
         break

################### In Progress ###################
def askUserToEditNote():
   oldNoteID = input("Enter the number of a note to rearrange priority: ")
   StartupNotes.mycursor.execute("SELECT * FROM Notes WHERE noteID = %s", (oldNoteID))
   newNoteID = input("Enter new number: ")
   oldNote = Note(0, "")
   newNote = Note(0, "")
   for note in StartupNotes.mycursor:
      print(note)
      if oldNoteID == note[0]:
         oldNote = Note(oldNoteID, note[1])
         newNote = Note(newNoteID, note[1])
         break
   print("dsad")
   StartupNotes.editnote(oldNote, newNote)
###################################################

# INTERFACE
def _NOTES_():
   run = 1
   while run == 1:
      os.system(clean)
      print(
        iodecor.colorText("[[blue]] _   _  ____ _______ ______  _____\n") +
        iodecor.colorText("[[blue]]| \ | |/ __ \__   __|  ____|/ ____|\n") +
        iodecor.colorText("[[blue]]|  \| | |  | | | |  | |__  | (___ \n") +
        iodecor.colorText("[[cyan]]| . ` | |  | | | |  |  __|  \___ \ \n") +
        iodecor.colorText("[[cyan]]| |\  | |__| | | |  | |____ ____) |\n") +
        iodecor.colorText("[[white]]|_| \_|\____/  |_|  |______|_____/ \n")
      )
      displaynotes()
      print(
         iodecor.centertext("1) ADD NOTE") + "\n" +
         iodecor.centertext("2) REMOVE NOTE") + "\n" +
         # iodecor.centertext("3) EDIT NOTE") + "\n" +
         iodecor.centertext("3) EXIT")
      )
      choice = input("Choose: ")
      if choice == "1":
         askUserForNote()
      elif choice == "2":
         askUserToRemoveNote()
      # elif choice == "3":      
      #   askUserToEditNote()
      elif choice == "3":
         print("Exiting...")
         run = 0
      else:
         print(iodecor.centertext("Choose a valid choice."))

# RUN
_NOTES_()

#!/usr/bin/env python3

import os, time, sys, pymysql, platform
from Note import *



if __name__ == '__main__':
   print("\nExecuted \'" + os.path.basename(__file__) + "\' directly.\n")
else:
   print("\nExecuted \'" + os.path.basename(__file__) + "\' indirectly.\n")




# DATABASE
db = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "password", # $password
        database = "NOTES"
)
mycursor = db.cursor()
mycursor.execute("USE NOTES")



### DATA ###
# Add note by object itself (Note)
def addnote(newNote):
   mycursor.execute("INSERT INTO Notes(noteID, note) VALUES(%s, %s)", (newNote.getNoteID(), newNote.getNote()))
   db.commit()

# Remove note by its ID (noteID)
def removenote(noteID):
   mycursor.execute("DELETE FROM Notes WHERE noteID = %s", (noteID))
   db.commit()

# Edit note by old and new object (Note) - In Progress
# def editnote(oldNote, newNote):
#   mycursor.execute("DELETE FROM Notes WHERE noteID = %s", (oldNote.getNoteID()))
#   mycursor.execute("INSERT INTO Notes(noteID, note) VALUES(%s, %s)", (newNote.getNoteID(), newNote.getNote()))
#   db.commit()



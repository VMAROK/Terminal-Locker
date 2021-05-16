#!/usr/bin/env python3





class Note:

   noteID = 0
   note = ""

   def __init__(self, noteID, note):
      self.noteID = noteID
      self.note = note

   def getNoteID(self):
      return self.noteID

   def setNoteID(self, noteID):
      self.noteID = noteID

   def getNote(self):
      return self.note

   def setNote(self, note):
      self.note = note

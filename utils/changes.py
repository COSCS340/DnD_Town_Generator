# Undo/Redo Stack (urstack)
# Purpose: Provides general purpose undo and redo functions using dictionaries
# Author:  Ben Johnson

class Changes:
    def __init__(self):
        self.undos = []
        self.redos = []

    def log(self, change):
        self.undos.append(change)
        if len(self.redos) != 0: self.redos.clear()

    def undo(self):
        if len(self.undos) != 0:
            change = self.undos.pop()
            self.redos.append(change)
            return change
        else: return None

    def redo(self):
        if len(self.redos) != 0:
            change = self.redos.pop()
            self.undos.append(change)
            return change
        else: return None

    def canUndo(self):
        if len(self.undos) == 0: return False
        else: return True

    def canRedo(self):
        if len(self.redos) == 0: return False
        else: return True

    def clear(self):
        self.undos.clear()
        self.redos.clear()

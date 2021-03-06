class CellOverwriteError(Exception):
    '''
    Exception raised when attempting to overwrite a previously-solved cell.

    Attributes:
        new_val -- the new value trying to be written
        preexisting_val -- the pre-existing value
        message -- explanation of the error
    '''

    def __init__(self, old, message='Cell has already been solved!'):
        self.old = old
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} --> Cell value = {self.old}'

        

class Cell:

    def __init__(self, coords, val=None):
        self.value = val
        self.possibles = None if val else [1,2,3,4,5,6,7,8,9]
        self.coords = coords
        self.row = coords[0]
        self.col = coords[1]
        self.box = coords[2]
        
    def set_possibles(self, possibles):
        if self.value:
            raise CellOverwriteError(self.value)
        else:
            self.possibles = possibles

    def remove_possibles(self, impossibles):
        for impossible in impossibles:
            self.possibles.remove(impossible)

    def set(self, val):
        if self.value:
            raise CellOverwriteError(self.value)
        else:
            self.value = val
            self.possibles = None

    def getVal(self):
        return self.value

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getBox(self):
        return self.box

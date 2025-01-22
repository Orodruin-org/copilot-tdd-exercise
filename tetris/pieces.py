from enum import Enum

class TetrominoType(Enum):
    I = 1
    O = 2
    T = 3
    S = 4
    Z = 5
    J = 6
    L = 7

class Piece:
    def __init__(self, tetromino_type):
        self.type = tetromino_type
        # For demonstration, store a shape as a list of coordinates or something similar
        # e.g., for an I piece, a simple placeholder could be:
        if self.type == TetrominoType.I:
            self.shape = [(0,0), (0,1), (0,2), (0,3)]
        elif self.type == TetrominoType.O:
            self.shape = [(0,0), (0,1), (1,0), (1,1)]
        elif self.type == TetrominoType.T:
            self.shape = [(0,1), (1,0), (1,1), (1,2)]
        elif self.type == TetrominoType.S:
            self.shape = [(0,1), (0,2), (1,0), (1,1)]
        elif self.type == TetrominoType.Z:
            self.shape = [(0,0), (0,1), (1,1), (1,2)]
        elif self.type == TetrominoType.J:
            self.shape = [(0,0), (1,0), (1,1), (1,2)]
        elif self.type == TetrominoType.L:
            self.shape = [(0,2), (1,0), (1,1), (1,2)]
        else:
            self.shape = []
    
    def rotate(self):
        """Rotate the piece 90 degrees in place."""
        if self.type == TetrominoType.I:
            self.shape = [(y, -x) for x, y in self.shape]
        elif self.type == TetrominoType.O:
            pass  # O piece does not change shape on rotation
        elif self.type == TetrominoType.T:
            self.shape = [(y, -x) for x, y in self.shape]
        elif self.type == TetrominoType.S:
            self.shape = [(y, -x) for x, y in self.shape]
        elif self.type == TetrominoType.Z:
            self.shape = [(y, -x) for x, y in self.shape]
        elif self.type == TetrominoType.J:
            self.shape = [(y, -x) for x, y in self.shape]
        elif self.type == TetrominoType.L:
            self.shape = [(y, -x) for x, y in self.shape]

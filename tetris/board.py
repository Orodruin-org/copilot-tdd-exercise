class Board:
    def __init__(self, rows=20, columns=10):
        """Initialize the game board with the specified number of rows and columns."""
        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns must be positive integers.")
        self.rows = rows
        self.columns = columns
        self.grid = [['' for _ in range(columns)] for _ in range(rows)]
    
    def is_cell_empty(self, row, col):
        """Check if the cell at (row, col) is empty."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise IndexError("Cell position out of bounds.")
        return self.grid[row][col] == ''
    
    def place_block(self, row, col, block_type):
        """Place a block at (row, col). block_type is a simple string or enum."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise IndexError("Cell position out of bounds.")
        self.grid[row][col] = block_type

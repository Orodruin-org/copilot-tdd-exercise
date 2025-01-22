# TDD Tetris with Copilot

Welcome to the TDD Tetris project. This repository demonstrates how to build a simple Tetris game in Python using Test-Driven Development (TDD) in tandem with GitHub Copilot or a similar AI-assisted coding tool.

## Table of Contents  
1. Overview  
2. Features and Final Game Description  
3. Requirements  
4. Setup Instructions  
   - Windows  
   - macOS and Linux  
5. Running the Tests  
6. Running the Program  
7. First 5 Test Cases  
8. Next Features to Implement  
9. Using TDD with Copilot  
10. Contributing  

---

## 1. Overview  
- Language: Python  
- Testing Framework: Pytest  
- Goal: Provide a skeleton Tetris game where participants learn TDD by writing tests first, watching them fail, then using Copilot to implement code until the tests pass.

---

## 2. Features and Final Game Description  
When fully implemented, this Tetris clone should include:  

- A 20×10 grid representing the Tetris board  
- Standard Tetris shapes (I, O, T, S, Z, J, L) spawning at the top  
- Movement (left, right, down) and rotation for each piece  
- Line clearing when a row is completely filled  
- Score and level tracking, with speed increasing after certain cleared lines  
- Game over detection when no space is left to place a new piece  

Initially, the game is incomplete. You will use TDD and Copilot to build it step by step.

---

## 3. Requirements  
1. Python 3.8 or later and pip
2. Git if you plan to clone this repository  
3. A code editor or IDE with optional Copilot integration

---

## 4. Setup Instructions  

### Windows  
1. Open a command prompt or PowerShell in the project folder  
2. Create a virtual environment by running:
   python -m venv venv
3. Activate the virtual environment:
   For Command Prompt: venv\Scripts\activate
   For PowerShell: .\venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt

### macOS and Linux  
1. Open a terminal in the project folder  
2. Create a virtual environment by running:  
   python3 -m venv venv  
3. Activate the virtual environment:  
   source venv/bin/activate  
4. Install dependencies:  
   pip install -r requirements.txt  

If there is no requirements file, simply install the pytest package by running pip install pytest.

---

## 5. Running the Tests  
Within the project folder and with your virtual environment activated, run this command:  

pytest  

All tests in the tests directory will run. You will initially see many failures, which is expected. Use TDD to implement the features until these tests pass.

---

## 6. Running the Program  
Currently, the repository does not have a dedicated main script to start the game loop. However, you can create one (for example, main.py) and run:

python main.py

Alternatively, you can develop a main loop or a graphical interface once you have the core logic. For now, focus on building out the Tetris features with TDD. Once you are ready, you can integrate all parts into a playable game.

---

## 7. First 5 Test Cases  
Below are the initial tests you will encounter:

1. test_board_initialization  
   Tests that a Board is created with rows, columns, and a 2D grid of the correct size.

2. test_board_is_cell_empty  
   Ensures that a newly initialized Board reports its cells as empty.

3. test_board_place_block  
   Checks that placing a block changes a cell from empty to occupied.

4. test_piece_creation  
   Verifies that creating a Piece with type I has four segments.

5. test_piece_rotation  
   Confirms that rotating a piece changes its shape.

These tests will fail at first. You will fix them by writing just enough code to pass each test, then move on to the next.

---

## 8. Next Features to Implement  
After you have passed the initial tests, you can continue with your TDD approach to implement additional features. Remember, always write your tests first for each feature, let them fail, and then write the actual implementation. Some suggestions include:

1. Implement piece movement (left, right, down)
2. Complete piece rotation logic (including boundary checks)
3. Detect and clear full lines, shifting everything above down
4. Track scoring and level progression
5. Implement a game over state when new pieces cannot spawn
6. (Optional) Create a graphical or text-based interface for gameplay

The key is to expand your Tetris logic step by step, always guided by failing tests that you then make pass.

---

## 9. Using TDD with Copilot  
1. Review the failing test to see which assertion fails.  
2. Open the corresponding source file (for example, board.py or pieces.py) and the file containing the pertinent tests.
3. Begin implementing the required class or method by adding a docstring or partial signature. You can reference to a given file and a given function (test) to define that you want to make this piece pass.
4. Let Copilot suggest code; accept or refine the suggestions.  
5. Re-run the tests to confirm the fix.  
6. Continue until all tests pass.  

Example flow:  
- You see test_board_initialization fail because Board is missing rows, columns, or grid.  
- In board.py, implement the Board class with the required attributes.  
- Re-run tests until the failure is resolved.  
- Move to the next test.
- Run CI pipeline

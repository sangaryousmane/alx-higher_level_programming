#!/usr/bin/python3
"""Solves the N-queens puzzle"""


class Nqueens:
    """ Mimics the Nqueen puzzle"""

    def __init__(self):
        """ construct the class instance """
        pass

    def init_board(self, n):
        """Initialize an `n`x`n` sized chessboard with 0's."""
        board = []
        for i in range(n):
            board.append([])
        for i in range(n):
            for r in board:
                r.append(' ')
        return board

    def nqueen_copy(self, board):
        """Return a deepcopy of a chessboard."""
        if type(board) != list:
            return list(map(self.nqueen_copy, board))
        return (board)

    def nqueen_solvable(self, board):
        """Return the solved board."""
        sol = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    sol.append([r, c])
                    break
        return sol

    def xout(self, board, row, col):
        """ the X spots on a chessboard. """
        for c in range(col + 1, len(board)):
            board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            board[row][c] = "x"
        for r in range(row + 1, len(board)):
            board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, len(board)):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            board[r][c]
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, len(board)):
            if c < 0:
                break
            board[r][c] = "x"
            c -= 1

    def solve_recur(self, board, row, queens, sol):
        """solve the puzzle with recursion."""
        if queens == len(board):
            sol.append(self.nqueen_solvable(board))
            return (sol)
        for c in range(len(board)):
            if board[row][c] == " ":
                tmp_board = self.nqueen_copy(board)
                tmp_board[row][c] = "Q"
                self.xout(tmp_board, row, c)
                sol = self.solve_recur(tmp_board, row + 1, queens + 1, sol)
        return (sol)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueen = Nqueens()
    board = nqueen.init_board(int(sys.argv[1]))
    result = nqueen.solve_recur(board, 0, 0, [])
    for sol in result:
        print(sol)

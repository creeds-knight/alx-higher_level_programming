#!/usr/bin/python3

""" A class to solve the n queens problem """

class Solution:
    def solveQueens(self, n: int) -> list[list[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [".".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res


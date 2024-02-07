from django.test import TestCase
import numpy as np
# Create your tests here.
def is_valid(tbl, row, col, num):  #ایجاد تابع معتبربودن عدد با ورودی های جدول وسطر و ستون و عدد
    # بررسی معتبر بودن عدد در سطر
    for i in range(9):
        if tbl[row][i] == num:
            return False
    # بررسی معتبر بودن عدد در ستون
    for i in range(9):
        if tbl[i][col] == num:
            return False
    # بررسی معتبر بودن عدد در بلوک سه در سه
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if tbl[i][j] == num:
                return False
    return True

def solve_sudoku(tbl):
    empty_cell = find_empty_cell(tbl)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(tbl, row, col, num):
            tbl[row][col] = num
            if solve_sudoku(tbl):
                return True
            tbl[row][col] = 0
    return False

def find_empty_cell(tbl):
    for i in range(9):
        for j in range(9):
            if tbl[i][j] == 0:
                return (i, j)
    return None

                                               # نماد اولیه جدول سودوکو
sudoku_board = [                       #آرایه دوبعدی با مقادیر استاندارد جدول
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):            #در اینجا جدول را به عنوان ورودی به تابع حل سودوکو داده شده
    for row in sudoku_board:               #اگر جدول خالی باشد و عدد های
       print(row)
else:
    print("No solution exists")
print("\n▓-----------▓-----------▓-----------▓")
for i in range(9):
    print("▓ ",end="")
    for j in range(9):
        if j == 0 :
            print(sudoku_board[i][j],end=" | ")
        else:
            if j==8 or j==5 or j==2:
                print(sudoku_board[i][j],end=" ▓ ")  # alt +176
            else:
                print(sudoku_board[i][j], end=" | ")
    if i % 3 ==2:
        print("\n▓-----------▓-----------▓-----------▓")
    else:
        print("")

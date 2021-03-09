from typing import List

import mypy




class Matrix:

    def __init__(self, ls_2d: list):
        # ls_2d as a 2-dimensional list
        self.matrix = {}

        # column number fixed as len of ls_2d
        self.col_num = len(ls_2d)
        # decl max_row_len
        max_row_len = -1

        # iterate through ls_2d
        for i in range(len(ls_2d)):
            # row as current row in ls_2d
            row = ls_2d[i]
            # initialise dict in self.matrix[i]
            self.matrix[i] = {}
            # iterate through row, if row[j] not 0 then add key/value pair to dict
            for j in range(len(row)):
                if row[j] != 0:
                    self.matrix[i][j] = row[j]

            # since ls_2d may be ragged, size of matrix row length is max len of rows in ls_2d
            if len(row) > max_row_len:
                max_row_len = len(row)

        self.row_num = max_row_len

    def get_row_num(self) -> int:
        return self.row_num

    def get_col_num(self) -> int:
        return self.col_num

    def get_item(self, row_i: int, col_i: int):
        # check that indexes are valid
        if not self.is_valid_index(row_i, col_i):
            return None

        # if key exists in that row, return its value
        if col_i in self.matrix[row_i]:
            return self.matrix[row_i][col_i]
        # ow, it must be a 0
        else:
            return 0

    def is_valid_index(self, row_i: int, col_i: int) -> bool:
        return self.row_num > row_i >= 0 and self.col_num > col_i >= 0

    def swap_row(self, row_i_1: int, row_i_2: int):
        tmp = self.matrix[row_i_1]
        self.matrix[row_i_1] = self.matrix[row_i_2]
        self.matrix[row_i_2] = self.matrix[row_i_1]

    def get_submatrix(self, row_i: int, col_i: int):
        submatrix = [[None for i in range(self.row_num - 1)] for j in range(self.col_num - 1)]
        for i in range(self.row_num - 1):
            for j in range(self.col_num - 1):
                if i < row_i:
                    curr_row_i = i
                else:
                    curr_row_i = i + 1
                if j < col_i:
                    curr_col_i = j
                else:
                    curr_col_i = j + 1
                submatrix[i][j] = self.get_item(curr_row_i, curr_col_i)
        return Matrix(submatrix)

    def show(self):
        print("Showing a matrix")
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(self.get_item(i, j), end="\t")
            print("")

    def show_keys(self):
        print(self.matrix.keys())

    def get_row(self, row_i: int) -> list:
        ls = [0 for i in range(self.col_num)]
        for key in self.matrix[row_i]:
            ls[key] = self.get_item(row_i, key)
        return ls

    def get_col(self, col_i: int) -> list:
        ls = [0 for i in range(self.row_num)]
        for key in self.matrix:
            ls[key] = self.get_item(key, col_i)
        return ls

    def get_product(self, mat): # should ensure type here is a Matrix object):
        # check sizes of matrices match
        if not (self.row_num == mat.get_col_num() and self.col_num == mat.get_row_num()):
            # might need to throw exception here
            return None

        ls = [[None for i in range(self.row_num)] for j in range(mat.get_col_num())]
        for i in range(self.row_num):
            row = self.get_row(i)
            for j in range(mat.get_col_num()):
                col = mat.get_col(j)
                acc = 0
                for k in range(len(row)):
                    acc += row[k] * col[k]
                ls[i][j] = acc

        return Matrix(ls)

    def get_sum(self, mat):
        # check sizes of matrices match
        if not (self.row_num == mat.get_row_num() and self.col_num == mat.get_col_num()):
            # might need to throw exception here
            return None

        ls = [[None for i in range(self.row_num)] for j in range(self.col_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                ls[i][j] = self.get_item(i, j) + mat.get_item(i, j)

        return Matrix(ls)

    def mult_scalar(self, coeff: int):
        for r_i in self.matrix:
            for c_i in self.matrix[r_i]:
                self.matrix[r_i][c_i] *= coeff



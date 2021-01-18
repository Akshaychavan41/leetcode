class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for r_idx, r_val in enumerate(matrix):
            for c_idx, c_val in enumerate(matrix[r_idx]):
                if c_val == 0:
                    row_set.add(r_idx)
                    col_set.add(c_idx)
        for r_idx, r_val in enumerate(matrix):
            for c_idx, c_val in enumerate(matrix[r_idx]):
                if r_idx in row_set or c_idx in col_set:
                    matrix[r_idx][c_idx] = 0
                   
                
                

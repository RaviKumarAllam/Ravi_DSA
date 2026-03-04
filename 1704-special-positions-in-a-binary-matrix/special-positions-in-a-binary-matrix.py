class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
        row_sums = [0] * num_rows
        col_sums = [0] * num_cols
        for i in range(num_rows):
            for j in range(num_cols):
                value = mat[i][j]
                row_sums[i] += value
                col_sums[j] += value
        special_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
      
        return special_count    
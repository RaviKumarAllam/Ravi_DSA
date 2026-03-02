class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rightmost_one_positions = [-1] * n
      
        for row_idx in range(n):
            for col_idx in range(n - 1, -1, -1):
                if grid[row_idx][col_idx] == 1:
                    rightmost_one_positions[row_idx] = col_idx
                    break
      
        total_swaps = 0
        for target_row in range(n):
            suitable_row_idx = -1
          
            for candidate_row in range(target_row, n):
                if rightmost_one_positions[candidate_row] <= target_row:
                    total_swaps += candidate_row - target_row
                    suitable_row_idx = candidate_row
                    break
            if suitable_row_idx == -1:
                return -1
            while suitable_row_idx > target_row:
                rightmost_one_positions[suitable_row_idx], rightmost_one_positions[suitable_row_idx - 1] = \
                    rightmost_one_positions[suitable_row_idx - 1], rightmost_one_positions[suitable_row_idx]
                suitable_row_idx -= 1
      
        return total_swaps
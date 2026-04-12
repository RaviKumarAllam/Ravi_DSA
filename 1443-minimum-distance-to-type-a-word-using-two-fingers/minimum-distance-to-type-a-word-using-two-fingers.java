class Solution {
    public int minimumDistance(String word) {
        int n = word.length();
        final int INF = 1 << 30;
        int[][][] dp = new int[n][26][26];
      
        for (int[][] row : dp) {
            for (int[] cell : row) {
                Arrays.fill(cell, INF);
            }
        }
        int firstChar = word.charAt(0) - 'A';
        for (int j = 0; j < 26; ++j) {
            dp[0][firstChar][j] = 0;  
            dp[0][j][firstChar] = 0; 
        }
      
        for (int i = 1; i < n; ++i) {
            int prevChar = word.charAt(i - 1) - 'A';
            int currChar = word.charAt(i) - 'A';
            int distance = dist(prevChar, currChar);
          
            for (int j = 0; j < 26; ++j) {
                dp[i][currChar][j] = Math.min(dp[i][currChar][j], dp[i - 1][prevChar][j] + distance);
                dp[i][j][currChar] = Math.min(dp[i][j][currChar], dp[i - 1][j][prevChar] + distance);
              
              
                if (j == prevChar) {
                    for (int k = 0; k < 26; ++k) {
                        int moveDistance = dist(k, currChar);
                       
                        dp[i][currChar][j] = Math.min(dp[i][currChar][j], dp[i - 1][k][prevChar] + moveDistance);
                      
                        dp[i][j][currChar] = Math.min(dp[i][j][currChar], dp[i - 1][prevChar][k] + moveDistance);
                    }
                }
            }
        }
        int result = INF;
        int lastChar = word.charAt(n - 1) - 'A';
        for (int j = 0; j < 26; ++j) {
            result = Math.min(result, dp[n - 1][j][lastChar]); 
            result = Math.min(result, dp[n - 1][lastChar][j]); 
        }
      
        return result;
    }
    private int dist(int a, int b) {
        int row1 = a / 6, col1 = a % 6;
        int row2 = b / 6, col2 = b % 6;
        return Math.abs(row1 - row2) + Math.abs(col1 - col2);
    }
}

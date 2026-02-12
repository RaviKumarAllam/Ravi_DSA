class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            cnt = [0] * 26
            mx = 0
            v = 0
            for j in range(i, n):
                c = ord(s[j]) - ord('a')
                cnt[c] += 1
                if cnt[c] == 1:
                    v += 1

                if cnt[c] > mx:
                    mx = cnt[c]
                current_len = j - i + 1
                if mx * v == current_len:
                    ans = max(ans, current_len)

        return ans      
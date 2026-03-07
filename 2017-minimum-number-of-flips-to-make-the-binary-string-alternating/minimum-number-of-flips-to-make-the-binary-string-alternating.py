class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        tar_p = "01"
        m_count = sum(char != tar_p[i & 1] for i, char in enumerate(s))
        m_flips = min(m_count, n - m_count)
        for i in range(n):
            m_count -= s[i] != tar_p[i & 1]
            m_count += s[i] != tar_p[(i + n) & 1]
            m_flips = min(m_flips, m_count, n - m_count)
      
        return m_flips    
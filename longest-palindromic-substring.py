class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        if s == s[0] * n:
            return s

        from collections import defaultdict
        char_indices = defaultdict(list)
        for i, ch in enumerate(s):
            char_indices[ch].append(i)

        max_len = 0
        start = 0

        def expand(l, r):
            nonlocal max_len, start
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > max_len:
                max_len = r - l - 1
                start = l + 1

        for indices in char_indices.values():
            k = len(indices)
            if k == 1:
                continue
            expand((indices[0] + indices[-1]) // 2, (indices[0] + indices[-1]) // 2)
            expand((indices[0] + indices[-1]) // 2, (indices[0] + indices[-1]) // 2 + 1)

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return s[start:start + max_len]

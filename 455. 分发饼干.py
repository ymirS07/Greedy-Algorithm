class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        g.sort()
        s.sort()
        idx = len(s) - 1
        for i in range(len(g) - 1, -1, -1):
            if idx >= 0 and s[idx] >= g[i]:
                cnt += 1
                idx -= 1
        return cnt
# 排序 + 双指针 + 贪心

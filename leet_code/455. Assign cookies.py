# 첫 풀이
# 한 아이당 최대 한개의 쿠키를 줄 수 있는 조건을 놓침.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        if not s:
            return 0

        cookies = collections.Counter(s)

        heap = []
        result = 0

        g.sort()

        for size, count in cookies.items():
            heapq.heappush(heap, (size, count))

        for content in g:
            while heap:
                size, count = heapq.heappop(heap)
                content -= size

                if count - 1 > 0:
                    heapq.heappush(heap, (size, count - 1))

                if content <= 0:
                    result += 1
                    break

        return result


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        return
        -------
        result : int
        만족한 아이들의 수
        """

        if not s:
            return 0

        g.sort()
        s.sort()

        result = 0

        i = 0
        j = 0

        while i < len(g) and j < len(s):

            if g[i] <= s[j]:
                result += 1
                i += 1
            j += 1

        return result

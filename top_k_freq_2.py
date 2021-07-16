class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = collections.Counter(nums)
        freq_heap = []

        for f in freqs:
            heapq.heappush(freq_heap, (-freqs[f], f))

        upper = []

        for i in range(k):
            upper.append(heapq.heappop(freq_heap)[1])

        return upper

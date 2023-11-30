class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heap.append((distance, point))
        output = []
        heapq.heapify(heap)
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
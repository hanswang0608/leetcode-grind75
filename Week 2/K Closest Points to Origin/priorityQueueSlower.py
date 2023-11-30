from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = PriorityQueue()
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            queue.put((distance, point))
        output = []
        for i in range(k):
            output.append(queue.get()[1])
        return output
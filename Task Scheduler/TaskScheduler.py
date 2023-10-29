from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCounter = Counter(tasks)
        tasksDict = dict(sorted(tasksCounter.items(), key=lambda x: x[1], reverse=True))
        timeDict = {}
        
        def canDo(task, curTime):
            if not task in timeDict or timeDict[task] < curTime:
                timeDict[task] = curTime + n
                return True
            else:
                return False

        time = 1
        while tasksDict:
            didTask = False
            for task in tasksDict:
                if canDo(task, time):
                    print(time, task)
                    tasksDict[task] -= 1
                    if tasksDict[task] == 0:
                        tasksDict.pop(task)
                    didTask = True
                    break
            if not didTask:
                print(time, 'idle')
            time += 1
            
        return time-1

solution = Solution()
tasks = ["A","A","A","B","B","B"]
tasks2 = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(solution.leastInterval(tasks, n))
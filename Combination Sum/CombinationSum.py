class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(target, candidates, candidate = None):
            if target == 0:
                return [[candidate]]
            if target < 0:
                return None
            paths = []
            for i, num in enumerate(candidates):
                ret = dfs(target-num, candidates[i:], num)
                if not ret:
                    continue
                for path in ret:
                    if candidate:
                        paths.append([candidate] + path)
                    else:
                        paths.append(path)
            return paths
        
        return dfs(target, candidates)

solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
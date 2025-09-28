from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinationSumHelper(start: int, cur_sum: int, cur_comb: List[int]):
            if cur_sum == target:
                result.append(cur_comb[:])
                return
                
            if cur_sum > target:
                return
            
            for i in range(start, len(candidates)):
                cur_comb.append(candidates[i])
                combinationSumHelper(i, cur_sum + candidates[i], cur_comb)
                cur_comb.pop()

        combinationSumHelper(0, 0, [])
        return result

            

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
         
        dfs(0, [], 0)
        return res
                
            

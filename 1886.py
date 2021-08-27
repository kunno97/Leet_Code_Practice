class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        check1, check2, check3, check4 = True, True, True, True
        
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    check1 = False
                    break
                    
        if check1: return True
        
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[c][n - r - 1]:
                    check2 = False
                    break
                    
        if check2: return True
        
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n - r - 1][n - c - 1]:
                    check3 = False
                    break
                    
        if check3: return True
        
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n - c - 1][r]:
                    check4 = False
                    break
                    
        if check4: return True
        
        return False

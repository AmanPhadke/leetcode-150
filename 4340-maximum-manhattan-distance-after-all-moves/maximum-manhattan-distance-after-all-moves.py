class Solution(object):
    def maxDistance(self, move):
        x, y = 0 , 0 

        l = 0
        count = move.count('_')

        while l < len(move):
            if move[l] == 'L':
                x -= 1
            elif move[l] == 'R':
                x += 1
            elif move[l] == 'U':
                y += 1
            elif move[l] == 'D':
                y -= 1
            
            l += 1

        manhattan = abs(0 - (x)) + abs(0 - (y))
        manhattan += count
        
        return manhattan
import collections
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q=deque()
        visited=set()
        q.append((sr,sc))
        color = image[sr][sc]
        image[sr][sc]=newColor
        visited.add((sr,sc))
        while(len(q)>0):
            r,c = q.pop()
            def fillColor(r,c):
                if(r>=0 and r<len(image) and c>=0 and c<len(image[0]) and (r,c) not in visited and image[r][c]==color):
                    q.append((r,c))
                    visited.add((r,c))
                    image[r][c] = newColor
            fillColor(r-1,c)
            fillColor(r+1,c)
            fillColor(r,c-1)
            fillColor(r,c+1)
        return image
                
                

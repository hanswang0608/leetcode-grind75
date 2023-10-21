class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (image[sr][sc] == color):
            return image
        oldColor = image[sr][sc]
        image[sr][sc] = color
        # Check up
        if (sr > 0 and image[sr-1][sc] == oldColor):
            image = self.floodFill(image, sr-1, sc, color)
        # Check right
        if (sc < len(image[sr])-1 and image[sr][sc+1] == oldColor):
            image = self.floodFill(image, sr, sc+1, color)
        # Check down
        if (sr < len(image)-1 and image[sr+1][sc] == oldColor):
            image = self.floodFill(image, sr+1, sc, color)
        # Check left
        if (sc > 0 and image[sr][sc-1] == oldColor):
            image = self.floodFill(image, sr, sc-1, color)
        return image
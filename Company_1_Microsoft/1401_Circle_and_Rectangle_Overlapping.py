class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        X = max(x1, min(xCenter , x2))
        Y = max(y1, min(yCenter , y2))
        return ((X - xCenter) ** 2 + (Y - yCenter) ** 2) <= (radius) ** 2
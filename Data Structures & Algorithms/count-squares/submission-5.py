class CountSquares:

    points: list[tuple[int, int]]
    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append((point[0], point[1]))

    def count(self, point: List[int]) -> int:
        horzCount: dict[int, int] = {}
        vertCount: dict[int, int] = {}
        diag13Count: dict[int, int] = {}
        diag24Count: dict[int, int] = {}
        
        # print('Query', point)
        for pt in self.points:
            dx, dy = point[0] - pt[0], point[1] - pt[1]
            if dx == 0 and dy == 0:
                continue
            # print(pt, dx, dy)

            if dx == 0:
                vertCount[dy] = vertCount.get(dy, 0) + 1
            if dy == 0:
                horzCount[dx] = horzCount.get(dx, 0) + 1
            
            if dx == dy:
                diag13Count[dx] = diag13Count.get(dx, 0) + 1
            elif dx == -dy:
                diag24Count[dx] = diag24Count.get(dx, 0) + 1
            
        # print('h  ', horzCount)
        # print('v  ', vertCount)
        # print('d13', diag13Count)
        # print('d24', diag24Count)
        
        squares: int = 0
        for dist, count in horzCount.items():
            if vertCount.get(dist) and diag13Count.get(dist):
                squares += count * vertCount[dist] * diag13Count[dist]
            if vertCount.get(-dist) and diag24Count.get(dist):
                squares += count * vertCount[-dist] * diag24Count[dist]
        
        return squares

        

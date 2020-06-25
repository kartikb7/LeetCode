import numpy as np

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return None

        max_time = len(grid) * len(grid[0])
        minute = -1
        not_found = True

        grid_np = np.asarray(grid)

        while not_found and minute < max_time:
            rotten_spots = []
            not_found = False
            for i in range(grid_np.shape[0]):
                for j in range(grid_np.shape[1]):
                    if grid_np[i, j] == 2:
                        rotten_spots.append([i, j])
                    if grid_np[i, j] == 1:
                        not_found = True

            for i in rotten_spots:
                self.rot_adjacent(grid_np, i[0] + 1, i[1])
                self.rot_adjacent(grid_np, i[0], i[1] + 1)
                self.rot_adjacent(grid_np, i[0] - 1, i[1])
                self.rot_adjacent(grid_np, i[0], i[1] - 1)

            minute += 1

        if not not_found:
            return minute
        else:
            return -1

    def rot_adjacent(self, grid_np, i, j):
        if i < 0 or j < 0 or i >= len(grid_np) or j >= len(grid_np[0]):
            return
        else:
            if grid_np[i, j] == 1:
                grid_np[i, j] = 2


import numpy as np


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_np = np.asarray(grid)
        island_count = 0
        for i in range(grid_np.shape[0]):
            for j in range(grid_np.shape[1]):
                if (grid_np[i, j]) == '1':
                    island_count += 1
                    self.destroy_island(grid_np, i, j)
                    if i < grid_np.shape[1] - 1:
                        j += 1
        return island_count

    def destroy_island(self, grid_np_test, i, j):
        grid_np_test[i, j] = 0
        if i > 0:
            if (grid_np_test[i - 1, j]) == '1':
                self.destroy_island(grid_np_test, i - 1, j)
        if j > 0:
            if (grid_np_test[i, j - 1]) == '1':
                self.destroy_island(grid_np_test, i, j - 1)
        if i < grid_np_test.shape[0] - 1:
            if (grid_np_test[i + 1, j]) == '1':
                self.destroy_island(grid_np_test, i + 1, j)
        if j < grid_np_test.shape[1] - 1:
            if (grid_np_test[i, j + 1]) == '1':
                self.destroy_island(grid_np_test, i, j + 1)

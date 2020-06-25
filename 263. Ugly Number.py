class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        if num == 1:
            return True

        for val in [2, 3, 5]:
            while num % val == 0:
                num = num / val

        return num == 1

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
            count = 0
            not_found = True
            minute = 0

            self.grid_np = np.asarray(grid)

            # while not_found and count<max_time:
            #     not_found == False
            rotten_spots = []
            for i in range(self.grid_np.shape[0]):
                for j in range(self.grid_np.shape[1]):
                    if self.grid_np[i, j] == 2:
                        rotten_spots.append([i, j])

            print(rotten_spots)
            for i in rotten_spots:
                self.rot_adjacent(i[0] + 1, i[1])
                self.rot_adjacent(i[0], i[1] + 1)
                self.rot_adjacent(i[0] - 1, i[1])
                self.rot_adjacent(i[0], i[1] - 1)

            print(self.grid_np)

            if not not_found:
                return count
            else:
                return -1

        def rot_adjacent(self, i, j):
            if i < 0 or j < 0 or i >= len(self.grid_np) or j >= len(self.grid_np[0]):
                return
            else:
                if self.grid_np[i, j] == 1:
                    print('i:' + str(i) + ',j:' + str(j))
                    self.grid_np[i, j] == 2



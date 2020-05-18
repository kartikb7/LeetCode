
filesSent = True
NumofHours = 0

while filesSent:
	NumofHours += 1
	filesSent = False
	For i in range(rows):
	For j in range(columns):
		if grid[i][j] == 0:
			filesSent = True
For i in range(rows):
	For j in range(columns):
		if grid[i][j] == 1:
			sendfile(grid, i+1,j)
	sendfile(grid, i-1,j)
	sendfile(grid, i,j+1)
	sendfile(grid, i,j-1)

Def sendfile(grid,i,j):
	if(i<0):
Return
elif i>=len(grid):
	Return
elif j<0:
Return
elif j>=len(grid[i]):
Return
elif grid[i,j] == 1):
Return None
Else:
	Grid[i][j] = 1
	Return

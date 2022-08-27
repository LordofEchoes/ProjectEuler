# Brute force method of just checking 4 directions, down, bottom left, bottom right, and right

def inputGenerate(square, filename, length = 20):
	file = open(filename)
	for outer,line in enumerate(file.readlines()):
		line_list = line.split()
		for inner,num in enumerate(line_list):
			# print(int(i/length), int(i%length))
			square[int(outer)][int(inner)] = int(num)

def checkSolution(sol, temp_sol):
	if sol > temp_sol:
		return sol
	else:
		return temp_sol


def findSolution(db):
	sol = db[0][0]*db[0][1]*db[0][2]*db[0][3]
	for row_index,row in enumerate(db):
		for col_index, col in enumerate(row):
			temp_sol = 1
			#check right
			if col_index+3 < 20:
				temp_sol = db[row_index][col_index]
				temp_sol *= db[row_index][col_index+1]
				temp_sol *= db[row_index][col_index+2]
				temp_sol *= db[row_index][col_index+3]
			sol = checkSolution(sol, temp_sol)
			#check down
			if row_index+3 < 20:
				temp_sol = db[row_index][col_index]
				temp_sol *= db[row_index+1][col_index]
				temp_sol *= db[row_index+2][col_index]
				temp_sol *= db[row_index+3][col_index]
			sol = checkSolution(sol, temp_sol)
			#check bottomleft:
			if row_index+3 < 20 and col_index-3 > -1:
				temp_sol = db[row_index][col_index]
				temp_sol *= db[row_index+1][col_index-1]
				temp_sol *= db[row_index+2][col_index-2]
				temp_sol *= db[row_index+3][col_index-3]
			sol = checkSolution(sol, temp_sol)
			#check bottomright:
			if row_index+3 < 20 and col_index+3 < 20:
				temp_sol = db[row_index][col_index]
				temp_sol *= db[row_index+1][col_index+1]
				temp_sol *= db[row_index+2][col_index+2]
				temp_sol *= db[row_index+3][col_index+3]
			sol = checkSolution(sol, temp_sol)
	return sol




db = [[0 for i in range(20)] for j in range(20)]
inputGenerate(db, "Euler11_file", 20)
solution = findSolution(db)
print(solution)
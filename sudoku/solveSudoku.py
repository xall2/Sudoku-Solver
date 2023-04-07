from sudoku import *
from tkinter import *
import time
import os


os.system("start GAME.wav")


'''
@author: alaa
@author: safa
'''
"""**************************************************************************"""
def Backtracking():
 root =Tk()
 root.geometry("420x520")
 root.rowconfigure([0, 1, 2, 3,4,5,6,7,8,9], minsize=50)
 root.columnconfigure([0, 1, 2, 3], minsize=50)
 root.title("Backtracking Sudoku Game")
#sudoku
 sudoku1=readsudokuEasy()
 sudoku2=readsudokuMedium()
 sudoku3=readsudokuHard()

 def printsudoku(sudoku):
    line = ""
    j=0
    for i in range(len(sudoku)):
        if j==8:
         line += "\n"
        if i == 3 or i == 6:
            line += "-------------------------\n"
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            
            line += str(sudoku[i][j])+"  "
        #print(line)
    return line


 
    
 def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


 def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False



 def solveSudoku(sudoku, i=0, j=0):
    i, j = findNextCellToFill(sudoku) 
    if i == -1:
        return True
    for e in range(1, 10): 
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>EasySudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def easysolve():
   label3 =Label(root,text=printsudoku(sudoku1), fg="blue").grid(row=3, column=2)
    

 def easy():
    label3 =Label(root,text=printsudoku(readsudokuEasy()), fg="green").grid(row=3, column=2)
    start = time.process_time()
    solveSudoku(sudoku1)
    myButton=Button(root,text="show solution",command=easysolve, bg="orange", fg="white").grid(row=4, column=2)
    label2 =Label(root,text="Time token to find the solution=", bg="orange", fg="white").grid(row=5, column=2)
    label4 =Label(root,text=(time.process_time()-start), fg="red").grid(row=6, column=2)
    
 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MediumSudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def mediumsolve():
    
    label3 =Label(root,text=printsudoku(sudoku2), fg="red").grid(row=3, column=2)

 def medium():
    label4 =Label(root,text=printsudoku(readsudokuMedium()), fg="black").grid(row=3, column=2)
    start = time.process_time()
    solveSudoku(sudoku2)
    myButton=Button(root,text="show solution",command=mediumsolve, bg="orange", fg="white").grid(row=4, column=2)
    label2 =Label(root,text="Time token to find the solution=", bg="orange", fg="white").grid(row=5, column=2)
    label4 =Label(root,text=(time.process_time()-start), fg="red").grid(row=6, column=2)
    
    
 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>HardSudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def hardsolve():
    label3 =Label(root,text=printsudoku(sudoku3), fg="purple").grid(row=3, column=2)

 def hard():
    label5 =Label(root,text=printsudoku(readsudokuHard()), fg="grey").grid(row=3, column=2)
    start = time.process_time()
    solveSudoku(sudoku3)
    myButton=Button(root,text="show solution",command=hardsolve, bg="orange", fg="white").grid(row=4, column=2)
    label2 =Label(root,text="Time token to find the solution=", bg="orange", fg="white").grid(row=5, column=2)
    label4 =Label(root,text=(time.process_time()-start), fg="red").grid(row=6, column=2)



 #text
 label2 =Label(root,text=">>Backtracking to solve sudoku<<", bg="orange", fg="white").grid(row=0, column=2)
 label1 =Label(root,text="Enter your choice!!!", fg="red").grid(row=1, column=2)


 #Button
 myButton=Button(root,text="easy",command=easy).grid(row=2, column=1) 
 myButton=Button(root,text="medium",command=medium).grid(row=2, column=2)
 myButton=Button(root,text="hard",command=hard).grid(row=2, column=3)  

 root.mainloop()
 
 
 
 
 
 
 
 """
 @author: talla
 @author: raghad
 """

def Naive():
 root1 = Tk()
 root1.geometry("420x520")
 root1.rowconfigure([0, 1, 2, 3,4,5,6,7], minsize=50)
 root1.columnconfigure([0, 1, 2, 3], minsize=50)
 root1.title("Naive Sudoku Game")


 sudoku1=readsudokuEasy()
 sudoku2=readsudokuMedium()
 sudoku3=readsudokuHard()
 # N is the size of the 2D matrix N*N


 # A utility function to print grid
 def printsudoku(sudoku):
     line = ""
     j=0
     for i in range(len(sudoku)):
         if j==8:
          line += "\n"
         if i == 3 or i == 6:
             line += "-------------------------\n"
         for j in range(len(sudoku[i])):
             if j == 3 or j == 6:
                 line += "| "
             
             line += str(sudoku[i][j])+"  "
         #print(line)
     return line

 # Checks whether it will be
 # legal to assign num to the
 # given row, col
 def isSafe(grid, row, col, num):

 	# Check if we find the same num
 	# in the similar row , we
 	# return false
 	for x in range(9):
 		if grid[row][x] == num:
 			return False

 	# Check if we find the same num in
 	# the similar column , we
 	# return false
 	for x in range(9):
 		if grid[x][col] == num:
 			return False

 	# Check if we find the same num in
 	# the particular 3*3 matrix,
 	# we return false
 	startRow = row - row % 3
 	startCol = col - col % 3
 	for i in range(3):
 		for j in range(3):
 			if grid[i + startRow][j + startCol] == num:
 				return False
 	return True

 # Takes a partially filled-in grid and attempts
 # to assign values to all unassigned locations in
 # such a way to meet the requirements for
 # Sudoku solution (non-duplication across rows,
 # columns, and boxes) */
 def solveSudoku(grid, row=0, col=0):

 	# Check if we have reached the 8th
 	# row and 9th column (0
 	# indexed matrix) , we are
 	# returning true to avoid
 	# further backtracking
 	if (row == 9 - 1 and col == 9):
 		return True
 	
 	# Check if column value becomes 9 ,
 	# we move to next row and
 	# column start from 0
 	if col == 9:
 		row += 1
 		col = 0

 	# Check if the current position of
 	# the grid already contains
 	# value >0, we iterate for next column
 	if grid[row][col] > 0:
 		return solveSudoku(grid, row, col + 1)
 	for num in range(1, 9 + 1, 1):
 	
 		# Check if it is safe to place
 		# the num (1-9) in the
 		# given row ,col ->we
 		# move to next column
 		if isSafe(grid, row, col, num):
 		
 			# Assigning the num in
 			# the current (row,col)
 			# position of the grid
 			# and assuming our assigned
 			# num in the position
 			# is correct
 			grid[row][col] = num

 			# Checking for next possibility with next
 			# column
 			if solveSudoku(grid, row, col + 1):
 				return True

 		# Removing the assigned num ,
 		# since our assumption
 		# was wrong , and we go for
 		# next assumption with
 		# diff num value
 		grid[row][col] = 0
 	return False

 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>EasySudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def easysolve():
     label3 =Label(root1,text=printsudoku(sudoku1), fg="blue").grid(row=3, column=2)
     

 def easy():
     label3 =Label(root1,text=printsudoku(readsudokuEasy()), fg="green").grid(row=3, column=2)
     start = time.process_time()
     solveSudoku(sudoku1)
     myButton=Button(root1,text="show solution",command=easysolve, bg="purple", fg="white").grid(row=4, column=2)
     label2 =Label(root1,text="Time token to find the solution=", bg="purple", fg="white").grid(row=5, column=2)
     label4 =Label(root1,text=(time.process_time()-start), fg="purple").grid(row=6, column=2)
     
 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MediumSudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def mediumsolve():
     
     label3 =Label(root1,text=printsudoku(sudoku2), fg="red").grid(row=3, column=2)

 def medium():
     label4 =Label(root1,text=printsudoku(readsudokuMedium()), fg="black").grid(row=3, column=2)
     start = time.process_time()
     solveSudoku(sudoku2)
     myButton=Button(root1,text="show solution",command=mediumsolve, bg="purple", fg="white").grid(row=4, column=2)
     label2 =Label(root1,text="Time token to find the solution=", bg="purple", fg="white").grid(row=5, column=2)
     label4 =Label(root1,text=(time.process_time()-start), fg="purple").grid(row=6, column=2)
     
     
 """>>>>>>>>>>>>>>>>>>>>>>>>>>>>>HardSudoku<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
 def hardsolve():
     label3 =Label(root1,text=printsudoku(sudoku3), fg="blue").grid(row=3, column=2)

 def hard():
     label5 =Label(root1,text=printsudoku(readsudokuHard()), fg="grey").grid(row=3, column=2)
     start = time.process_time()
     solveSudoku(sudoku3)
     myButton=Button(root1,text="show solution",command=hardsolve, bg="purple", fg="white").grid(row=4, column=2)
     label2 =Label(root1,text="Time token to find the solution=", bg="purple", fg="white").grid(row=5, column=2)
     label4 =Label(root1,text=(time.process_time()-start), fg="purple").grid(row=6, column=2)
 
 


 #text
 label2 =Label(root1,text=">>The naive approach to solve sudoku<<", bg="purple", fg="white").grid(row=0, column=2)
 label1 =Label(root1,text="Enter your choice!!!", fg="red").grid(row=1, column=2)


 #Button
 myButton=Button(root1,text="easy",command=easy).grid(row=2, column=1) 
 myButton=Button(root1,text="medium",command=medium).grid(row=2, column=2)
 myButton=Button(root1,text="hard",command=hard).grid(row=2, column=3)  
 
 root1.mainloop()
 
 
 
""">>>>>>>>>>>>>>>>>>>>>>>main<<<<<<<<<<<<<<<<<<<<<<<<<""" 
windwo = Tk()
windwo.geometry("400x400")
windwo.rowconfigure([0, 1, 2, 3,4,5,6,7,8,9], minsize=50)
windwo.columnconfigure([0, 1, 2, 3], minsize=50)
windwo.title("sudoku game")
 
label2 =Label(windwo,text=">>welcom to sudoku game<<", bg="pink", fg="black").grid(row=1, column=2)
label1 =Label(windwo,text="Enter your choice!!!", fg="red").grid(row=2, column=2)

myButton=Button(windwo,text="Backtracking",command=Backtracking).grid(row=3, column=2) 
myButton=Button(windwo,text="Naive",command=Naive).grid(row=4, column=2) 
windwo.mainloop()

 
 
 
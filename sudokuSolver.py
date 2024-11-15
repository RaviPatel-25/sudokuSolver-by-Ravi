from tkinter import*

class App:
	def __init__(self,root):
		self.root = root
		self.width = self.root.winfo_screenwidth()
		self.height = self.root.winfo_screenheight()
		self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
		self.root.overrideredirect(True)
		self.root.config(bg="black")
		
		self.x = 0
		self.y = 300
		
		self.varlist = []
		self.iterate = 0
		
		self.main()
		
	def main(self):
		self.head = Label(self.root,text="SudokuSolver",bg="black",fg="red",font=("Arial",20,"bold"))
		self.head.place(x=170,y=100)
		
		self.result = Label(self.root,text="",bg="black",fg="red",font=("Arial",20,"bold"))
		self.result.place(x=350,y=1700)
		
		
		for i in range(81):
			self.textvar = StringVar()
			self.varlist.append(self.textvar)
			
		for i in range(9):
			for j in range(9):
				self.btn = Entry(self.root,fg="green",bg="yellow",bd=7,font=("Arial",15,"bold"),textvariable=self.varlist[self.iterate])
				self.btn.place(x=self.x,y=self.y,width=(self.width/9),height=(self.width/9))
				if self.x<(self.width-(self.width/9)):
					self.x+=self.width/9
				else:
					self.x=0
					self.y+=self.width/9
				self.iterate+=1
				
		solvebtn = Button(self.root,text="Solve",bd=0,bg="black",fg="red",command=self.getvalue)
		solvebtn.place(x=200,y=1500)
		clearbtn = Button(self.root,text="Clear",bd=0,bg="black",fg="red",command=self.clear)
		clearbtn.place(x=650,y=1500)
		
				
	def getvalue(self):
		self.iterate = 0
		self.value =[]
		for i in range(9):
			raw = []
			for j in range(9):
				if self.varlist[self.iterate].get()!='':
					raw.append(int(self.varlist[self.iterate].get()))
				else:
					raw.append(0)
				self.iterate+=1
			self.value.append(raw)
		self.solve()
			
	def solve(self):
			N = 9
			self.iterate =0
			def printing(arr):
			    for i in range(N):
			        for j in range(N):
			            self.varlist[self.iterate].set(arr[i][j])
			            self.iterate+=1
			            
			def isSafe(grid, row, col, num):
			    for x in range(9):
			        if grid[row][x] == num:
			            return False
			          
			    for x in range(9):
			        if grid[x][col] == num:
			            return False
			
			    startRow = row - row % 3
			    startCol = col - col % 3
			
			    for i in range(3):
			        for j in range(3):
			            if grid[i + startRow][j + startCol] == num:
			                return False
			    return True
			
			def solveSudoku(grid, row, col):
			    if (row == N - 1 and col == N):
			        return True
			        
			    if col == N:
			        row += 1
			        col = 0
			
			    if grid[row][col] > 0:
			        return solveSudoku(grid, row, col + 1)
			    for num in range(1, N + 1, 1):
			        if isSafe(grid, row, col, num):
			            grid[row][col] = num
			            if solveSudoku(grid, row, col + 1):
			                return True
			
			        grid[row][col] = 0
			        
			    return False
			
			self.grid = self.value
			
			if (solveSudoku(self.grid, 0, 0)):
			    printing(self.grid)
			    self.result.config(text="Solved")
			else:
			    print("no solution  exists ")
			    self.result.config(text="Not Solved")
			    
	def clear(self):
		self.result.config(text="")
		self.iterate =0
		for i in range(9):
			 for j in range(9):
			      self.varlist[self.iterate].set('')
			      self.iterate+=1
			            
		
root = Tk()
obj = App(root)
root.mainloop()
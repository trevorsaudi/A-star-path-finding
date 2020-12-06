 #the goal is to find the shortest path between point A and B which are 
 #represented in nodes and edges
 #we make informed search using heuristics
 
 #we use an open set that is represented by an priority queue
 #we put the start node in the open set along with the distance to that node open={O,A}
import pygame
import math
from queue import PriorityQueue

# setting up the display dimensions
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED  = (255,0,0)
GREEN  = (0,255,0)
BLUE  = (0,0,255)
YELLOW  = (255,255,0)
WHITE  = (255,255,255)
BLACK  = (0,0,0)
PURPLE  = (128,0,128)
ORANGE  = (255,165,0)
TURQUOISE  = (64,224,208)
GREY = (128,128,128)

#the little cubes in the grid, different elements will be represented by colors
#the methods help us tell the state of the node
class Node: 
	def __init__(self,row,col,width,total_rows):
		self.row = row
		self.col = col
		self.x = row * width #help us figure out the position of the cubes
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED #closed set

	def is_open(self):
		return self.color == GREEN #open set
	
	def is_barrier(self):
		return self.color == BLACK #the barrier

	def is_start(self):
		return self.color == ORANGE #the starting color

	def is_end(self):
		return self.color == PURPLE
	
	def reset(self):
		self.color = WHITE


	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED
	
	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color =  BLACK
	def make_end(self):
		self.color = TURQUOISE
	def make_path(self):
		self.color = PURPLE
	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1]) 

	def __lt__(self,other): #comparing nodes
		return False


#defining the heuristics function
#uses the manhattan distance(L-distance)
def h(p1, p2):
	x1,y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start)) #add the first node and its f score
	came_from = {} #keeping track of the nodes we came from
	g_score = {node: float("inf") for row in grid for node in row}
	g_score[start] = 0
	f_score = {node: float("inf") for row in grid for node in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True
		
		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]: #if we find a better way add it to the path
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1 #add the neighbor if it isnt in the open set
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()
	return False
def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j,gap, rows)
			grid[i].append(node)

	return grid

#make the horizontal and vertical grid lines
def draw_grid(win, rows, width):
	gap  = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0,i*gap),(width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j*gap, 0),(j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE) #fill the entire screen with white

	#draw all the colors
	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

#finding which spot the mouse clicked on

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y,x = pos

	row = y // gap
	col = x // gap

	return row, col

def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS,width)

	#the starting and end nodes
	start = None
	end = None
	
	run = True
	started = False

	#check for the events happening in pygame
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			

	#check if user pressed on mouse, make checks on start , end position , the barriers
			if pygame.mouse.get_pressed()[0]: #pressing the left 
				pos = pygame.mouse.get_pos()
				row,col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				if not start and node != end: #if we havent pressed start and end, then make those
					start = node
					start.make_start()
				elif not end and node !=start:
					end = node
					end.make_end()
				elif node != end and node != start:
					node.make_barrier()
					 
			elif pygame.mouse.get_pressed()[2]: #pressing the right mouse
					pos = pygame.mouse.get_pos()
					row, col  = get_clicked_pos(pos, ROWS, width)
					node = grid[row][col]
					node.reset()
					if node == start:
						start = None
					elif node == end:
						end = None     

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for node in row:
							node.update_neighbors(grid)
					algorithm(lambda: draw(win,grid, ROWS, width), grid, start ,end)


				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)
	pygame.quit()

main(WIN,WIDTH)
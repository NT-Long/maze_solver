# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style

## Functions
def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == '%'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == '-'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")
			
		print('\n')

# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '-'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '-'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '-'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '-'):
		s_cells += 1

	return s_cells
#random value
# starting_height=int(random.random()*100)+3
# starting_width=int(random.random()*100)+3
# height=random.choice(range(starting_height+1,200))
# width=random.choice(range(starting_width+1,200))

height =30
width=30
height,width=map(int,input('height and width: ').split())
starting_height=random.choice(range(0, height))
starting_width=random.choice(range(0,width))
## Main code
# Init variables
wall = '%'
cell = '-'
unvisited = 'u'
maze = []

# Initialize colorama
init()

# Denote all cells as unvisited
maze=[[unvisited for i in range(width)]for j in range(height)]

# Randomize starting point and set it a cell


# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = '%'
maze[starting_height][starting_width - 1] = '%'
maze[starting_height][starting_width + 1] = '%'
maze[starting_height + 1][starting_width] = '%'

while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '-'):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '-'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '-'):
						maze[rand_wall[0]-1][rand_wall[1]] = '%'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '-'):
						maze[rand_wall[0]+1][rand_wall[1]] = '%'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != '-'):
						maze[rand_wall[0]][rand_wall[1]-1] = '%'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '-'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '-'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '-'):
						maze[rand_wall[0]-1][rand_wall[1]] = '%'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '-'):
						maze[rand_wall[0]][rand_wall[1]-1] = '%'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '-'):
						maze[rand_wall[0]][rand_wall[1]+1] = '%'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '-'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '-'

				# Mark the new walls
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '-'):
						maze[rand_wall[0]+1][rand_wall[1]] = '%'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '-'):
						maze[rand_wall[0]][rand_wall[1]-1] = '%'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '-'):
						maze[rand_wall[0]][rand_wall[1]+1] = '%'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '-'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '-'

				# Mark the new walls
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '-'):
						maze[rand_wall[0]][rand_wall[1]+1] = '%'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '-'):
						maze[rand_wall[0]+1][rand_wall[1]] = '%'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != '-'):
						maze[rand_wall[0]-1][rand_wall[1]] = '%'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# Mark the remaining unvisited cells as walls
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = '%'

# Set entrance and exit
def exit():
    for i in range(0,width):
        if maze[1][i]=="-":
            e1=[0,i]
            break
    for i in range(0,height):
        if maze[i][1]=="-": 
            e2=[i,0]
            break
    for i in range(width-1,0,-1):
        if maze[height-2][i]=="-":
            e3=[height-1,i]
            break             
    for i in range(0,height):
        if maze[i][width-2]=="-":
            e4=[i,width-1]
            break
    x=random.choice([e1,e2,e3,e4])
    return x

exit1=exit()
ending_height=exit1[0]
ending_width=exit1[1]
maze[exit1[0]][exit1[1]]="-"
def random_path():
    for j in  range(1,height-1):
            for i in range(1,width-1):
                rand=random.choice([0,1])
                if maze[j][i]=="%" and rand==1:
                    if maze[j-1][i]=="-"and maze[j+1][i]=="-" and j>1 and j<height-2:
                        maze[j][i]="-"
                    elif maze[j][i+1]=="-"and maze[j][i-1]=="-" and i>1 and i<width-2:
                        maze[j][i]='-'
    return
random_path()
printMaze(maze)
#random test
def writetest(x):
	source='maze'+str(x)+'.txt'
	print(source)
	with open(source,"x") as f:
		f.truncate(0)
		f.write('%i '%starting_height)
		f.write('%i\n'%starting_width)
		f.write('%i '%ending_height)
		f.write("%i\n"%ending_width)
		f.write('%i '%height)
		f.write('%i\n'%width)
		for j in maze:
			for k in range(width):
				f.write("%s"%j[k])
			f.write("\n")
x=int(input('press one number to save your maze in it( it must differ with previous maze number)'))
writetest(x)
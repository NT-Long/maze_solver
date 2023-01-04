import sys
from turtle import *
import copy
x=int(input('press maze you want to solve: '))
source='maze'+str(x)+'.txt'
f=open(source,"r")  
a=f.readline()
b=f.readline()
c=f.readline()
mosque_x, mosque_y = list(map(int, a.split()))
door_x,door_y = list(map(int, b.split()))
n, m = list(map(int, c.split()))
grid = []
node_expanded = []
queue = []
answer_routes = None
maxnode=0
t=1
algo=[]
for i in range(0, n):
    d=f.readline()
    grid.append(list(map(str, d)))
f.close
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
queue.append([mosque_x, mosque_y, []])
while len(queue) > 0:
    x, y, r = queue.pop(0)
    routes = copy.deepcopy(r)
    routes.append([x, y])

    node_expanded.append([x, y])

    if x == door_x and y == door_y:
        if answer_routes == None:
            answer_routes = routes
            break

    for direction in directions:
        next_x, next_y = x + direction[0], y + direction[1]
        if next_x < 0 or next_x >= n or next_y < 0 and next_y >= n:
            continue

        if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
            grid[next_x][next_y] = '='
            queue.append([next_x, next_y, routes])
            t+=1
            algo.append([next_x,next_y])
    t-=1
    maxnode=max(t,maxnode)

path=answer_routes
bg = '#E9D8A6'
wall = '#005F73'
cell = '#A3FE01'
line = wall
pig = '#001219' 
door = '#AE2012'
searching_path = '#8b8c89'
final_path = '#F49021'


wn=Screen()
wn.bgcolor(bg)
wn.title("A perfect maze")
wn.setup(700,700)
f=open(source,"r")
a=f.readline()
b=f.readline()
c=f.readline()
mosque_x, mosque_y = list(map(int, a.split()))
door_x, door_y = list(map(int, b.split()))
h, w = list(map(int, c.split()))
maze=[]

for i in range(h):
    d=f.readline()
    d1=[]
    for i in range(w):
        d1.append(d[i])
    maze.append(d1)
maze[mosque_x][mosque_y]="p"
maze[door_x][door_y]="e"
x0=int(600/w)
y0=int(600/h)
#y0 = x0
class Pen(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        ###
        self.color("white")
        self.penup()
        self.speed(0)
        self.resizemode("user")
        self.shapesize(1/20*y0,1/20*x0)
    def changesize(self,x,y):
        self.shapesize(stretch_wid=x, stretch_len=y)
def setup_maze(mazedraw):
    for y in range(h):
        for x in range(w):
            character=mazedraw[y][x]
            if w%2==0:
             cor_x=-300+x*x0
            else:
             cor_x=-300+x0/2+x*x0
            if h%2==0:
             cor_y=300-y*y0
            else:
             cor_y=300-y0/2-y*y0
            if character == '-':
                pen.color(line,cell)
                pen.goto(cor_x,cor_y)
                pen.stamp()                
            if character=="%":
                ###
                pen.color(wall)
                pen.goto(cor_x,cor_y)
                pen.stamp()
            elif character=="p":
                pen.color(pig)
                pen.goto(cor_x,cor_y)
                pen.stamp()
            elif character=="e":
                # pen.shape('circle')
                pen.color(door)
                pen.goto(cor_x,cor_y)
                pen.stamp()
                # pen.shape('square')
def algorithm(algo):
    for i in algo:
        x=i[1]
        y=i[0]
        if w%2==0:
            cor_x=-300+x*x0
        else:
            cor_x=-300+x0/2+x*x0
        if h%2==0:
            cor_y=300-y*y0
        else:
            cor_y=300-y0/2-y*y0
        pen.color(line,searching_path)
        pen.goto(cor_x,cor_y)
        pen.stamp()
def mpath(path):
    for i in path:
        x=i[1]
        y=i[0]
        
        if w%2==0:
            cor_x=-300+x*x0
        else:
            cor_x=-300+x0/2+x*x0
        if h%2==0:
            cor_y=300-y*y0
        else:
            cor_y=300-y0/2-y*y0
        pen.color(line,final_path)
        pen.goto(cor_x,cor_y)
        pen.stamp()
print('Numbers of node expanded(Time Conplexity):' ,str(len(algo)))
#for point in node_expanded:
#    print(str(point[0]) + " " + str(point[1]))
print('Numbers of node in answer routes(Path length):', str(len(path) - 3))
#for point in answer_routes:
#    print(str(point[0]) + " " + str(point[1]))
print('Numbers of maximum nodes in fronties(Space complexity)',maxnode)
    
pen=Pen()
setup_maze(maze)
algorithm(algo)
mpath(path)

mainloop()
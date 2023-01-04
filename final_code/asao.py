import sys
from turtle import *

x=int(input('press maze you want to solve: '))
source='maze'+str(x)+'.txt'

import copy
import time 
from queue import PriorityQueue
import textwrap
st=time.time()
f=open(source,"r")
a=f.readline()
b=f.readline()
c=f.readline()
mosque_x, mosque_y = list(map(int, a.split()))
start=(mosque_x,mosque_y)
door_x, door_y = list(map(int, b.split()))
goal=(door_x,door_y)
h, w = list(map(int, c.split()))
grid=[]#maze

for i in range(0,h):
    d=f.readline()
    d0=[]
    for i in range(w):
        d0.append(d[i])
    grid.append(d0)
print(grid)
def distance(a,b):
    x1,y1=a
    x2,y2=b
    return abs(x1-x2)+abs(y1-y2)
def aStar(grid,a,b):
    goal=b
    start=a
    coordinate=[]
    for i in range(len(grid)):
        for i1 in range(len(grid[0])):
            coordinate.append((i,i1))
    
    g_score={cell:float('inf') for cell in coordinate}
    g_score[start]=0
    f_score={cell:float('inf') for cell in coordinate}
    f_score[start]=g_score[start]+distance(start,goal)
    piorityQueue= PriorityQueue()
    piorityQueue.put((f_score[start],distance(start,goal),start))
    close=[]
    search=[]
    path={}
    large=0
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    while not piorityQueue.empty():
        currcell=piorityQueue.get()[2]
        search.append(currcell)
        if piorityQueue.qsize()>large:
                large=piorityQueue.qsize()
        if currcell==goal:
            way=[]
            node=currcell
            
            while node!=start:
                way.append(node)
                node=path[node]
            way.remove(way[0]) 
            break
        for d in directions:
            childcell= (currcell[0]+d[0],currcell[1]+d[1])
            if grid[childcell[0]][childcell[1]]=='-' or grid[childcell[0]][childcell[1]]=='.' and childcell not in close: 
                temp_g_score=g_score[currcell]+1
                temp_f_score=temp_g_score+distance(childcell,goal)
                if temp_f_score<f_score[childcell]:
                    g_score[childcell]=temp_g_score
                    f_score[childcell]=temp_f_score
                    piorityQueue.put((f_score[childcell],distance(childcell,goal),childcell))
                    path[childcell]=currcell
    
        close.append(currcell)
    way=[]
    node=currcell
    while node!=start:
        way.append(node)
        node=path[node]
    way.remove(way[0]) 
    return search,way,large
algo,path,maxnode=aStar(grid,start,goal)   



#variable
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
print('Numbers of node in answer routes(Path length):', str(len(path) - 1))
#for point in answer_routes:
#    print(str(point[0]) + " " + str(point[1]))
print('Numbers of maximum nodes in fronties(Space complexity)',maxnode)
    
pen=Pen()
setup_maze(maze)
algorithm(algo)
mpath(path)

mainloop()


    
    
    
   


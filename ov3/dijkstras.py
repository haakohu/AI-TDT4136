import heapq
from image_gui import *

class Node:
    parent = None
    heuristic_value = None
    distance = None
    type = None
    x = None
    y = None
    orig_type = None
    

    #Types: # = Closed, . = open, P = path
    def __init__(self,value,x,y):
        if value not in ['#','.','P','A','B','w','m','f','g','r']:
            raise
        self.type = value
        self.x = x
        self.y = y
        self.orig_type = value

    def total_cost(self):
        return self.heuristic_value + self.distance 
    

    def get_values(self):
        return (self.distance,self.heuristic_value)
    
    def __lt__(self,other):
        return self.heuristic_value < other.heuristic_value


class Board:
    board = None

    def __init__(self,matrix):
        self.board = []
        for row_i in range(len(matrix)):
            new_row = []
            for col_i in range(len(matrix[0])):
                n = Node(matrix[row_i][col_i],col_i,row_i)
                new_row.append(n)
            self.board.append(new_row)

    
    def get_node(self,x,y):
        if x >= len(self.board[0]) or y >= len(self.board) or x < 0 or y < 0:
            return None
        return self.board[y][x]
    

    def get_8_neighbours(self,node):
        n = set()
        for y in range(node.y-1,node.y+2):
            for x in range(node.x-1,node.x+2):
                new_node = self.get_node(x,y)
                if new_node != None:
                    n.add(self.get_node(x,y))
        n.remove(node)
        return n


    def get_4_neighbours(self,node):
        n = set()
        if self.get_node(node.x,node.y-1) != None:
            n.add(self.get_node(node.x,node.y-1))
        if self.get_node(node.x,node.y+1) != None:
            n.add(self.get_node(node.x,node.y+1))
        if self.get_node(node.x-1,node.y) != None:
            n.add(self.get_node(node.x-1,node.y))
        if self.get_node(node.x+1,node.y) != None:
            n.add(self.get_node(node.x+1,node.y))
        return n

    def generate_heuristic(self,start_node):
        queue = [start_node]
        seen = {start_node}
        start_node.heuristic_value = 1
        while len(queue) != 0:
            start_node = heapq.heappop(queue)
            neighbours = self.get_4_neighbours(start_node)
            for node in neighbours:
                if node not in seen:
                    seen.add(node)
                    node.heuristic_value = start_node.heuristic_value + 1
                    heapq.heappush(queue,node)


    def print_values(self):
        for row in self.board:
            print([x.get_values() for x in row])
    
    def print_coordinates(self):
        for row in self.board:
            print([(node.x,node.y) for node in row])

    
    def set_solution(self,end_node):
        print("LOL")
        while True:
            if end_node.type != 'A' and end_node.type != 'B':
                end_node.type = 'P'
            if end_node.parent == None:
                break
            end_node = end_node.parent
    

    def get_types(self):
        return [[x.type for x in row] for row in self.board]
    
    def get_node_of(self,el):
        for row in self.board:
            for node in row:
                if node.type == el:
                    return node
        raise 
    def get_start_pos(self):
        return self.get_node_of('A')
    def get_end_pos(self):
        return self.get_node_of('B')
    
    def get_distance(self,node,distances):
        if node.orig_type not in distances.keys():
            raise
        return distances[node.orig_type]

    
    def a_star_alogirthm(self,distances):
        start_node = self.get_start_pos()
        end_node = self.get_end_pos()
        start_node.distance = 0
        open_list = [start_node]
        sorter = lambda x: (x.distance) #Change the sorting variable
        closed_list = set()
        while len(open_list) > 0:
            open_list = sorted(open_list,key=sorter)
            point_node = open_list.pop(0)
            if point_node == end_node:
                return 
            closed_list.add(point_node)
            point_node.type = 'C'
            neighbors = self.get_4_neighbours(point_node)
            for node in neighbors:
                if not node in closed_list:
                    if not node in open_list:
                        open_list.append(node)
                        node.type = 'O'
                    if node.distance == None or node.distance > point_node.distance + self.get_distance(node,distances):
                        node.distance = point_node.distance + self.get_distance(node,distances)
                        node.parent = point_node
                
    
def get_board_from_file(path):
    f = open(path,'r')
    matrix = [[x for x in list(row.strip())] for row in f.readlines()]
    return Board(matrix)




def do_task():
    board = get_board_from_file("/Users/hakon/programmering/tdt4136/ov3/boards/board-2-4.txt")
    start_node = board.get_start_pos()
    end_node = board.get_end_pos()
    board.generate_heuristic(end_node)
    board.a_star_alogirthm({'#': 9999999,'.':1,'A':1,'B':1,'w':100,'m':50,'f':10,'g':5,'r':1})
    board.set_solution(end_node)
    show_matrix(board.board)



if __name__ == '__main__':
    do_task()
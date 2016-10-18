from PIL import Image

def matrix_to_image(matrix):
    matrix = generate_matrix(matrix)
    im = Image.new('RGB',(len(matrix[0]),len(matrix)))
    im.putdata(matrix_to_array(matrix))
    return im


def set_value(matrix,node,row_i,col_i):
    for y in range(3):
        for x in range(3):
            if node.orig_type == '#':  #closed
                matrix[row_i*3+y][col_i*3+x]  = (0,0,0)
            elif node.orig_type == '.':  #open
                matrix[row_i*3+y][col_i*3+x]  = (255,255,255)
            elif node.orig_type == 'P':  #path
                matrix[row_i*3+y][col_i*3+x]  = (100,100,100)
            elif node.orig_type == 'A':  #start
                matrix[row_i*3+y][col_i*3+x]  = (0,255,0)
            elif node.orig_type == 'B': #end
                matrix[row_i*3+y][col_i*3+x]  = (255,0,0)
            elif node.orig_type == 'w': #water
                matrix[row_i*3+y][col_i*3+x]  = (0,0,180)
            elif node.orig_type == 'm': #mountains
                matrix[row_i*3+y][col_i*3+x]  = (169,169,169)
            elif node.orig_type == 'f': #forests
                matrix[row_i*3+y][col_i*3+x]  = (0,140,0)
            elif node.orig_type == 'g': #grasslands
                matrix[row_i*3+y][col_i*3+x]  = (0,70,0)
            elif node.orig_type == 'r': #roads
                matrix[row_i*3+y][col_i*3+x]  = (165,42,42)
    if node.type == 'P':
        matrix[row_i*3+1][col_i*3+1] = (0,0,0)
    if node.type == 'O': #In the open list
        matrix[row_i*3+1][col_i*3+1] = (255,192,203)
    if node.type == 'C':
        matrix[row_i*3+1][col_i*3+1] = (255,255,0)



# # = CLOSED, . = OPEN, P = PATH
def generate_matrix(matrix):
    new_matrix = [[0 for x in range(len(matrix[0])*3)] for y in range(len(matrix)*3)]
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[0])):
            set_value(new_matrix,matrix[row_i][col_i],row_i,col_i)
    return new_matrix

def matrix_to_array(matrix):
    return [a for row in matrix for a in row]

def show_matrix(matrix):
    matrix_to_image(matrix).show()


if __name__ == "__main__":
    f = open('/Users/hakon/programmering/tdt4136/ov3/boards/board-1-1.txt','r')
    matrix = [[x for x in list(row.strip())] for row in f.readlines()]
    show_matrix(matrix)
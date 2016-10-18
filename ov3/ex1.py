from a_star import *
from image_gui import *



 
    
def do_task():
    board = get_board_from_file("/Users/hakon/programmering/tdt4136/ov3/boards/board-1-4.txt")
    start_node = board.get_start_pos()
    end_node = board.get_end_pos()
    board.generate_heuristic(end_node)
    board.a_star_alogirthm({'#': 9999999,'.':1,'A':1,'B':1})
    print("DONE2")
    board.set_solution(end_node)
    show_matrix(board.get_types())



            





if __name__ == '__main__':
    do_task()
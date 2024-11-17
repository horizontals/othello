import pygame as pg
from itertools import product
def main():
    # すべての初期化
    pg.init()
    screen = pg.display.set_mode((WIN_LENGTH, WIN_LENGTH))
    pg.display.set_caption("othello")
    screen.fill(GND_COLOR)
    clock = pg.time.Clock()

    # lineを引く
    for i in range(0, WIN_LENGTH+1, CELL_SIZE):
        pg.draw.line(screen, LINE_COLOR, (i, 0), (i, WIN_LENGTH), width=LINE_WIDTH)
        pg.draw.line(screen, LINE_COLOR, (0, i), (WIN_LENGTH, i), width=LINE_WIDTH)
    
    # dotを打つ
    for i in DOTS:
        pg.draw.circle(screen, LINE_COLOR, i, 2*LINE_WIDTH, width=LINE_WIDTH)


    # if push esc or click x: False 
    running = True

    # キーが押されたらプレスフラグをたてる
    is_press = False

    # gameの初期化も忘れない
    should_init=True
    # すべての初期化ここまで

    while running: # すべてのloop(何gameもやる人)

        if should_init:
            should_init=False

            # 1game内の初期化

            turn = BLACK

            # board init
            board = [[UNPLACED]*8 for _ in range(8)]
            board[3][3], board[3][4] = WHITE, BLACK
            board[4][3], board[4][4] = BLACK, WHITE

            # 1game内の初期化ここまで

        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                running = False
                break
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
             # まず、マウスの座標からセルの座標へと移す
                mouse_pos=pg.mouse.get_pos()
                if not(0 in mouse_pos or WIN_LENGTH-1 in mouse_pos):
                    cell_x = mouse_pos[X]//CELL_SIZE
                    cell_y = mouse_pos[Y]//CELL_SIZE
                    is_press = True
        
        if is_press:
            is_press = False
            places=place_list(board, turn, cell_x, cell_y)
            if len(places):
                for p_x,p_y in places:
                    board[p_y][p_x] = turn

                # pass判定
                if can_place(board, turn*FLIP):
                    turn*=FLIP
                else:
                    if not(can_place(board, turn)):
                        should_init=True


        for x,y in product(range(8),range(8)):
            pg.draw.circle(screen, COLOR[board[y][x]], ((x+0.5)*CELL_SIZE, (y+0.5)*CELL_SIZE), CELL_SIZE*0.3)
        pg.display.flip()
        clock.tick(30)
    pg.quit()

# cell_inside_width=size-width
CELL_SIZE = 10
LINE_WIDTH = 1
WIN_LENGTH=8*CELL_SIZE+LINE_WIDTH

temp1=CELL_SIZE*2 + 1 +LINE_WIDTH//2
temp2=CELL_SIZE*6 + 1 +LINE_WIDTH//2
DOTS={(temp1,temp1), (temp1,temp2), (temp2,temp1), (temp2,temp2)}

# board value
UNPLACED =  0
BLACK    =  1
WHITE    = -1

# board[y][x]*=FLIP
FLIP = -1

BLACK_COLOR = (  0,   0,   0)
WHITE_COLOR = (255, 255, 255)
LINE_COLOR  = (  0,   0,   0)
GND_COLOR   = (  0, 190,   0)

COLOR = (GND_COLOR, BLACK_COLOR, WHITE_COLOR)

# 走査する方向
DIRECTIONS = {(-1,-1),( 0,-1),( 1,-1),
             (-1, 0),        ( 1, 0),
             (-1, 1),( 0, 1),( 1, 1)}

# index
X = 0
Y = 1

def place_list(board: list, turn, cell_x, cell_y):
    can_place_set = set()
    if board[cell_y][cell_x]:
        return can_place_set

    for direction in DIRECTIONS:
        can_turn_set = set()
        ref_cell_x=cell_x
        ref_cell_y=cell_y

        while True:
            ref_cell_x += direction[X]
            ref_cell_y += direction[Y]
            ref = UNPLACED if not(0<=ref_cell_x<=7 and 0<=ref_cell_y<=7) else board[ref_cell_y][ref_cell_x]
            if ref == UNPLACED:
                break
            elif ref == turn and len(can_turn_set):
                can_place_set|=can_turn_set
                break
            elif ref == FLIP*turn:
                can_turn_set.add((ref_cell_x,ref_cell_y))
    if len(can_place_set) >= 1:
        can_place_set.add((cell_x,cell_y))
    return can_place_set
    
def can_place(board, turn):
    for x,y in product(range(8),range(8)):
        if len(place_list(board, turn, x, y)):
            return True
    return False




     
    
# mainを使用
# ここより上にすべての定義を書く
if __name__ == "__main__":
    main()
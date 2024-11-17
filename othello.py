import pygame
CELL_SIZE=10

UNPLACED=0
BLACK=1
WHITE=-1
turn=BLACK
FLIP=-1
BLACK_COLOR=(0,0,0)
WHITE_COLOR=(255,255,255)
DIRECTION={(-1,-1),( 0,-1),( 1,-1),
           (-1, 0),        ( 1, 0),
           (-1, 1),( 0, 1),( 1, 1)}
X=0
Y=1
# tupleの参照(x,y)




board=[[UNPLACED for _ in range(8) ] for _ in range(8)]
board[3][3],board[3][4]=WHITE,BLACK
board[4][3],board[4][4]=BLACK,WHITE

def main():
    pygame.init()
    win=pygame.display.set_mode((CELL_SIZE*8,CELL_SIZE*8))
    clock=pygame.time.Clock()
    pygame.display.set_caption("Test")

    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
            elif e.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if 0 not in pos and CELL_SIZE*8-1 not in pos:
                    cell=()
                    cell[X] = pos[X]//CELL_SIZE
                    cell[Y] = pos[Y]//CELL_SIZE
                    print(cell[X],cell[Y])
                    for dir in DIRECTION:
                        d=1
                        while True:
                            reference=(cell[X]+d*dir[X], cell[Y]+d*dir[X])
                            if 0<=reference[X]<=7 and 0<=reference[Y]<=7:pass
                            
            

        win.fill((0, 190, 0))

        for i in range(8):
            for j in range(8):
                pygame.draw.rect(win, (0,0,0), pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE), width=1)
                if board[i][j]!=0:
                    pygame.draw.circle(win, (BLACK_COLOR if board[i][j]==1 else WHITE_COLOR), ((i+0.5)*CELL_SIZE, (j+0.5)*CELL_SIZE), CELL_SIZE*0.3)

        pygame.display.flip()
        clock.tick(30)



if __name__=='__main__':
    main()

import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png")#lec2
    kt_img = pg.transform.flip(kt_img,True,False)#lec2
    im_ls=[kt_img,pg.transform.rotozoom(kt_img,10,1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x =tmr%1600
        screen.blit(bg_img, [-x, 0])#練習4
        screen.blit(bg_img,[1600-x,0])
        screen.blit(im_ls[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
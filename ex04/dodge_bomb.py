import pygame as pg
import sys
from random import randint

def main():
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()

    # 練習３
    k_img = pg.image.load("fig/6.png")
    k_img = pg.transform.rotozoom(k_img, 0, 2.0)
    k_uimg = k_img.get_rect()
    k_uimg.center = 900, 400

    # 練習５
    bom_sfc = pg.Surface((20, 20))
    bom_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bom_sfc, (255,0,0), (10, 10), 10)
    bom_rct = bom_sfc.get_rect()
    bom_rct.centerx = randint(0, scrn_rct.width)
    bom_rct.centery = randint(0, scrn_rct.height)

    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc, bg_rect) # 練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:# こうかとんの縦座標を -1
            k_uimg.centery -= 1
        if key_lst[pg.K_DOWN]:# こうかとんの縦座標を +1
            k_uimg.centery += 1
        if key_lst[pg.K_LEFT]:# こうかとんの縦座標を -1
            k_uimg.centerx -= 1
        if key_lst[pg.K_RIGHT]:# こうかとんの縦座標を +1
            k_uimg.centerx +=1
        
        scrn_sfc.blit(k_img, k_uimg) # 練習３

        scrn_sfc.blit(bom_sfc, bom_rct) # 練習５

        pg.display.update()
        clock.tick(1000) # 練習２
        



if __name__ == "__main__":
    pg.init
    main()
    pg.quit
    sys.exit()
import pygame as pg
import sys
import random
import time

def start(): # スタート画面（未完成）
    mscrn_s = pg.display.set_mode((600, 400))
    mscrn_r = mscrn_s.get_rect()
    clock = pg.time.Clock()

    while True:
        mscrn_s.fill((0,100,0))
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.K_ESCAPE:
                return
        key_lst = pg.key.get_pressed()    
        if key_lst[pg.K_1]: # キーボードの１が押された時にmain()を起動する
            time.sleep(0.5)
            main()
            break
        pg.display.update()
        clock.tick(1000)

def game_over(): # ゲームオーバー画面（未完成）
    pg.display.set_caption("Game Over")
    mscrn_s = pg.display.set_mode((600, 400))
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.K_ESCAPE:
                return
        mscrn_s.fill((0,0,0))
        clock.tick(1000)

def check_bound(obj_rct, scr_rct):
    """
    obj_rct: こうかとんrct　または爆弾rct
    scr_rct: スクリーンrct
    領域内: +1　領域外: -1
    """
    yoko, tate = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

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

    oji_gif = pg.image.load("fig/ghost_rmbg.png") # ghostのクロマキー画像読み込み
    oji_gif = pg.transform.rotozoom(oji_gif, 0, 0.2) # ghostの大きさを0.2倍
    oji_gif_rct = oji_gif.get_rect()
    oji_gif_rct.centerx = random.randint(0, scrn_rct.width)
    oji_gif_rct.centery = random.randint(0, scrn_rct.height)

    # 練習５
    bom_sfc = pg.Surface((20, 20))
    bom_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bom_sfc, (255,0,0), (10, 10), 10)
    bom_rct = bom_sfc.get_rect()
    bom_rct.centerx = random.randint(0, scrn_rct.width)
    bom_rct.centery = random.randint(0, scrn_rct.height)

    # 練習６
    vx, vy = 1, 1
    gvx, gvy = 1, 1
    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc, bg_rect) # 練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.K_ESCAPE:
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
        
        yoko, tate = check_bound(k_uimg, scrn_rct)
        if yoko == -1: # 四つ角に２つのキー同時押でぶつかると壁にめり込むため、４つ角対策
            if key_lst[pg.K_LEFT]:
                k_uimg.centerx += 1
                if tate == -1:
                    if key_lst[pg.K_UP]:
                        k_uimg.centery += 1
                    if key_lst[pg.K_DOWN]:
                        k_uimg.centery -= 1

            if key_lst[pg.K_RIGHT]:
                k_uimg.centerx -= 1
                if tate == -1:
                    if key_lst[pg.K_UP]:
                        k_uimg.centery += 1
                    if key_lst[pg.K_DOWN]:
                        k_uimg.centery -= 1

        elif tate == -1:
            if key_lst[pg.K_UP]:
                k_uimg.centery += 1
            if key_lst[pg.K_DOWN]:
                k_uimg.centery -= 1
            
        scrn_sfc.blit(k_img, k_uimg) # 練習３

        # 練習７
        byoko, btate = check_bound(bom_rct, scrn_rct)
        gyoko, gtate = check_bound(oji_gif_rct, scrn_rct)
        vx *= byoko
        vy *= btate
        gvx *= gyoko
        gvy *= gtate
        bom_rct.move_ip(vx, vy)
        oji_gif_rct.move_ip(gvx, gvy)

        scrn_sfc.blit(bom_sfc, bom_rct) # 練習５
        scrn_sfc.blit(oji_gif, oji_gif_rct)
        if k_uimg.colliderect(bom_rct) or k_uimg.colliderect(oji_gif_rct):
            time.sleep(0.5)
            game_over()
            return

        pg.display.update()
        clock.tick(1000) # 練習２
        
if __name__ == "__main__":
    pg.init
    start() # start()を起動
    pg.quit
    sys.exit()
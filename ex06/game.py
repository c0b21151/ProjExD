import pygame as pg
import sys

img_bg1 = "pic/bgimage.jpg"
img_bg2 = "pic/bgimage2.png"
img_bg3 = "pic/bgimage3.jpg"
img_bg4 = "pic/skybg.jpg"
img_bg5 = "pic/night1.png" # 試した背景画像
bg_y = 0

px = 300 # プレイヤーの初期位置データ
py = 300

def movep(screen, key): # playerの移動
    global px, py
    if key[pg.K_UP] == 1:
        py -= 10
    if key[pg.K_DOWN] == 1:
        py += 10
    if key[pg.K_LEFT] == 1:
        py -= 10
    if key[pg.K_RIGHT] == 1:
        py += 10

def background(sd, cl, bg): # sd:screen cl:clock bg:background
    global bg_y
    img_bg = pg.image.load(bg)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        bg_y = (bg_y+0.4)%400
        sd.blit(img_bg,[0,bg_y])
        sd.blit(img_bg,[0,bg_y-400]) #画面を分割して表示

        pg.display.update()
        cl.tick()

def main():
    pg.init()
    pg.display.set_caption("move background")
    screen = pg.display.set_mode((600,400))
    clock = pg.time.Clock()
    key = pg.key.get_pressed()
    while True:
        background(screen, clock, img_bg5)
        movep(screen, key)

if __name__ == "__main__":
    main()

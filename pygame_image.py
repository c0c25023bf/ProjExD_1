import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

    #第1回練習問題　
    # 2. 【ル】背景画像SurfaceをスクリーンSurfaceにblitし，表示させよ．
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    # 1. 【初】「pg_bg.jpg」（画像サイズ：幅1600 高さ900）を読み込み，Surfaceを生成せよ．
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0




   
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # 2.背景画像SurfaceをスクリーンSurfaceにblitし，表示させよ．
        screen.blit(bg_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
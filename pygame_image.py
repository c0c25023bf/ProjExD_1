import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 第1回練習問題
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 1. 【初】「pg_bg.jpg」（画像サイズ：幅1600 高さ900）を読み込み，Surfaceを生成せよ．
    bg_img = pg.image.load("fig/pg_bg.jpg")

    # 8.
    bg_img_flip = pg.transform.flip(bg_img, True, False)
    tmr = 0

    # 3
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img = pg.transform.flip(kokaton_img, True, False)
    # 10-1/10-2
    kokaton_rct = kokaton_img.get_rect()
    kokaton_rct.center = 300, 200  # 初期値 横、縦
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            # 10-3
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            kokaton_rct.move_ip((0, -1))
        if key_list[pg.K_DOWN]:
            kokaton_rct.move_ip((0, +1))
        if key_list[pg.K_LEFT]:
            kokaton_rct.move_ip((-1, 0))
        if key_list[pg.K_RIGHT]:
            kokaton_rct.move_ip((+2, 0))
        
        # 2.背景画像SurfaceをスクリーンSurfaceにblitし，表示させよ．
        # 5.tmrを使って、背景画像を動かす/9.xを書き換える。割った余りを使う。
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        # 7.残像の引き延ばし＋1600
        screen.blit(bg_img_flip, [-x + 1600, 0])
        # 9.残像の引き延ばし＋3200
        screen.blit(bg_img, [-x + 3200, 0])
        # 4　こうかとん描画/10-5
        screen.blit(kokaton_img, kokaton_rct)
        kokaton_rct.move_ip((-1,0))
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

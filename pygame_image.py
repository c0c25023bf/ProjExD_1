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

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 2.背景画像SurfaceをスクリーンSurfaceにblitし，表示させよ．
        # 5.tmrを使って、背景画像を動かす/9.xを書き換える。割った余りを使う。
        x = tmr%3200
        print(x)
        screen.blit(bg_img, [-x, 0])
        # 7.残像の引き延ばし＋1600
        screen.blit(bg_img_flip, [-x + 1600, 0])
        # 9.残像の引き延ばし＋3200
        screen.blit(bg_img_flip, [-x + 3200, 0])
        # 4　こうかとん描画
        screen.blit(kokaton_img, [300, 200])

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


import pyxel
#コメントのテスト
pyxel.init(150, 150)
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 5, 5, 6)

pyxel.run(update, draw)

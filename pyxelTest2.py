
import pyxel

pyxel.init(50, 50)
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 10, 10, 11)

pyxel.run(update, draw)

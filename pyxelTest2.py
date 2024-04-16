
import pyxel
#コメントのテスト
class App:
    def __init_(self):
        #ディスプレイの初期化
        pyxel.init(150, 150)
        
        #マウスカーソルを表示
        pyxel.mouse(True)

        #アプリケーションの開始
        pyxel.run(self.update, self.draw)
        
#開始時に呼ばれる関数
def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
        
#起動時に呼ばれる描画関数
def draw(self):
    pyxel.cls(0)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 5, 5, 6)

App()





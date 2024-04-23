
import pyxel
import math
#コメントのテスト

####Constants###

screenX = 150
screenY = 150
numOrgCircles = 10

class vec2:
    def __init__(self, x,y):
        self.x = x
        self.y = y



# 円を描くクラス
class circle:
    def __init__(self):
        self.r = pyxel.rndi(10, 20)
        
        self.pos = vec2(
            pyxel.rndf(self.r, screenX - self.r),
            pyxel.rndf(self.r, screenY - self.r),
        )
        self.color = pyxel.rndi(1, 15)


class App:
    def __init__(self):
        
        #ディスプレイの初期化
        pyxel.init(screenX, screenY, title="clickTest.py", fps=20)
        
        #マウスカーソルを表示
        pyxel.mouse(True)
        
        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False

        #self.circle = circle()
        self.circles = [circle() for _ in range(numOrgCircles)]
        clickToggle = False


        #アプリケーションの開始
        pyxel.run(self.update, self.draw)

        

        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        numCircles = len(self.circles)
        #print(numCircles)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :
            for i in range(numCircles):
                circle = self.circles[i]
                dx = circle.pos.x - pyxel.mouse_x
                dy = circle.pos.y - pyxel.mouse_y

                if dx * dx + dy * dy < circle.r * circle.r :
                    print("deleted")
                    clickToggle = True
                    del self.circles[i]
                    break
                
        
        
            
        #経過フレーム数でTrueにするトグルをTrueにする
        self.frameCounterEnabled = (pyxel.frame_count % 10) == 0

        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()

        for circle in self.circles:
            pyxel.circ(circle.pos.x, circle.pos.y, circle.r, circle.color)

      
    def cls(self):
        pyxel.cls(0)
        
   
App()


import pyxel

####Constants###
screenWidth = 150
screenHeight = 150
numExplodeCircles = 7   #周りの円の数
circleDist = 4




class vec2:
    def __init__(self, x,y):
        self.x = x
        self.y = y



# 円を描くクラス
class circle:
    def __init__(self):
        self.r = pyxel.rndi(10, 20)
        self.pos = vec2(75,75)
        self.color = 4



class App:    
    def __init__(self):
        self.screenX = screenWidth
        self.screenY = screenHeight
        
        #ディスプレイの初期化
        pyxel.init(self.screenX, self.screenY, title="CircleTest.py", fps=20)
        
        #マウスカーソルを表示
        pyxel.mouse(True)

        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False
        
        #最初の円のインスタンスを作る
        self.circle = circle()
        
        #self.circle.color = 5
        print(self.circle.pos.x, self.circle.pos.y, self.circle.r,self.circle.color)

        #周りの円を格納する円の配列を作る
        self.newCircles = [circle()]
        
        #アプリケーションの開始
        pyxel.run(self.update, self.draw)
        
        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        #経過フレーム数でTrueにするトグルをTrueにする
        self.frameCounterEnabled = (pyxel.frame_count % 10) == 0
        
        
        # 周りの円を表示する繰り返し処理
        for i in range(numExplodeCircles):
            
            #表示する角度を均等にする
            angle = 360 * i / numExplodeCircles

            #周りの円のインスタンスを生成
            self.newCircle = circle()

            #周りの円の半径を元の円から計算、半径x半径を表示する数で割る
            self.newCircle.r = pyxel.sqrt(self.circle.r * self.circle.r / numExplodeCircles)
            print(self.newCircle.r)

            #周りの円の場所
            self.newCircle.pos.x = self.circle.pos.x + (self.circle.r + self.newCircle.r) * pyxel.cos(angle)
            self.newCircle.pos.y = self.circle.pos.y + (self.circle.r + self.newCircle.r) * pyxel.sin(angle)

            #元の円と周りの円の距離を伸ばしたい
            self.newCircle.pos.x += pyxel.cos(angle) * circleDist
            self.newCircle.pos.y += pyxel.sin(angle) * circleDist

            self.newCircle.color = pyxel.rndi(1, 15)
            #できた円を配列に格納
            self.newCircles.append(self.newCircle)
        
    #起動時に呼ばれる描画関数
    def draw(self):
        self.cls()
        
        #元の円を描く
        pyxel.circ(self.circle.pos.x, self.circle.pos.y, self.circle.r, self.circle.color)
   
        #周りの円を描く
        for circle in self.newCircles:
            pyxel.circ(circle.pos.x, circle.pos.y, circle.r, circle.color)
            
        
    def cls(self):
        pyxel.cls(0)

App()


import pyxel
#コメントのテスト

####Constants###

screenX = 150
screenY = 150
#最初の円の数
numOrgCircles = 10
maxCircleSpeed = 2

class vec2:
    def __init__(self, x,y):
        self.x = x
        self.y = y



# 円を描くクラス
class circle:
    def __init__(self):
        self.r = pyxel.rndi(10, 20)

        #最初に表示される場所
        self.pos = vec2(
            pyxel.rndf(self.r, screenX - self.r),
            pyxel.rndf(self.r, screenY - self.r),
        )
        
        #移動に関する定数、次のupdate関数で常に更新し続ける
        self.vel = vec2(
            pyxel.rndf(-maxCircleSpeed, maxCircleSpeed),
            pyxel.rndf(-maxCircleSpeed, maxCircleSpeed),
        )
        
        self.color = pyxel.rndi(1, 15)


    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        if self.vel.x < 0 and self.pos.x < self.r:
            self.vel.x *= -1

        if self.vel.x > 0 and self.pos.x > screenX - self.r:
            self.vel.x *= -1

        if self.vel.y < 0 and self.pos.y < self.r:
            self.vel.y *= -1

        if self.vel.y > 0 and self.pos.y > screenY - self.r:
            self.vel.y *= -1


class App:
    def __init__(self):
        
        #ディスプレイの初期化
        pyxel.init(screenX, screenY, title="clickTest2.py", fps=20)
        
        #マウスカーソルを表示
        pyxel.mouse(True)

        #消した時オンになるトグル
        self.isDeleted = False

        self.isFinished = False
        
        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False
        
        #作る円をしまう配列を作る
        self.circles = [circle() for _ in range(0, numOrgCircles)]


        #アプリケーションの開始
        pyxel.run(self.update, self.draw)

        

        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #配列に入っている円の数を調べる 
        numCircles = len(self.circles)
        #print(numCircles)
        if not numCircles == 0:
            
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :
                for i in range(numCircles):
                    #配列に格納された円を一つずつ取り出す
                    circle = self.circles[i]

                    #マウスカーソルからの距離
                    dx = circle.pos.x - pyxel.mouse_x
                    dy = circle.pos.y - pyxel.mouse_y

                    #三角関数で半径内にマウスがあるか判断
                    if dx * dx + dy * dy < circle.r * circle.r :
                        #print("deleted")
                        #消されたというトグルをオン
                        self.isDeleted = True
                    
                        #あったらその円を配列から消す
                        del self.circles[i]
                    
                        #配列に入っている円の数を一つ減らす
                        numCircles -= 1
                    
                        #これ以上繰り返す必要がないのでfor文を抜ける
                        break
                
            
                
        if numCircles == 0:
            print("done")
            self.isFinished = True
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :
                self.restart()

        #circleのupdate関数を呼び出して円を動かす、10個が初期値なら0を含む9から-1まで-1ずつ
#なぜ-1なのかわかりません
        for i in range(numCircles-1, -1, -1):
            bi = self.circles[i]
            bi.update()

        
            
            

        
        
            
        #経過フレーム数でTrueにするトグルをTrueにする
        self.frameCounterEnabled = (pyxel.frame_count % 10) == 0

        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()
        
        

        
            
        #円を描画
        for circle in self.circles:
            pyxel.circ(circle.pos.x, circle.pos.y, circle.r, circle.color)

        if not self.isDeleted:
            pyxel.text(50, 75, "Tap Circle!", pyxel.rndi(1, 15))
        elif self.isFinished:
            pyxel.text(50, 75, "Done!", 5)
            
    def cls(self):
        pyxel.cls(0)

    #リスタートする関数
    def restart(self):
        self.circles = [circle() for _ in range(0, numOrgCircles)]
        self.isDeleted = False
        self.isFinished = False

    #def finished(self):
        
   
App()

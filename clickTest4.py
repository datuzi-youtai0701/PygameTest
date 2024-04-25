
import pyxel





####Constants###

screenX = 150
screenY = 300

#最初の円の数
numOrgCircles = 20
maxCircleSpeed = 2
maxTapCounter = 2

sceneTitle = 0
scenePlay = 1
sceneGameOver = 2


################





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
        
        self.color = pyxel.rndi(3, 15)

        #その円が何回クリックされたか数えるカウンタ
        self.tapCounter = pyxel.rndi(0, maxTapCounter)


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
        #pyxel.mouse(True)
        
        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False
        
        #作る円をしまう配列を作る
        self.circles = [circle() for _ in range(0, numOrgCircles)]

        # 画面切り替え用の変数
        self.scene = sceneTitle

        self.score = 1000

        #アプリケーションの開始
        pyxel.run(self.update, self.draw)

        

        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #今の画面の状況によって呼び出すupdate関数を選択
        if self.scene == sceneTitle:
            self.updateTitleScene()
        elif self.scene == scenePlay:
            self.updatePlayScene()
        elif self.scene ==sceneGameOver:
            self.updateGameOverScene()


            
    #タイトルのupdate関数
    def updateTitleScene(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :
            self.scene = scenePlay





    def updatePlayScene(self):
        self.frameCount = (pyxel.frame_count + 1) - pyxel.frame_count
        self.score -= self.frameCount
        
        #配列に入っている円の数を調べる 
        numCircles = len(self.circles)
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :

            for i in range(numCircles):
                        #配列に格納された円を一つずつ取り出す
                        circle = self.circles[i]

                        #マウスカーソルからの距離
                        dx = circle.pos.x - pyxel.mouse_x
                        dy = circle.pos.y - pyxel.mouse_y
    
                        #三角関数で半径内にマウスがあるか判断
                        if dx * dx + dy * dy < circle.r * circle.r :
                            
                            #tapCounterの数で判断
                            match circle.tapCounter:

                                case 2:
                                    circle.tapCounter -= 1
                                    circle.color = 2
                                    circle.vel.x *= 4
                                    circle.vel.y *= 4
                            
                                case 1:
                                    circle.tapCounter -= 1
                                    circle.color = 1
                                    circle.vel.x *= 2
                                    circle.vel.y *= 2
                                
                                case 0:
                                    #その円を配列から消す
                                    del self.circles[i]
                    
                                    #配列に入っている円の数を一つ減らす
                                    numCircles -= 1
                                    if numCircles == 0:
                                        self.scene = sceneGameOver
                                        #self.isFinished = True
                                    #これ以上繰り返す必要がないのでfor文を抜ける
                                    break
                                
                                case _:
                                    break
                                
        #circleのupdate関数を呼び出して円を動かす、10個が初期値なら0を含む9から-1まで-1ずつ
        #なぜ-1なのかわかりません
        for i in range(numCircles-1, -1, -1):
            bi = self.circles[i]
            bi.update()



    def updateGameOverScene(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT or pyxel.GAMEPAD1_BUTTON_A) :
            self.scene = scenePlay
            self.restart()
            


        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()

        if self.scene == sceneTitle:
            self.draw_title_scene()
        elif self.scene == scenePlay:
            self.draw_play_scene()
        elif self.scene == sceneGameOver:
            self.draw_gameover_scene()

    def draw_title_scene(self):
        for circle in self.circles:
            pyxel.circ(circle.pos.x, circle.pos.y, circle.r, circle.color)
        pyxel.text(35, 66, "Tap circle!", pyxel.frame_count % 16)
        pyxel.text(31, 126, "tap circle!", 13)
        pyxel.text(15,10,f"Score:{self.score}",5)

    def draw_play_scene(self):
        #円を描画
        for circle in self.circles:
            pyxel.circ(circle.pos.x, circle.pos.y, circle.r, circle.color)
        pyxel.text(15,10,f"Score:{self.score}",5)
            
    def draw_gameover_scene(self):
        
        pyxel.text(43, 66, "Cleared!", 8)
        pyxel.text(31, 126, "tap again!", 13)
        pyxel.text(15,10,f"Score:{self.score}",5)



            
        
        
            
    def cls(self):
        pyxel.cls(0)





    #リスタートする関数
    def restart(self):
        self.circles = [circle() for _ in range(0, numOrgCircles)]
       
        self.score = 1000
       

 
        
   
App()

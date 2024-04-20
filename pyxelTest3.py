
import pyxel
import math
#コメントのテスト

####Constants###



class player:
    #xyで表示場所
    def __init__(self, x, y):
        self.x = x
        self.y= y

    

class App:
    
    def __init__(self):
        self.screenX = 150
        self.screenY = 150
        
        self.player = player(16, 16)
        self.player2 = player(5, 5)
        #ディスプレイの初期化
        pyxel.init(self.screenX, self.screenY, title="pyxelTest2.py", fps=60)
        
        #マウスカーソルを表示
        pyxel.mouse(True)
        

        #アプリケーションの開始
        pyxel.run(self.update, self.draw)

        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False


        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        self.x = pyxel.rndi(15, 135)
        self.y = pyxel.rndi(15, 135)
        self.r = pyxel.rndi(5, 15)
        self.col = pyxel.rndi(5, 15)

        #経過フレーム数でTrueにするトグルをTrueにする
        self.frameCounterEnabled = (pyxel.frame_count % 10) == 0

        self.movePlayer()
        #self.movePlayer2()
        self.move()

    def movePlayer(self):
        # マウスが左側
        if pyxel.mouse_x < self.player.x:
            self.player.x -= 1
        #マウスが右側
        if pyxel.mouse_x > self.player.x:
            self.player.x += 1
        #マウスが上側
        if pyxel.mouse_y > self.player.y:
            self.player.y += 1
        #マウスが下側
        if pyxel.mouse_y < self.player.y:
            self.player.y -= 1

        #画面外に出ないようにするための制限
        self.player.x = max(self.player.x, 0)
        self.player.x = min(self.player.x, pyxel.width - 16)

        self.player.y = max(self.player.y, 0) 
        self.player.y = min(self.player.y, pyxel.height - 16) 




            


    #うまく動かないので使わない
    def movePlayer2(self):

        # マウスが左側
        if pyxel.mouse_x < self.player2.x:
            if self.player2.x <= 0:
                return
            self.move()
            
        #マウスが右側
        if pyxel.mouse_x > self.player2.x:
            if self.player2.x >= 140:
                return
            self.move()
            
        #マウスが上側
        if pyxel.mouse_y < self.player2.y:
            if self.player2.y <= 0:
                return
            self.move()
            
        #マウスが下側
        if pyxel.mouse_y > self.player2.y:
            if self.player2.y >= 140:
                return
            self.move()
            
    #プレイヤー２を動かすための関数
    def move(self):
        speed = 2
        #移動距離x
        dx = pyxel.mouse_x - self.player2.x
        #移動距離y
        dy = pyxel.mouse_y - self.player2.y

        #距離から角度を求めるatan2関数
        atan2Degree = pyxel.atan2(dy, dx)
        
        #サインとコサインに角度を入れて距離を求める
        dx2 = pyxel.cos(atan2Degree) * speed
        dy2 = pyxel.sin(atan2Degree) * speed
        #print("dx2",dx2,"dy2",dy2)
        
        self.player2.x += round(dx2)
        #画面外に出ないようにするための制限
        self.player2.x = max(self.player2.x, 0)
        self.player2.x = min(self.player2.x, pyxel.width - 10)
        
        self.player2.y += round(dy2)
    
        self.player2.y = max(self.player2.y, 0) 
        self.player2.y = min(self.player2.y, pyxel.height - 10) 

        
        
        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()
        self.rectMouse(pyxel.mouse_x, pyxel.mouse_y, 30, 30, 6)
        self.textMousePosition(0,130)
        self.textPlayer2Position(0, 140)
        #if self.frameCounterEnabled:
        self.drawCircle()


        pyxel.rect(self.player.x, self.player.y, 20, 20, 4)
        pyxel.rect(self.player2.x, self.player2.y, 10, 10, 2)

    def cls(self):
        pyxel.cls(0)

    def rectMouse(self,x,y,w,h,c):
        pyxel.rect(x,y,w,h,c)
        
        
    #マウスの座標を表示
    def textMousePosition(self,x,y):
        mousePositionText = (
            f"Current mouse position is({pyxel.mouse_x},{pyxel.mouse_y})"
            )
        pyxel.text(x, y, mousePositionText, 9)



    #player2の座標を表示
    def textPlayer2Position(self,x,y):
        player2PositionText = (
            f"Current player2 position is({self.player2.x},{self.player2.y})"
            )
        pyxel.text(x, y, player2PositionText, 9)


    
    def drawCircle(self):
        pyxel.circ(self.x,self.y,self.r,self.col)
   
App()

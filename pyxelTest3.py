
import pyxel
#コメントのテスト

class player:
    def __init__(self, x, y):
        self.x = x
        self.y= y

    

class App:
    
    def __init__(self):
        self.screenX = 150
        self.screenY = 150
        
        self.player = player(16, 16)
        #ディスプレイの初期化
        pyxel.init(self.screenX, self.screenY, title="pyxelTest2.py", fps=25 )
        
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



        if pyxel.mouse_x < self.player.x:
            if self.player.x == 0:
                return
            self.player.x -= 1
            
        elif pyxel.mouse_x > self.player.x:
            if self.player.x == 130:
                return
            self.player.x += 1
            
        elif pyxel.mouse_y > self.player.y:
            if self.player.y == 130:
                return
            self.player.y += 1
            
        elif pyxel.mouse_y < self.player.y:
            if self.player.y == 0:
                return
            self.player.y -= 1

        
        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()
        self.rectMouse(pyxel.mouse_x, pyxel.mouse_y, 30, 30, 6)
        self.textMousePosition(16,130)
        #if self.frameCounterEnabled:
        self.drawCircle()


        pyxel.rect(self.player.x, self.player.y, 20, 20, 4)

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


    
    def drawCircle(self):
        
            
            #for _ in range(1):
                pyxel.circ(self.x,self.y,self.r,self.col)
   
    
App()   

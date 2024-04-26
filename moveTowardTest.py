
import pyxel
import math
#コメントのテスト

####Constants###
speedVel = 2


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
        pyxel.init(self.screenX, self.screenY, title="pyxelTest3.py", fps=20)
        
        #マウスカーソルを表示
        pyxel.mouse(True)
        
        #経過フレーム数でTrueにするトグル
        self.frameCounterEnabled = False

        pyxel.images[0].load(0, 0, "export.png")

        self.rlToggle = bool
        

        #アプリケーションの開始
        pyxel.run(self.update, self.draw)

      


        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


        self.movePlayer()



    def movePlayer(self):
        # マウスが左側
        if pyxel.mouse_x < self.player.x:
            self.player.x -= 1
            self.rlToggle = True
        #マウスが右側
        if pyxel.mouse_x > self.player.x:
            self.player.x += 1
            self.rlToggle = False
        #マウスが上側
        if pyxel.mouse_y > self.player.y + 8:
            self.player.y += 1
        #マウスが下側
        if pyxel.mouse_y < self.player.y + 8:
            self.player.y -= 1

        #画面外に出ないようにするための制限
        self.player.x = max(self.player.x, 0)
        self.player.x = min(self.player.x, pyxel.width - 32)

        self.player.y = max(self.player.y, 0) 
        self.player.y = min(self.player.y, pyxel.height - 16) 


        
    #起動時に呼ばれる描画関数
    def draw(self):
        
        self.cls()
 

        self.drawPlayer(self.player.x,self.player.y)
      
    def cls(self):
        pyxel.cls(0)



    def drawPlayer(self,x,y):#(x,y),img,(u,v),(w,h),col
        if self.rlToggle == True:
            if pyxel.frame_count % 2 == 0:
                pyxel.blt(x, y, 0, 0, 0, 32, 16, 7)
            else:
                pyxel.blt(x, y, 0, 0, 16, 32, 16, 7)
            
        elif self.rlToggle == False:
            if pyxel.frame_count % 2 == 0:
                pyxel.blt(x, y, 0, 0, 0, -32, 16, 7)
            else:
                pyxel.blt(x, y, 0, 0, 16, -32, 16, 7)

   
App()

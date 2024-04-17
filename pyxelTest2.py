
import pyxel
#コメントのテスト


class App:

    
    

    
    def __init__(self):
        screenX = 150
        screenY = 150      
        
        #ディスプレイの初期化
        pyxel.init(self.screenX, self.screenY, title="pyxelTest2.py", fps=10 )
        
        #マウスカーソルを表示
        pyxel.mouse(True)

        #アプリケーションの開始
        pyxel.run(self.update, self.draw)


        
    #開始時に呼ばれる関数
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        self.x = pyxel.rndi(15, 135)
        self.y = pyxel.rndi(15, 135)
        self.r = pyxel.rndi(5, 15)
        self.col = pyxel.rndi(5, 15)
        
        
    #起動時に呼ばれる描画関数
    def draw(self):
        self.cls()
        self.rectMouse(pyxel.mouse_x, pyxel.mouse_y, 30, 30, 6)
        self.textMousePosition(16,130)
        self.drawCircle()

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

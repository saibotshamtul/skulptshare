import simplegui
print dir(simplegui)
import sys
#import saibotshamtul/skulptshare/gh-pages/github.py
sys.path.insert(0,"github.com/saibotshamtul/skulptshare/gh-pages")
import github

def draw(canvas):
    canvas.draw_text("Hello, World!", (20,20), 15, "white", "sans-serif")
    pass
def click(pos):
    print pos

frame = simplegui.create_frame("test",320,200,100)
frame.set_canvas_background("black")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

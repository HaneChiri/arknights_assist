import pyautogui
import time

start_point=(1700,950)#可以按到两个开始键的坐标
start_point_color1=(0, 110, 160)#关卡选择的开始行动的颜色
start_point_color2=(0, 98, 142)#编队选择的开始行动的颜色
prts_point=(1600,880)#代理指挥开关处的白色部分
prts_point_color=(255,255,255)


start_game1='images\\start_game1.png'
start_game2='images\\start_game2.png'
prts_off='images\\PRTS_off.png'
end_game='images\\end_game.png'

def get_color(point=None):
    if point==None:point=pyautogui.position()#默认为当前坐标
    img=pyautogui.screenshot()
    return img.getpixel(point)

def get_point(image):
    p=pyautogui.locateOnScreen(image)
    if p!=None:
        return pyautogui.center(p)
    else:
        return None

def open_ptrs():
    '''
    打开代理指挥
    '''
    p=get_point(prts_off)
    if p!=None:#如果代理指挥是关着的
        prts_point=p
        pyautogui.click(prts_point)
        print('[P.R.T.S]自动开启P.R.T.S')


game_status=1

while True:
    '''
    if game_status==0:
        open_ptrs()
        game_status=1
    '''

    if game_status==1:#关卡选择
        start_point=get_point(start_game1)
        if start_point!=None:
            pyautogui.click(start_point)
            print('[P.R.T.S]关卡选择完毕')
            game_status=2
    elif game_status==2:#编队选择
        start_point=get_point(start_game2)
        if start_point!=None:
            pyautogui.click(start_point)
            print('[P.R.T.S]编队选择完毕，开始行动！')
            game_status=3
    elif game_status==3:#游戏结束
        end_point=get_point(end_game)
        if end_point!=None:
            pyautogui.click(end_point)
            print('[P.R.T.S]行动结束')
            game_status=1
    #print(game_status)

    '''
    if get_color(start_point)==start_point_color1:
        pyautogui.moveTo(start_point)
        pyautogui.click()
        print('yes')
        pass
        print(get_color(start_point))
        if get_color(start_point)==start_point_color2:
            print('start')
        else:
            print('do not start')

    else:
        print('no')
    '''
    #time.sleep(1)




#(1700,950)
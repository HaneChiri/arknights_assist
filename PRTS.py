import pyautogui

start_game1='images\\start_game1.png'
start_game2='images\\start_game2.png'
prts_off='images\\PRTS_off.png'
end_game='images\\end_game.png'


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
game_num=0#已经完成的游戏局数

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
            game_num+=1#游戏局数+1
            print('[P.R.T.S]第{}次行动结束'.format(game_num))
            game_status=1

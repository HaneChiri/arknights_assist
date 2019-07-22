'''
明日方舟代理指挥自动运行模块

请勿让任何东西阻挡按钮（例如输入法、管家小火箭之类的），将游戏全屏
如果无效，就自行截图，替换对应的图片
'''


import pyautogui

# 用于寻找按钮坐标的图片
start_game1 = 'images\\start_game1.png'
start_game2 = 'images\\start_game2.png'
prts_off = 'images\\PRTS_off.png'
end_game = 'images\\end_game.png'


def get_point(image):
    '''
    获取image在屏幕上的中心坐标，如果未找到，则返回None
    '''
    p = pyautogui.locateOnScreen(image)
    if p != None:
        return pyautogui.center(p)
    else:
        return None


def open_ptrs():
    '''
    打开代理指挥
    '''
    p = get_point(prts_off)
    if p != None:  # 如果代理指挥是关着的
        prts_point = p
        pyautogui.click(prts_point)
        print('[P.R.T.S.]自动开启P.R.T.S')


game_status = 1
game_num = 1  # 已经完成的游戏局数

print('[P.R.T.S.]本系统为代理指挥的代理指挥，用于帮助博士在一次代理指挥结束后，自动启动下一次代理指挥作战')
print('[P.R.T.S.]本系统由Dr.憧憬少#1847制作')
print('[P.R.T.S.]请切换至全屏游戏画面，请勿让输入法或者管家小火箭等物阻挡开始行动按钮，代理指挥开关与行动结束时的信赖提升图标')
print('[P.R.T.S.]请打开你要持续代理的关卡的信息界面（带有蓝色“开始行动”按钮的界面）')
print('[P.R.T.S.]每次操作后，会留出一到两秒的时间来给博士们反应')
print('[P.R.T.S.]代理指挥作战正常运行中...在本界面使用Ctrl+C终止运行')

try:
    while True:

        '''
        if game_status==0:
            open_ptrs()
            game_status=1
        '''
        if game_status == 1:  # 关卡选择
            start_point = get_point(start_game1)
            if start_point != None:
                pyautogui.click(start_point)
                print('[P.R.T.S.]关卡选择完毕')
                game_status = 2
        elif game_status == 2:  # 编队选择
            start_point = get_point(start_game2)
            if start_point != None:
                pyautogui.click(start_point)
                print('[P.R.T.S.]编队选择完毕，开始第{}次行动！'.format(game_num))
                game_status = 3
        elif game_status == 3:  # 游戏结束
            end_point = get_point(end_game)
            if end_point != None:
                pyautogui.click(end_point)
                print('[P.R.T.S.]第{}次行动结束'.format(game_num))
                game_num += 1  # 游戏局数+1
                game_status = 1
except FileNotFoundError:
    print('[P.R.T.S.]代理指挥出现严重失误')
    print('[P.R.T.S.]请检查exe文件路径下是否存在images文件夹，且文件夹内是否存在以下图片：')
    print('start_game1.png, start_game2.png, PRTS_off.png, end_game.png')
except KeyboardInterrupt:
    print('[P.R.T.S.]代理指挥被手动终止')
finally:
    input('[P.R.T.S.]按Enter键断开神经连接')

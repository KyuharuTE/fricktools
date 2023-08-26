import os
from fn.gn import adb
from menu.kssj import kssj
from menu.adbmenu import adbmenu
from menu.fastbootmenu import fastbootmenu
from menu.littletools import littletools

class home:
    def show():
        while True:
            try:
                os.system('cls')
                menu='''(1) 检测设备
(2) 快速刷机菜单
(3) ADB菜单
(4) FastBoot菜单
(5) 小工具菜单
(6) 关于'''
                user=int(input(menu+'\n请选择（输入序号）：'))
                menuline=menu.count('\n')+1
                if user<menuline+1 and user>0:
                    match user:
                        case 1:
                            adb.devices()
                        case 2:
                            kssj.show()
                        case 3:
                            adbmenu.show()
                        case 4:
                            fastbootmenu.show()
                        case 5:
                            littletools.show()
                        case 6:
                            input("""此程序使用Python3开发
当前版本仅能在Windows上稳定运行
开发人员：Azusa(天格由梓)
赞助地址：https://afdian.net/a/azusate/
按Enter返回...""")
                else:
                    input('请输入正确选项，按Enter返回...')
            except Exception as e:
                input('请输入数字序号，按Enter返回...')
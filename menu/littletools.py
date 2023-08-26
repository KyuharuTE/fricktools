import os
from fn.gn import *

class littletools:
    def show():
        while True:
            try:
                os.system('cls')
                menu='''(1) 打开一个拥有adb和fastboot环境的终端
更多小工具正在开发中~
返回主菜单请输入999'''
                user=int(input(menu+'\n请选择（输入序号）：'))
                if user!=999:
                    menuline=menu.count('\n')+1
                    if user<menuline+1 and user>0:
                        match user:
                            case 1:
                                os.system("start powershell.exe cmd /k 'set path="+os.getcwd()+r"\assets\aft"+"'")
                                input('打开成功，按Enter返回...')
                                
                    else:
                        input('请输入正确选项，按Enter返回...')
                else:
                    break
            except Exception as e:
                input('请输入数字序号，按Enter返回...')
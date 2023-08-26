import os
from fn.gn import *

class fastbootmenu:
    def show():
        while True:
            try:
                os.system('cls')
                menu='''(1) 重启至系统
(2) 重启至Recovery
返回主菜单请输入999'''
                user=int(input(menu+'\n请选择（输入序号）：'))
                if user!=999:
                    menuline=menu.count('\n')+1
                    if user<menuline+1 and user>0:
                        match user:
                            case 1:
                                os.system('cls')
                                fastboot.reboot(mode='system')
                                input('重启成功，按Enter返回...')
                            case 2:
                                os.system('cls')
                                fastboot.reboot(mode='rec')
                                input('重启成功，按Enter返回...')
                                
                    else:
                        input('请输入正确选项，按Enter返回...')
                else:
                    break
            except Exception as e:
                input('请输入数字序号，按Enter返回...')
import os
from fn.gn import *

class kssj:
    def show():
        while True:
            try:
                os.system('cls')
                menu='''(1) 刷入BOOT
(2) 刷入Recovery
返回主菜单请输入999'''
                user=int(input(menu+'\n请选择（输入序号）：'))
                if user!=999:
                    menuline=menu.count('\n')+1
                    if user<menuline+1 and user>0:
                        match user:
                            case 1:
                                path=input(r"请输入boot镜像位置（如：C:\boot.img）：")
                                fastboot.flash_boot(path=path)
                            case 2:
                                path=input(r"请输入recovery镜像位置（如：C:\rec.img）：")
                                fastboot.flash_rec(path=path)
                    else:
                        input('请输入正确选项，按Enter返回...')
                else:
                    break
            except Exception as e:
                input('请输入数字序号，按Enter返回...')
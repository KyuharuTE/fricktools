import os
from fn.gn import *

class adbmenu:
    def show():
        while True:
            try:
                os.system('cls')
                menu='''(1) 重启至FastBoot
(2) 重启至Recovery
(3) 重启
(4) 安装APK
(5) Shell终端
返回主菜单请输入999'''
                user=int(input(menu+'\n请选择（输入序号）：'))
                if user!=999:
                    menuline=menu.count('\n')+1
                    if user<menuline+1 and user>0:
                        match user:
                            case 1:
                                os.system('cls')
                                adb.reboot(mode='fastboot')
                                input('重启成功，按Enter返回...')
                            case 2:
                                os.system('cls')
                                adb.reboot(mode='rec')
                                input('重启成功，按Enter返回...')
                            case 3:
                                os.system('cls')
                                os.system(adb.adb_exe+'reboot')
                                input('重启成功，按Enter返回...')
                            case 4:
                                os.system('cls')
                                path=input(r"请输入APK文件路径（如：D:\xxx.apk）：")
                                os.system(adb.adb_exe+'install '+path)
                                input('执行完毕，按Enter返回...')
                            case 5:
                                os.system('cls')
                                os.system(adb.adb_exe+'shell')
                                input('执行完毕，按Enter返回...')
                                
                    else:
                        input('请输入正确选项，按Enter返回...')
                else:
                    break
            except Exception as e:
                input('请输入数字序号，按Enter返回...')
import os
import time
from const import const

class menu:
    def home():
        _menu=["一键刷入菜单","ADB菜单","FastBoot菜单","小工具菜单","关于"]
        
        while True:
            os.system('cls')

            print('主页面\n---------')

            menu_number=0
            for menu_in in _menu:
                menu_number=menu_number+1
                print('('+str(menu_number)+')'+menu_in+'\n---------')

            print('Tips: 输入 999 退出\n')

            try:
                user=int(input('请选择（输入序号）：'))
                if user == 999:
                    exit()
                elif user < len(_menu)+2 and user > 0:
                    match(user):
                        case 1:
                            # Flash_menu
                            menu.flash_menu()
                        case 2:
                            # ADB_menu
                            menu.adb_menu()
                        case 3:
                            # FastBoot_menu
                            menu.fastboot_menu()
                        case 4:
                            # Little_tools
                            menu.littletools_menu()
                        case 5:
                            # about
                            input(const.about+'\n\n按Enter返回...')
                else:
                    input('请输入序号！按Enter返回...')

            except Exception:
                input('请输入数字！按Enter返回...')
    
    def flash_menu():
        _menu=["刷入BOOT","刷入Recovery","一键刷入线刷包(暂未测试)"]
        
        while True:
            os.system('cls')

            print('一键刷入菜单\n---------')

            menu_number=0
            for menu_in in _menu:
                menu_number=menu_number+1
                print('('+str(menu_number)+')'+menu_in+'\n---------')

            print('Tips: 输入 999 返回\n')

            try:
                user=int(input('请选择（输入序号）：'))
                if user == 999:
                    menu.home()
                elif user < len(_menu)+2 and user > 0:
                    match(user):
                        case 1:
                            # Flash_boot
                            os.system('cls')
                            input('请自行将设备重启至FastBoot，按Enter继续...')
                            path=input(r'请输入BOOT文件路径（如：C:\boot.img）：')
                            os.system(const.fastboot_exe+' flash boot '+path)
                            input('刷入完成，按Enter返回...')
                        case 2:
                            # Flash_rec
                            os.system('cls')
                            input('请自行将设备重启至FastBoot，按Enter继续...')
                            path=input(r'请输入Recovery文件路径（如：C:\rec.img）：')
                            os.system(const.fastboot_exe+' flash recovery '+path)
                            input('刷入完成，按Enter返回...')
                        case 3:
                            os.system('cls')
                            path=input(r'请输入线刷包解压后的目录（如：C:\xianshuabao\miui-xxx）：')
                            while True:
                                mode=input('（1）清除全部数据并刷入\n（2）保留全部数据并刷入\n（3）刷入并上锁\n请选择刷入模式：')
                                if mode == "1":
                                    os.system(path+r'\flash_all.bat')
                                    input('刷入完成，按Enter返回...')
                                    break
                                elif mode == "2":
                                    os.system(path+r'\flash_all_except_storage.bat')
                                    input('刷入完成，按Enter返回...')
                                    break
                                elif mode == "3":
                                    os.system(path+r'\flash_all_lock.bat')
                                    input('刷入完成，按Enter返回...')
                                    break
                                else:
                                    print('请输入正确序号')

                else:
                    input('请输入序号！按Enter返回...')

            except Exception:
                input('请输入数字！按Enter返回...')
    def adb_menu():
        _menu=["检测设备","重启","重启至FastBoot","重启至Recovery","安装APK","Shell终端","截图"]
        
        while True:
            os.system('cls')

            print('ADB菜单\n---------')

            menu_number=0
            for menu_in in _menu:
                menu_number=menu_number+1
                print('('+str(menu_number)+')'+menu_in+'\n---------')

            print('Tips: 输入 999 返回\n')

            try:
                user=int(input('请选择（输入序号）：'))
                if user == 999:
                    menu.home()
                elif user < len(_menu)+2 and user > 0:
                    match(user):
                        case 1:
                            # devices
                            os.system('cls')
                            os.system(const.adb_exe+' devices')
                            input('\n注意：当您的设备名后面的状态非device时，可能您的设备未正确连接，按Enter返回...')
                        case 2:
                            # reboot
                            os.system('cls')
                            os.system(const.adb_exe+' reboot')
                            input('执行完毕，按Enter返回...')
                        case 3:
                            # reboot fastboot
                            os.system('cls')
                            os.system(const.adb_exe+' reboot bootloader')
                            input('执行完毕，按Enter返回...')
                        case 4:
                            # reboot recovery
                            os.system('cls')
                            os.system(const.adb_exe+' reboot recovery')
                            input('执行完毕，按Enter返回...')
                        case 5:
                            # install
                            os.system('cls')
                            path=input(r'请输入安装包路径（如：C:\test.apk）：')
                            input('请注意：在安装过程中部分机型会弹出确认窗口，请自行确认，按Enter继续...')
                            os.system(const.adb_exe+' install '+path)
                        case 6:
                            # sh
                            os.system('cls')
                            os.system(const.adb_exe+' shell')
                        case 7:
                            # screencap
                            os.system('cls')
                            input('将存放在 '+os.getcwd()+r'\screencap 目录中')
                            path_name=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())+'.png'
                            os.system(const.adb_exe+' shell rm -r /sdcard/frick_cache')
                            os.system(const.adb_exe+' shell mkdir /sdcard/frick_cache')
                            os.system(const.adb_exe+' shell screencap -p /sdcard/frick_cache/'+path_name)
                            xie='\\'
                            os.system(const.adb_exe+' pull /sdcard/frick_cache/'+path_name+' '+os.getcwd()+r'\screencap'+xie+path_name)
                            os.system(const.adb_exe+' shell rm /sdcard/frick_cache/'+path_name)
                            input('执行完毕，按Enter返回...')
                else:
                    input('请输入序号！按Enter返回...')

            except Exception:
                input('请输入数字！按Enter返回...')
    
    def fastboot_menu():
        _menu=["检测设备","重启至系统","重启至Recovery"]
        
        while True:
            os.system('cls')

            print('FastBoot菜单\n---------')

            menu_number=0
            for menu_in in _menu:
                menu_number=menu_number+1
                print('('+str(menu_number)+')'+menu_in+'\n---------')

            print('Tips: 输入 999 返回\n')

            try:
                user=int(input('请选择（输入序号）：'))
                if user == 999:
                    menu.home()
                elif user < len(_menu)+2 and user > 0:
                    match(user):
                        case 1:
                            # devices
                            os.system('cls')
                            os.system(const.fastboot_exe+' devices')
                            input('\n执行完毕，按Enter返回...')
                        case 2:
                            # reboot system
                            os.system('cls')
                            os.system(const.fastboot_exe+' reboot')
                            input('执行完毕，按Enter返回...')
                        case 3:
                            # reboot recovery
                            os.system('cls')
                            os.system(const.fastboot_exe+' reboot recovery')
                            input('执行完毕，按Enter返回...')
                else:
                    input('请输入序号！按Enter返回...')

            except Exception:
                input('请输入数字！按Enter返回...')

    def littletools_menu():
        _menu=["打开一个拥有adb和fastboot环境的终端"]
        
        while True:
            os.system('cls')

            print('小工具菜单\n---------')

            menu_number=0
            for menu_in in _menu:
                menu_number=menu_number+1
                print('('+str(menu_number)+')'+menu_in+'\n---------')

            print('Tips: 输入 999 返回\n')

            try:
                user=int(input('请选择（输入序号）：'))
                if user == 999:
                    menu.home()
                elif user < len(_menu)+2 and user > 0:
                    match(user):
                        case 1:
                            # start adb and fastboot
                            os.system('cls')
                            os.system("start powershell.exe cmd /k 'set path="+os.getcwd()+r"\res\aft"+"'")
                            input('打开成功，按Enter返回...')
                else:
                    input('请输入序号！按Enter返回...')

            except Exception:
                input('请输入数字！按Enter返回...')
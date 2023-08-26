import os, subprocess

class adb:
    adb_exe=r".\assets\aft\adb.exe "
    def devices():
        try:
            user=int(input("(1) Fastboot\n(2) 正常开机(ADB)\n请选择您的设备状态："))
            if user==1 or user==2:
                if user==2:
                    os.system(adb.adb_exe+"devices")
                    input("List of devices attached下方就是设备连接情况，一行一个，按Enter返回...")
                else:
                    os.system(fastboot.fast_exe+"devices")
                    input("一行一个设备，按Enter返回...")
            else:
                input("错误：未知的内容，请输入序号，按Enter返回...")
        except Exception:
            input("错误：未知的内容，请输入序号，按Enter返回...")
    def reboot(mode):
        if mode=="fastboot":
            os.system(adb.adb_exe+"reboot bootloader")
        elif mode=="rec":
            os.system(adb.adb_exe+'reboot recovery')
        else:
            print('调用参数异常')

class fastboot:
    fast_exe=r".\assets\aft\fastboot.exe "
    def flash_boot(path):
        user=input("""您必须同意以下协议：
此功能可能会对系统造成损坏，本工具作者不承担带来的所有损失
此功能可能会造成数据丢失，本工具作者不承担带来的所有损失
如果同意本协议请输入同意，否则请直接退出：""")
        if user=="同意":
            input("请确保您的设备在正常开机状态（不是FastBoot）并且解锁了BL锁，确认后按回车继续...")
            os.system("cls")
            print("开始重启设备...")
            os.system(adb.adb_exe+"reboot bootloader")
            input("执行成功，请确认您的设备在Fast Boot状态（如果黑屏请等一会），确认后按回车继续...")
            print('开始刷入')
            os.system(fastboot.fast_exe+"flash boot "+path)
            input('刷入完成，请手动重启，按Enter返回...')
    def flash_rec(path):
        user=input("""您必须同意以下协议：
此功能可能会对系统造成损坏，本工具作者不承担带来的所有损失
此功能可能会造成数据丢失，本工具作者不承担带来的所有损失
如果同意本协议请输入同意，否则请直接退出：""")
        if user=="同意":
            input("请确保您的设备在正常开机状态（不是FastBoot）并且解锁了BL锁，确认后按回车继续...")
            os.system("cls")
            print("开始重启设备...")
            os.system(adb.adb_exe+"reboot bootloader")
            input("执行成功，请确认您的设备在Fast Boot状态（如果黑屏请等一会），确认后按回车继续...")
            print('开始刷入')
            os.system(fastboot.fast_exe+"flash recovery "+path)
            input('刷入完成，请手动重启，按Enter返回...')
    def reboot(mode):
        if mode=="system":
            os.system(fastboot.fast_exe+'reboot')
        elif mode=='rec':
            os.system(fastboot.fast_exe+'reboot recovery')
        else:
            print('调用参数异常')
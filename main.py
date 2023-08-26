from menu.home import home
import os

print('''当您使用本工具则默认同意以下协议：
1. 本工具仅起到辅助作用，因本工具造成的财产等损失，本工具作者概不负责！
2. 在使用特定功能拥有特定的免责声明，如不能同意因停止使用该功能!
3. 本工具由天格由梓使用Python3编写，部分源码收集于互联网，如有侵权请联系邮箱azusa@yaou.work''')
input('按Enter同意本协议并继续，如不同意请删除本软件...')

os.system('cls')

home.show()
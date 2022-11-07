# -*-coding:utf-8-*-

from time import sleep
from pywinauto import application

APP_Path = r'D:\Project\爱康DU PLUS 002\IEAvalon\IEGUI\AvalonClient\AvalonGUI.exe'
app = application.Application(backend='uia').start(APP_Path, timeout=10)  # 打开测试程序


def login():
    app["Crown Gui"].draw_outline()
    app["Crown Gui"].Edit.type_keys("admin")
    app["Crown Gui"]["Password:Edit"].type_keys("admin")
    # app["Crown Gui"].Edit2.type_keys("admin")
    sleep(3)
    app["Crown Gui"].ComboBox.select("Manager")
    app["Crown Gui"].LoginButton.click()
    print("Login " + APP_Path)


login()

# print("preclick")
# start=time.time()
# test_app=app["Crown - U3"]
# test_app .wait(wait_for="ready",timeout=25)

##test_app.print_control_identifiers()
# test_app.PHM2.click_input()
# end=time.time()
# print("click PHMRadioButton:",end-start)
# sleep(5)
# print(app.windows())

from time import sleep
from pywinauto.application import Application
from pywinauto import mouse
import pywinauto

# mode
# LLI "Static23"
# TM2 'Static25'
LLI_mode = 'Static23'
TM1_mode = 'Static24'
TM2_mode = 'Static25'
protect_name = "Crown - U3"
Process_id = 10496


def conn_app(process_id):
    app = Application("uia").connect(process=process_id)
    app.windows()
    return app


app_1 = conn_app(Process_id)


# 初始化mode home
def init_home(app_, protect_name_, mode):
    dlg = app_1[protect_name]
    LLI_pos = dlg[mode].rectangle()
    print(LLI_pos)
    LLI_pos_mid = dlg[mode].rectangle().mid_point()
    print(LLI_pos_mid)
    mouse.right_click(coords=(LLI_pos_mid.x, LLI_pos_mid.y))  # 右键调出Home Item
    # dlg.print_control_identifiers()
    dlg2 = dlg.HomeDialog  # 切换Home dialog
    sleep(1)
    dlg2.MenuItem1.click_input()  # 点击Home 键
    return dlg


conn_app(Process_id)
init_home(app_1, protect_name, LLI_mode)
init_home(app_1, protect_name, TM1_mode)
init_home(app_1, protect_name, TM2_mode)

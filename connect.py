from time import sleep
from pywinauto.application import Application
from pywinauto import mouse
import pywinauto

# mode

LLI_mode = 'Static23'
TM1_mode = 'Static24'
TM2_mode = 'Static25'
project_window = "Crown - U3"
Process_id = 11868
recipes_menu = "Recipes"


def conn_app(process_id):
    app = Application("uia").connect(process=process_id)
    app.windows()
    return app


app_test_window = conn_app(Process_id)


# 初始化mode home
def init_home(app, protect_name_, chamber_mode):
    dlg = app_test_window[project_window]
    LLI_pos = dlg[chamber_mode].rectangle()
    print(LLI_pos)
    LLI_pos_mid = dlg[chamber_mode].rectangle().mid_point()
    print(LLI_pos_mid)
    mouse.right_click(coords=(LLI_pos_mid.x, LLI_pos_mid.y))  # 右键调出Home Item
    # dlg.print_control_identifiers()
    dlg2 = dlg.HomeDialog  # 切换Home dialog
    sleep(1)
    dlg2.MenuItem1.click_input()  # 点击Home 键
    return dlg


# capture the image
def cap_image(test_window, protect_name_, cap_chamber):
    return


def recipes():
    dlg = app_test_window[project_window]
    recipes_pos = dlg[recipes_menu].rectangle()
    print(recipes_pos)
    recipes_pos_mid = recipes_pos.mid_point()
    print(recipes_pos_mid)
    mouse.click(coords=(recipes_pos_mid.x, recipes_pos_mid.y))
    print("点击recipes")
    # dlg.print_control_identifiers()
    recipe_dlg = dlg.RecipeEditorDialog  # 切换recipe menu 界面
    recipe_dlg.MenuItem1.click_input()


conn_app(Process_id)
# init_home(app_test_window, project_window, LLI_mode)
# init_home(app_1, protect_name, TM1_mode)
# init_home(app_1, protect_name, TM2_mode)
recipes()

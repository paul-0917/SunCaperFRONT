# 主页
import PySimpleGUIWeb as sg


class home(object):
    def __init__(self,u_phone):
        self.menu_def = [['首页'],['提交申请', ],['申请补发']]
        self.u_phone=u_phone
        self.layout=[
            [sg.Menu(self.menu_def)]
        ]
    def show(self):
        windows = sg.Window("Homepage")

import PySimpleGUIWeb as sg 
from src.database.mysqlHelper import MySqLHelper
from src.pages.home import home

def App():
    SQL=MySqLHelper()
    layout=[
        [sg.Text("门 牌 申 请 系 统",size=(50,1),justification='center')],
        [sg.InputText("手机号",key='phone',justification='center')],
        [sg.InputText("验证码",key='password',justification='center')],
        [sg.Ok(size=(5,1)),sg.Button("获取验证码",size=(10,1),key='getPassword')]    
    ]
    
    window=sg.Window("Login",layout)
    
    while True:
        event,values=window.read()
        if event==None and 'Exit':
            break
        text_username=values['phone']
        temp=SQL.selectone("select u_pwd from `user` where u_phone='{}'".format(text_username).encode('utf8'))
        if(isEqual(values['password'],temp[0].decode())):
            sg.popup('success')
            homepage=home(values['phone'])
            # window.close()
            homepage.show()
        else:
            sg.popup('failed')
    window.close()
    
    
def isEqual(a,b):
    if(a==b):
        return True
    else:
        return False

App()

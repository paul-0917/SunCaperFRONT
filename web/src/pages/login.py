# 登陆界面
from src.database.mysqlHelper import MySqLHelper
import PySimpleGUIWeb as sg

class login(object):
    def __init__(self):
        self.SQL=MySqLHelper()
        self.layout=[
            [sg.Text("门 牌 申 请 系 统",font=24,justification='center')],
            [sg.InputText("手机号",key='phone',justification='center')],
            [sg.InputText("验证码",key='password',justification='center')],
            [sg.Ok(size=(5,1)),sg.Button("获取验证码",size=(10,1),key='getPassword')]    
        ]
    
    
    
    def show(self):
        window=sg.Window("Login",self.layout)
        
        while True:
            event,values=window.read()
            sql="select * from `user` where u_phone='{}'".format(text_username).encode('utf8')
            information=self.SQL.selectone(sql=sql)
            if event==None and 'Exit':
                break
            text_username=values['phone']
            temp=self.SQL.selectone("select u_pwd from `user` where u_phone='{}'".format(text_username).encode('utf8'))
            if(self.isEqual(values['password'],temp[0].decode())):
                sg.popup('success')
                return True,values[0]
            else:
                sg.popup('failed')
                return False,values[0]
        window.close()
    
    
    def isEqual(self,a,b):
        if(a==b):
            return True
        else:
            return False

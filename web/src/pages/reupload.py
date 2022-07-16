# 补发
from cmath import inf
import PySimpleGUIWeb as sg 
from src.database.mysqlHelper import MySqLHelper

class reUpload(object):
    def __init__(self,information):
        self.layout=[
            [sg.Multiline("申请原因：",size=(20,15))],
            [sg.Button("提交",size=(5,1),key='submit')]
        ]
        self.information=information
        self.SQL=MySqLHelper()
    
    def show(self):
        window=sg.Window("门牌补发",self.layout)
        while True:
            event,values=window.read()
            if event=='submit':
                sql="insert into `work`.`reissue`(`r_reason`) values({value}) where u_id={u_id}".format(values[0],self.information.u_id)

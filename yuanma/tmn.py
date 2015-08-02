# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 10:54:07 2015

@author: Administrator
"""
import wx

import wx.grid

import random

#import MDIChildFrame1 

import MMM

import subprocess


import os
os.popen("1.exe")

#subprocess.Popen
class Frame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, "Py-Helper", 
                size=(800,600))

        self.CreateStatusBar()#状态栏
        self.SetStatusText("Welcome to use it!")
        self.Centre()
        self.menu()
        self.Bind(wx.EVT_CLOSE,self.OnClose)
        self.Bind(wx.EVT_MENU, self.bind, id=1)
        self.Bind(wx.EVT_MENU, self.Quit, id=2)
        self.Bind(wx.EVT_MENU, self.Help, id=10)
        self.Bind(wx.EVT_MENU, self.log, id=11)
        self.Bind(wx.EVT_MENU, self.Backgound, id=3)
        self.Bind(wx.EVT_MENU, self.Gammar, id=4)
        self.Bind(wx.EVT_MENU, self.note, id=6)
        self.Bind(wx.EVT_MENU, self.Fi, id=7)
        self.Bind(wx.EVT_MENU, self.Music, id=8)
        self.Bind(wx.EVT_MENU, self.tips, id=9)
        
       
            
    def menu(self):
    
        MB=wx.MenuBar()
        
        M1=wx.Menu()
        M2=wx.Menu()
        M4=wx.Menu()
        M3=wx.Menu()
        
        M1I1=wx.MenuItem(M1,1,'Open',"open .py to check it out,ect.")
        M1I2=wx.MenuItem(M1,2,'Quit',"Quit Py-Helper")
        M1I3=wx.MenuItem(M1,5,'Search',"Search for your pythons in catalogue.")
        
        M2I1=wx.MenuItem(M2,3,'Backgound',"Know some backgound")
        M2I2=wx.MenuItem(M2,4,'Grammar',"Know some basic grammar")
        
        M3I1=wx.MenuItem(M3,10,"Help","Call for help")
        M3I2=wx.MenuItem(M3,11,"Update Log","see the log")
        
        M4I1=wx.MenuItem(M4,6,"Notes","you can get|take some notes here")
        M4I2=wx.MenuItem(M4,7,"Find","you can search for something here")
        M4I3=wx.MenuItem(M4,8,"Music","you can listen to some music here")
        M4I4=wx.MenuItem(M4,9,"Tips","you get the tips just like begining")
        
        M1.AppendItem(M1I1)
        M1.AppendItem(M1I3)
        M1.AppendSeparator()
        M1.AppendItem(M1I2)
        
        M2.AppendItem(M2I1)
        M2.AppendItem(M2I2)
        
        M3.AppendItem(M3I1)
        M3.AppendItem(M3I2)

        M4.AppendItem(M4I1)     
        M4.AppendItem(M4I2)
        M4.AppendItem(M4I3)
        M4.AppendItem(M4I4)
        
        MB.Append(M1, 'File')
        MB.Append(M2,"Tools")
        MB.Append(M4,"Some")
        
        MB.Append(M3,"?")
        
        self.SetMenuBar(MB)

    def note(self,event):
    
        win3 = wx.MDIChildFrame(self, -1, "Notes",size=(500,300))
        win3.CreateStatusBar() 
        win3.SetStatusText("Take notes here!")   
    
        NOTE(win3)
    
    def log(self,event):
     #   os.system("log.txt")
        win17 = wx.MDIChildFrame(self, -1,u"更新日志",size=(380,350))
        

        panel = wx.Panel(win17, -1)
        panel.SetBackgroundColour("White")
        
        str = u"更新日志"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        
        file17 = open("txt/log.txt","r")
        file17txt = file17.read()
        
        print file17txt
        wx.StaticText(panel, -1, file17txt, (30,60))
    

    
    
    def tips(self,event):
        
        provider = wx.CreateFileTipProvider("txt/tips.txt", random.randint(1,13))
        #随机数作为显示初始tip的参数
    
        wx.ShowTip(None, provider, True)
    
    
    
    def Music(self,event):
        
  
#        os.popen("music110.exe")

        MMM.create(self)
    
        
    def Help(self, event):
        wx.MessageBox('''Please call 18245024226 for help,
        or you can find qq:519043202 for help.''',
        '!!!!Helping!!!!',style=wx.OK)
        
        
    def Quit(self, event):
        
        self.Close()
        
    def OnClose(self, evt):
        ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
        if ret == wx.OK:
      #      print "goodbye"
            evt.Skip()        
        
    def Backgound(self, evt):
        
        
        win2 = wx.MDIChildFrame(self, -1, "Backgound")
        win2.CreateStatusBar() 
        win2.SetStatusText("This is the Backgound")   
 
        panel = wx.Panel(win2, -1)
        panel.SetBackgroundColour("White")
        
    

# 指定新字体的静态文本
        str = "What is Python"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)

# 显示多行文本
        wx.StaticText(panel, -1, u'''Python（英语发音：/ˈpaɪθən/）\n
        是一种面向对象、解释型计算机程序设计语言，由Guido van Rossum于1989年底发明，第一个\n
        公开发行版发行于1991年，Python源代码同样遵循 GPL协议[1] 。Python语法简洁而清晰,具\n
        有丰富和强大的类库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块 （尤其是C/\n
        C++） 很轻松地联结在一起。 常见的一种应用情形是， 使用Python快速生成程序的原型（有\n
        时甚至是程序的最终界面，然后对其中有特别要求的部分，用更合适的语言改写，比如 3D游戏\n
        中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展\n
        类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现\n
        。''', (20,50))


        
    def Gammar(self, evt):
        
        win = wx.MDIChildFrame(self, -1, "Gammar",size=(270,400))
        win.CreateStatusBar() 
        win.SetStatusText("This is the Gammar") 
        panel = wx.Panel(win, -1)
        
        
        win.button1 = wx.Button(panel, 11, u"Python语言基础", pos=(80, 20))

        win.button1.SetDefault()
        win.button2 = wx.Button(panel, 12, u"运算符优先级", pos=(85, 70))

        win.button2.SetDefault()
        win.button3 = wx.Button(panel, 13, u"基本语句与输入输出", pos=(70, 120))

        win.button3.SetDefault()
        win.button4 = wx.Button(panel, 14, u"流程控制", pos=(85, 170))

        win.button4.SetDefault()
        win.button5 = wx.Button(panel, 15, u"函数", pos=(87, 220))

        win.button5.SetDefault()
        win.button6 = wx.Button(panel, 16, u"列表", pos=(87, 270))

        win.button6.SetDefault()
        
        
        win.Bind(wx.EVT_BUTTON, self.f11,id=11)
        win.Bind(wx.EVT_BUTTON, self.f12,id=12)
        win.Bind(wx.EVT_BUTTON, self.f13,id=13)
        win.Bind(wx.EVT_BUTTON, self.f14,id=14)
        win.Bind(wx.EVT_BUTTON, self.f15,id=15)
        win.Bind(wx.EVT_BUTTON, self.f16,id=16)
        win.Show(True)
        
    def f11(self, event):
         
        win11 = wx.MDIChildFrame(self, -1,u"Python语言基础",size=(450,330))
        
        win11.CreateStatusBar() 
        win11.SetStatusText("These are some language basic")   #状态栏
        
        panel = wx.Panel(win11, -1)
        panel.SetBackgroundColour("White")
        
        
        str = u"Python语言基础"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        file11 = open("txt/language basic.txt","r")
        file11txt = file11.read()
    
        wx.StaticText(panel, -1, file11txt, (20,50))


    def f12(self,event):
        win12 = wx.MDIChildFrame(self, -1,u"运算符优先级",size=(400,350))
        
        win12.CreateStatusBar() 
        win12.SetStatusText("to introduce something")   #状态栏
        
        panel = wx.Panel(win12, -1)
        panel.SetBackgroundColour("White")
        
        str = u"运算符优先级"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        file12 = open("txt/yunsuan.txt","r")
        file12txt = file12.read()
    
        wx.StaticText(panel, -1, file12txt, (20,50))

    
    def f13(self,event):
        
        win13 = wx.MDIChildFrame(self, -1,u"基本语句与输入输出",size=(400,370))
        
        win13.CreateStatusBar() 
        win13.SetStatusText("to introduce something")   #状态栏
        
        panel = wx.Panel(win13, -1)
        panel.SetBackgroundColour("White")
        
        str = u"基本语句与输入输出"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        file12 = open("txt/basic io.txt","r")
        file12txt = file12.read()
    
        wx.StaticText(panel, -1, file12txt, (20,50))


    
    def f14(self,event):
        win14 = wx.MDIChildFrame(self, -1,u"流程控制",size=(400,370))
        
        win14.CreateStatusBar() 
        win14.SetStatusText("to introduce programing")   #状态栏
        
        panel = wx.Panel(win14, -1)
        panel.SetBackgroundColour("White")
        
        str = u"流程控制"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        file12 = open("txt/f14.txt","r")
        file12txt = file12.read()
    
        wx.StaticText(panel, -1, file12txt, (20,50))
       
    
    def f15(self,event):
        win15 = wx.MDIChildFrame(self, -1,u"函数",size=(350,430))
        
        win15.CreateStatusBar() 
        win15.SetStatusText("to introduce function")   #状态栏
        
        panel = wx.Panel(win15, -1)
        panel.SetBackgroundColour("White")
        
        str = u"函数"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        file12 = open("txt/f15.txt","r")
        file12txt = file12.read()
    
        wx.StaticText(panel, -1, file12txt, (20,50))
       
    
    def f16(self,event):
        win16 = wx.MDIChildFrame(self, -1,u"列表",size=(380,350))
        
        win16.CreateStatusBar() 
        win16.SetStatusText("to introduce function")   #状态栏
        
        panel = wx.Panel(win16, -1)
        panel.SetBackgroundColour("White")
        
        str = u"列表"
        text = wx.StaticText(panel, -1, str, (10, 10))
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL,wx.ALIGN_CENTER)
        text.SetFont(font)
        
        file16 = open("txt/list.txt","r")
        file16txt = file16.read()
    
        wx.StaticText(panel, -1, file16txt, (20,50))
    
    
    def bind(self, event):
        wildcard = "Python source (*.py)|*.py|" \
            "Compiled Python (*.pyc)|*.pyc|" \
            "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), 
            "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            #print dialog.GetPath() 
            
        
            r= subprocess.Popen(dialog.GetPath(), shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            mass = r.stdout.read()
            #print type(mass)
            if mass=='':
                print u"正常运行"
            else:
                #print mass
                f = open("txt/er.txt","w")
                f.write(mass);
                f.close();
                line = mass.find("line")+5
                for i in range(6):
                    if (mass[line+i].isdigit()):
                        continue
                    else:

                        break
                #print i
                #print line
                er = mass[line:line+i]
                print u"在"+er+u"行发生了如下错误：",
                if "NameError" in mass:
                    print u"NameError:尝试访问一个没有申明的变量\n"
                elif "ZeroDivisionError" in mass:
                        
                    print u"ZeroDivisionError 除数为0\n"
                elif "SyntaxError" in mass:
                    print u"SyntaxError 语法错误\n"
                elif "IndexError" in mass:
                    print u"IndexError 索引超出序列范围\n"
                elif "IOError" in mass:
                    print u"IOError 输入输出错误（比如你要读的文件不存在）\n"
                elif "AttributeError" in mass:
                    print  u"AttributeError 尝试访问未知的对象属性 \n"
                elif "ValueError" in mass:
                    print u"ValueError 传给函数的参数类型不正确，比如给int()函数传入字符串形 \n"
                elif "IndentationError" in mass:
                    print u"IndentationError 极有可能是缩进问题\n"
    
        dialog.Destroy()

    def Fi(self,event):
        win4 = create(self)
        win4.CreateStatusBar()
        win4.SetStatusText("Search here!")
        
    
        

class NOTE(wx.grid.Grid):
        def __init__(self, parent):
                wx.grid.Grid.__init__(self, parent, -1,size=(300,200))
                
                panel = wx.Panel(self, -1)
                panel.SetBackgroundColour("black")
                self.SetDefaultRowSize(30, resizeExistingRows=False)

                self.DisableDragRowSize()
                self.CreateGrid(4, 2)
                self.SetColSize(0, 50)
                self.SetColSize(1, 250)
                self.SetColLabelValue(0, "01")
                self.SetColLabelValue(1, "02")
                self.SetRowLabelValue(0, "0a")

                self.SetRowLabelValue(1, "0b")

                self.SetRowLabelValue(2, "0c")

                self.SetRowLabelValue(3, "0d")

                self.SetCellValue(0, 0, "math")
                self.SetCellValue(0, 1, "Dernier")
                
                self.SetCellValue(1, 0, "wx")
                self.SetCellValue(1, 1, "Sandberg")    
                
                self.SetCellValue(2, 0, "os")
                self.SetCellValue(2, 1, "Matthews")
                
                self.SetCellValue(3, 0, "string")
                self.SetCellValue(3, 1, "Durham")         

                    
#为note添加行列碰到一些问题
                    
        def AppendRows(self, numRows=1): 
            return (self.GetRowCount() + numRows)  < 50
                



def create(parent):
    return MDIChildFrame1(parent)

[wxID_MDICHILDFRAME1, wxID_MDICHILDFRAME1BUTTON1, wxID_MDICHILDFRAME1PANEL1, 
 wxID_MDICHILDFRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class MDIChildFrame1(wx.MDIChildFrame):
    a='gam'
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIChildFrame.__init__(self, id=wxID_MDICHILDFRAME1, name='',
              parent=prnt, pos=wx.Point(40, 200), size=wx.Size(449, 116),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Find')
              
        self.SetClientSize(wx.Size(433, 78))
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)
        self.Show(True)
        self.SetToolTipString(u'MDIChildFrame1')

        self.panel1 = wx.Panel(id=wxID_MDICHILDFRAME1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(433, 78),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_MDICHILDFRAME1BUTTON1, label=u'Search',
              name='button1', parent=self.panel1, pos=wx.Point(320, 16),
              size=wx.Size(83, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_MDICHILDFRAME1BUTTON1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_MDICHILDFRAME1TEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(32, 16),
              size=wx.Size(256, 24), style=0, value=u'search for you need!')
        self.textCtrl1.SetEditable(True)
   #     self.textCtrl1.Bind(wx.EVT_TEXT, self.OnTextCtrl1Text,
    #          id=wxID_MDICHILDFRAME1TEXTCTRL1)
   #     self.textCtrl1.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl1TextEnter,
    #          id=wxID_MDICHILDFRAME1TEXTCTRL1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        
        a=self.textCtrl1.GetValue()
        f = open("txt/sou.txt","w")
        f.write(a);
        f.close();
        
        os.startfile("db.exe")
        

            
            
if __name__ == '__main__':
    app = wx.App()

    frame = Frame()
    frame.Show()
    
    provider = wx.CreateFileTipProvider("txt/tips.txt", random.randint(1,13))
    #随机数作为显示初始tip的参数
    
    wx.ShowTip(None, provider, True)

    app.MainLoop()
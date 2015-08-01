#Boa:MDIChild:MDIChildFrame1

import wx
import wx.lib.filebrowsebutton 

def create(parent):
    return Music(parent)

[wxID_MDICHILDFRAME1, wxID_MDICHILDFRAME1BUTTON1, wxID_MDICHILDFRAME1BUTTON2, 
 wxID_MDICHILDFRAME1PANEL1, wxID_MDICHILDFRAME1STATICTEXT1, 
 wxID_MDICHILDFRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Music(wx.MDIChildFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIChildFrame.__init__(self, id=wxID_MDICHILDFRAME1, name='',
              parent=prnt, pos=wx.Point(0, 420), size=wx.Size(615,90),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Music player')



        self.panel1 = wx.Panel(id=wxID_MDICHILDFRAME1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(615, 65),
              style=wx.TAB_TRAVERSAL)
              
        self.fbb = wx.lib.filebrowsebutton.FileBrowseButton(self.panel1,       
                            labelText="Select a WAVE file:", fileMask="*.wav")  
                            

        self.play_button = wx.Button(self.panel1, wx.ID_ANY, ">> Play")     
        self.play_button.Bind(wx.EVT_BUTTON, self.onPlay) 
        
        self.stop_button = wx.Button(self.panel1, wx.ID_ANY, "|| Stop")     
        self.stop_button.Bind(wx.EVT_BUTTON, self.Stop)        
        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)     
        hsizer.Add(self.fbb, 1, wx.ALIGN_CENTER_VERTICAL)     
        hsizer.Add(self.play_button, 0, wx.ALIGN_CENTER_VERTICAL)     
        hsizer.Add(self.stop_button, 0, wx.ALIGN_CENTER_VERTICAL)   
        # create a border space    
        border = wx.BoxSizer(wx.VERTICAL)     
        border.Add(hsizer, 0, wx.EXPAND|wx.ALL, 10)     
        self.panel1.SetSizer(border) 
    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def onPlay(self, event):
        filename = self.fbb.GetValue()     
        self.sound = wx.Sound(filename)     
        # error handling ...     
        if self.sound.IsOk():       
            self.sound.Play(wx.SOUND_ASYNC)     
            
        else:       
            wx.MessageBox("Missing or invalid sound file", "Error") 
            
            
    def Stop(self,event):
        filename = self.fbb.GetValue()     
        self.sound = wx.Sound(filename) 
        self.sound.Stop()

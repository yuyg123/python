import wx


def load(event):
    '''加载文件内容'''
    file = open(filename.GetValue(), 'r')
    contents.SetValue(file.read())
    file.close()


def save(event):
    '''保存文件内容'''
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()


app = wx.App()
win = wx.Frame(None, title='我的记事本', size=(410, 335))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='Open')
saveButton = wx.Button(bkg, label='Save')

loadButton.Bind(wx.EVT_BUTTON, load)
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.RIGHT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()

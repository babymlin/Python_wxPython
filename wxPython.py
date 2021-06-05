# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

#0503作業2
#101_AI班林建名

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"關閉程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )

		self.m_menubar.Append( self.m_menu1, u"檔案" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem5 )

		self.m_menubar.Append( self.m_menu2, u"關於" )

		self.SetMenuBar( self.m_menubar )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.m_richText = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer.Add( self.m_richText, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.creat_file, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.open_file, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.save_file, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.Exit, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.about_editor, id = self.m_menuItem5.GetId() )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def creat_file( self, event ):
		event.Skip()

	def open_file( self, event ):
		event.Skip()

	def save_file( self, event ):
		event.Skip()

	def Exit( self, event ):
		event.Skip()

	def about_editor( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog
###########################################################################

class MyDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"關於作者", pos = wx.DefaultPosition, size = wx.Size( 167,99 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"作者：林建名\n班級：101_AI_第7期", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

class execute(MyFrame):
    
    def main():
        app = wx.App()
        execute(None).Show()
        app.MainLoop()
    
    def creat_file( self, event ):
        self.SetLabel("記事本")
        self.m_richText.Clear()

    def open_file( self, event ):
        openFileDialog = wx.FileDialog(self,
                                       message = "請選擇要開啟的檔案",
                                       wildcard = "文字檔案 (*.txt)|*.txt",
                                       style = wx.FD_OPEN|wx.FD_CHANGE_DIR)
        dialog = openFileDialog.ShowModal()
        file_path = openFileDialog.GetPath()
        file_name = openFileDialog.GetFilename()
        if dialog !=  wx.ID_OK:
            return
        self.SetLabel(f"記事本 - {file_name}")
        with open(file_path, 'r', encoding="utf-8") as fp:
            data = fp.read()
            self.m_richText.SetValue(data)
    
    def save_file( self, event ):
        if self.GetLabel() == "記事本":
            saveFileDialog = wx.FileDialog(self,
                                            message = "請選擇要儲存的檔名",
                                            wildcard = "文字檔案 (*.txt)|*.txt",
                                            style = wx.FD_SAVE|wx.FD_CHANGE_DIR)
            dialog = saveFileDialog.ShowModal()
            file_path = saveFileDialog.GetPath()
            file_name = saveFileDialog.GetFilename()
            if dialog !=  wx.ID_OK:
                return
            self.SetLabel(f"記事本 - {file_name}")
            with open(file_path, 'w', encoding="utf-8") as fp:
                fp.write(self.m_richText.GetValue())
        else:
            file_name = str(self.GetLabel()).split("-")[1].replace(" ", "")
            with open(file_name, 'w', encoding="utf-8") as fp:
                fp.write(self.m_richText.GetValue())

    def Exit( self, event ):
        self.Destroy()
    
    def about_editor(self, event):
        app2 = wx.App()
        MyDialog(None).Show()
        app2.MainLoop()

if __name__ == '__main__':
    execute.main()

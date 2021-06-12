# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 431,273 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Kendaraan Kos Ceria", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer4.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer4.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl7, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Belum memiliki akun? Silahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer5.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.login )
		self.m_button8.Bind( wx.EVT_BUTTON, self.regis_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()

	def regis_login( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 503,408 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Kendaraan Kos Ceria", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer2.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nama Pemilik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Nomor Kamar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Plat Nomor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		gSizer2.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Slot Parkir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		gSizer2.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl71, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 3, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"ID" )
		self.m_grid2.SetColLabelValue( 1, u"Pemilik" )
		self.m_grid2.SetColLabelValue( 2, u"No. Kamar" )
		self.m_grid2.SetColLabelValue( 3, u"No. Plat" )
		self.m_grid2.SetColLabelValue( 4, u"Slot" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_grid2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer41.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer41.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( gSizer41, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.tambah )
		self.m_button2.Bind( wx.EVT_BUTTON, self.hapus )
		self.m_button3.Bind( wx.EVT_BUTTON, self.keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambah( self, event ):
		event.Skip()

	def hapus( self, event ):
		event.Skip()

	def keluar( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 438,289 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Registrasi ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer6.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer6.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer6.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		gSizer6.Add( self.m_staticText201, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button7, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.register )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def register( self, event ):
		event.Skip()



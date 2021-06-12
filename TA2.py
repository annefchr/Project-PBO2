import wx
import TA
import sqlite3

class Registrasi(TA.MyFrame4):
	def __init__(self, parent):
		super().__init__(parent)

	def register(self, event):
		nama = self.m_textCtrl9.GetValue()
		username = self.m_textCtrl10.GetValue()
		password = self.m_textCtrl11.GetValue()
		if nama == "" or username == "" or password == "" :
			wx.MessageBox("Semua informasi harus terisi!")
		else :
			conn = sqlite3.connect('baru.db')
			cursor = conn.cursor()
			cursor.execute("INSERT INTO pemilik(nama_pemilik, username,password) VALUES(?,?,?)",(nama,username,password))
			conn.commit()
			conn.close()
			wx.MessageBox("Data telah disimpan.")
			if(wx.OK):
				regis = Login(parent=self)
				regis.Show()

class Login(TA.MyFrame2):
	"""docstring for ClassName"""
	def __init__(self, parent):
		TA.MyFrame2.__init__(self,parent)

	def regis_login(self,event):
		regis_login = Registrasi(parent=self)
		regis_login.Show()

	def login(self,event):
		username = self.m_textCtrl6.GetValue()
		password = self.m_textCtrl7.GetValue()
		conn = sqlite3.connect('baru.db')
		cursor = conn.cursor()
		cek_akun = ("SELECT * FROM pemilik WHERE username = ? AND password = ?")
		cursor.execute(cek_akun,(username,password))
		results = cursor.fetchall()
		if results :
			for i in results :
				wx.MessageBox("Berhasil Login!")
				login = Kos(parent=self)
				login.Show()


class Kos(TA.MyFrame1):
	"""docstring for ClassName"""
	def __init__(self, parent):
		TA.MyFrame1.__init__(self,parent)

	def tambah( self, event ):
		ID = self.m_textCtrl5.GetValue()
		nama = self.m_textCtrl7.GetValue()
		kamar = self.m_textCtrl9.GetValue()
		plat = self.m_textCtrl10.GetValue()
		slot = self.m_textCtrl71.GetValue()

		if ID == "" or nama == "" or kamar == "" or plat == "" or slot == "" :
			wx.MessageBox("Masukkan data dengan lengkap!", "Warning", wx.OK | wx.ICON_WARNING) 
		elif not (wx.OK):
			self.m_textCtrl5.SetValue("")
			self.m_textCtrl7.SetValue("")
			self.m_textCtrl9.SetValue("")
			self.m_textCtrl10.SetValue("")
			self.m_textCtrl71.SetValue("")
		else:
			conn = sqlite3.connect('baru.db') 
			cursor = conn.cursor()
			data = cursor.execute("INSERT INTO kendaraan (id_kendaraan, nama, kamar, plat, slot) VALUES (?,?,?,?,?)", (ID, nama, kamar, plat, slot))
			data = cursor.execute("SELECT * FROM kendaraan").fetchall()
			conn.commit()
			conn.close()
			for baris in range(len(data)):
				self.m_grid2.AppendRows()
				for kolom in range (len(data[baris])):
					self.m_grid2.SetCellValue(baris, kolom, str(data[baris][kolom]))
			print("Data berhasil disimpan!")
			wx.MessageBox ("Data berhasil disimpan!", "Informasi", wx.OK | wx.ICON_INFORMATION)

	def hapus( self, event ):
		ID = self.m_textCtrl5.GetValue()
		if (wx.OK):
			self.m_textCtrl5.SetValue("")

			conn = sqlite3.connect('baru.db')
			cursor = conn.cursor()
			data = "DELETE from kendaraan where id_kendaraan=?"
			isian = (ID)
			cursor.execute(data, isian)
			conn.commit()
			conn.close()

			conn = sqlite3.connect('baru.db')
			cursor = conn.cursor()
			data = cursor.execute("SELECT * FROM kendaraan").fetchall()
			conn.commit()
			conn.close()
			for baris in range(len(data)):
				self.m_grid2.DeleteRows()
				for kolom in range (len(data[baris])):
					self.m_grid2.SetCellValue(baris, kolom, str(data[baris][kolom]))

			print("Data berhasil dihapus!")
			wx.MessageBox ("Data berhasil dihapus!", "Informasi", wx.OK | wx.ICON_INFORMATION)
		else :
			print("Data gagal dihapus!")
			wx.MessageBox ("Data gagal dihapus!", "Informasi", wx.OK | wx.ICON_INFORMATION)

					
if __name__ == '__main__':
	app = wx.App(False)
	frame = Login(None)
	frame.Show(True)
	app.MainLoop()
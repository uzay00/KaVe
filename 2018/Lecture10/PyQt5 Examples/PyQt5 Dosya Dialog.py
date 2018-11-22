import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__() 
        
        self.label = QLabel("")
        
        self.setCentralWidget(self.label)
        self.setUI()
        
    def setUI(self):
        
        
        self.toolbar = self.addToolBar("Dosyalar")
        self.statusBar()
        #Buton Ayarları, Oluşturma, Görünüm
        ac = QAction(QIcon("info.png"),"open",self)
        ac.setStatusTip("Dosya acmayi saglar.")
        self.toolbar.addAction(ac)
        
        #Butona Tıklayınca Çalışacak Fonksiyon
        ac.triggered.connect(self.uygula)
        
        
        
        
        #Pencere Başlığı ve Pencere İçin ICON Seçimi
        self.show()
        self.setWindowTitle("QFileDialog")
        self.setWindowIcon(QIcon("info.png"))
        
    def uygula(self):
        #Dosya Açma Butonunun İçeriği, Hangi Dosya Tipini Açacağı,İlk olarak nerede konumlanacağı
        fname = QFileDialog.getOpenFileName(self,"Dosya Ac","C:/Users/yemre/Desktop","Image File (*.png)")
        #Açılan Dosyanın Pencereye Yazılması
        self.label.setPixmap(QPixmap(fname[0]))
        
            
        



def window(): #Pencere Ayarları
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    window()
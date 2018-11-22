from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self): #Buton Oluşturma, Boyutunu Ayarlama, Üstündeki Yazıyı Ayarlama, Tıklayınca Olacağı Belirleme
        button = QPushButton(self)
        button.move(60,100)
        button.setText("Tıkla")
        button.clicked.connect(self.baglan)
        
        
        self.show()
        
        
    def baglan(self): #Butona Tıklayınca Olacak Şeylerin Fonksiyonu
        QMessageBox.warning(self,"Uyarı mesajı","Merhaba Merhaba")
        

        



def window(): #Pencereyi oluşturma
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    window()
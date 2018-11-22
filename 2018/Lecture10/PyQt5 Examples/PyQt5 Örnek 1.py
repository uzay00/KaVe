#Kütüphaneleri import ediyoruz.
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


#bir ana fonksiyon oluşturuyoruz. Pencere vb. işler bunun içerisinde işleyecekler.
def pencere():
    app = QApplication(sys.argv) #App'ı tanımlıyoruz.
    window = QWidget() #burada pencereyi tanımlıyoruz. Widget yerine 
    yazi = QLabel(window)
    alan = QLineEdit(window)
    yazi.setText("Merhaba Dünya!")
    yazi.move(50,100)
    alan.move(500,150)
    window.setWindowTitle("Pencere İsmi")
    window.setGeometry(200,200,300,300)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
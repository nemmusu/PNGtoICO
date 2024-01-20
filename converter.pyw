from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image
import os

class PNGtoICO(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.logo = QLabel(self)
        pixmap = QPixmap('img/logo.png')
        self.logo.setPixmap(pixmap)
        layout.addWidget(self.logo)
        self.label_risultato = QLabel()
        layout.addWidget(self.label_risultato)
        btn_converti = QPushButton("Converti da PNG a ICO")
        btn_converti.clicked.connect(self.converti_da_png_a_ico)
        layout.addWidget(btn_converti)
        self.setLayout(layout)
        self.setWindowTitle("Convertitore da PNG a ICO")
        
    def converti_da_png_a_ico(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_png, _ = QFileDialog.getOpenFileName(self, "Seleziona file PNG", "C:\\", "PNG Files (*.png);;All Files (*)", options=options)
        if not file_png:
            return
        try:
            with Image.open(file_png) as img:
                if img.format.lower() != 'png':
                    raise Exception("File non valido. Seleziona un file PNG.")
        except Exception as e:
            QMessageBox.critical(self, "Errore", "File non valido. Seleziona un file PNG.")
            return

        nome_file_png = os.path.basename(file_png)
        nome_file_base, _ = os.path.splitext(nome_file_png)
        file_ico, _ = QFileDialog.getSaveFileName(self, "Seleziona percorso di salvataggio per l'ICO", "C:\\", "ICO Files (*.ico);;All Files (*)", options=options)
        if not file_ico:
            return
        image = Image.open(file_png)
        image.save(file_ico, format="ICO")
        QMessageBox.information(self, "Conversione completata", f"File salvato su {file_ico}")

if __name__ == '__main__':
    app = QApplication([])
    finestra = PNGtoICO()
    finestra.show()
    app.exec_()

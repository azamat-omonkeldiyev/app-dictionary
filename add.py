from PyQt5.QtWidgets import *

class AddWindow(QWidget):
    def __init__(self,obj):
        super().__init__()

        self.setStyleSheet("font-size:20px")
        self.main_window = obj

        self.v_main_lay = QVBoxLayout()
        self.v_edit_lay = QVBoxLayout()
        self.h_edit_btn_lay = QHBoxLayout()

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uzb...")

        self.en_edit = QLineEdit()
        self.en_edit.setPlaceholderText("Eng...")

        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.Ok)

        self.lbl = QLabel()

        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.Menu)

        self.v_edit_lay.addWidget(self.uz_edit)
        self.v_edit_lay.addWidget(self.en_edit)

        self.h_edit_btn_lay.addLayout(self.v_edit_lay)
        self.h_edit_btn_lay.addWidget(self.ok_btn)

        self.v_main_lay.addLayout(self.h_edit_btn_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)
    
    def Menu(self):
        self.hide()
        self.main_window.show()

    def Ok(self):
        f = open("lugat.txt",'a+') 
        uz = self.uz_edit.text()
        en = self.en_edit.text()
        if uz and en:
            f.seek(0)
            if f"{uz}-{en}" not in f.read():
                f.write(f"{uz}-{en}\n")
                self.lbl.setText("Muvaffaqiyatli qo'shildi") 
            else:
                self.lbl.setText("Bunday so'z mavjud")
            self.uz_edit.clear()
            self.en_edit.clear()
            self.uz_edit.setStyleSheet("background:white")
            self.en_edit.setStyleSheet("background:white")
        else:
            self.lbl.setText("Barcha maydonlarni to'ldiring!")
            if not uz:
                self.uz_edit.setStyleSheet("background:red")        
            if not en:
                self.en_edit.setStyleSheet("background:red")

        f.close()
from PyQt5.QtWidgets import *


class SearchWindow(QWidget):
    def __init__(self,obj):
        super().__init__()
        
        self.main_window = obj

        self.setStyleSheet("font-size:20px")
        
        self.v_main_lay = QVBoxLayout()
        self.h_lay = QHBoxLayout()
        self.h2_lay = QHBoxLayout()
        self.h3_lay = QHBoxLayout()
        
        self.rd = QRadioButton("Eng")
        self.rd2 = QRadioButton("Uz")
        
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("....")
        self.btn = QPushButton("SEARCH")
        self.btn.clicked.connect(self.chek_file)
        self.btn2 = QPushButton("Menu")
        self.btn2.clicked.connect(self.manu)
        self.btn3 = QPushButton("Add")
        self.btn3.clicked.connect(self.add)
        self.btn3.hide()
        
        
        self.lbl = QLabel()

        
        self.h_lay.addWidget(self.rd)
        self.h_lay.addWidget(self.rd2)
        
        self.h2_lay.addWidget(self.edit)
        self.h2_lay.addWidget(self.btn)
        
        self.h3_lay.addWidget(self.btn2)
        self.h3_lay.addWidget(self.btn3)
        
        self.v_main_lay.addLayout(self.h_lay)
        self.v_main_lay.addLayout(self.h2_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h3_lay)
        self.setLayout(self.v_main_lay)
        
    def chek_file(self):
        
        with open("lugat.txt",'a+') as f:
        
            f.seek(0)
            word_lst = [i.split("-")[1] for i in f.readlines()]
            
            f.seek(0)
            sozlar_lst = [i.split("-")[0] for i in f.readlines()]
                        
            if self.rd.isChecked():
                if self.edit.text() + '\n' in word_lst:
                    self.lbl.clear()
                    self.lbl.setText(f"{sozlar_lst[word_lst.index(self.edit.text() + '\n')]}")
                    self.btn3.hide()
                elif not self.edit.text():
                    self.lbl.clear()
                    self.lbl.setText("Lug'at so'zni kiriting")
                else:
                    self.lbl.clear()
                    self.lbl.setText("Bunday so'z yo'q")
                    self.btn3.show()
                
            elif self.rd2.isChecked():
                if self.edit.text() in sozlar_lst:
                    self.lbl.clear()
                    self.lbl.setText(f"{word_lst[sozlar_lst.index(self.edit.text())]}")
                    self.btn3.hide()
                elif not self.edit.text():
                    self.lbl.clear()
                    self.lbl.setText("Lug'at so'zni kiriting")
                else:
                    self.lbl.clear()
                    self.lbl.setText("Bunday so'z yo'q")
                    self.btn3.show()
                
            else:
                self.lbl.clear()
                self.lbl.setText("Tilni Tanlang!")
    def add(self):
        self.hide()
        self.main_window.Add()
        
    def manu(self):
        self.main_window.show()
        self.hide()
            
            
        
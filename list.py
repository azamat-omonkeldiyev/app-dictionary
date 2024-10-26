from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout,QHBoxLayout,QPushButton

class ListWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        
        self.main_window = obj
        self.v_lay = QVBoxLayout()
        self.h_lay = QHBoxLayout()
        self.list = QListWidget()
        self.list2 = QListWidget()
        self.btn_manu = QPushButton("Menu")
        self.btn_manu.clicked.connect(self.menu)
        
        self.setStyleSheet("font-size:20px")

        with open("lugat.txt", "a+", encoding="utf-8") as f:
            f.seek(0)
            items = f.read().split()
            
            self.list.addItem("O'ZBEKCHA")
            self.list.addItem(f"{"-"*20}")
            self.list2.addItem("INGLIZCHA")
            self.list2.addItem(f"{"-"*20}")
            for i in items:
                self.list.addItem(i.split('-')[0])
                self.list2.addItem(i.split('-')[1])   
        
        self.h_lay.addWidget(self.list)
        self.h_lay.addWidget(self.list2)
        self.v_lay.addLayout(self.h_lay)
        self.v_lay.addWidget(self.btn_manu)
        
        self.setLayout(self.v_lay)
        
    def menu(self):
        self.main_window.show()
        self.hide()
        

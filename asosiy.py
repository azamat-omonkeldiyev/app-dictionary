from PyQt5.QtWidgets import *

from add import AddWindow

from search import SearchWindow

from list import ListWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size: 20px")

        self.h_main_lay = QHBoxLayout()
        self.v_btn_lay = QVBoxLayout()

        self.add_btn = QPushButton("ADD")
        self.add_btn.clicked.connect(self.Add)

        self.search_btn = QPushButton("SEARCH")
        self.search_btn.clicked.connect(self.Search)

        self.list_btn = QPushButton("LIST")
        self.list_btn.clicked.connect(self.List)

        self.exit_btn = QPushButton("EXIT")
        self.exit_btn.clicked.connect(exit)

        self.v_btn_lay.addWidget(self.add_btn)
        self.v_btn_lay.addWidget(self.search_btn)
        self.v_btn_lay.addWidget(self.list_btn)
        self.v_btn_lay.addWidget(self.exit_btn)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_btn_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)

    def Search(self):
        self.hide()
        self.search_Window = SearchWindow(self)
        self.search_Window.show()

    def Add(self):
        self.hide()
        self.add_window = AddWindow(self)
        self.add_window.show()

    def List(self):
        self.hide()
        self.list_window = ListWindow(self)
        self.list_window.show()
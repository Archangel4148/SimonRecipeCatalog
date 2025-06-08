#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
"""
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QDesktopWidget, QWidget, QLabel, \
    QHBoxLayout, QVBoxLayout, QSizePolicy


class Example(QWidget):

    def __init__(self, data, nrows):
        super().__init__()
        self.nrows = nrows
        self.data = data
        self.initUI()

    def getRandomRecipe(self):
        randNum = random.randint(0, self.nrows)
        data = self.data
        # data["ingredients"] = data["ingredients"].apply(lambda x: '\n'.join(x) if isinstance(x, list) else str(x))

        self.label.setText(f"""
            <div>
            <b>{data["title"][randNum]}</b><br><br>
            <b>Ingredients: </b> \n {data["ingredients"][randNum]}<br><br>
            <b>Directions:</b> \n {data["directions"][randNum]}<br><br>
            <b>Link to Recipe: </b> {data["link"][randNum]}<br><br>
            <b>Tags: </b>{data["NER"][randNum]}<br><br>
            <b>Home Website: </b>{data["site"][randNum]}<br><br>
        </div> """)

    def initUI(self):
        # Layout:
        hbox = QHBoxLayout()

        self.label = QLabel("Recipe Time :D", self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.move(400, 400)

        # Generate Button
        gbtn = QPushButton('Get a Random Recipe!', self)
        gbtn.clicked.connect(self.getRandomRecipe)

        gbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # gbtn.resize(1500, 150)
        # gbtn.move(100, 100)
        hbox.addWidget(gbtn)

        # Quit Button:
        qbtn = QPushButton('Quit', self)

        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # qbtn.resize(150,150)
        # qbtn.move(50, 50)
        hbox.addWidget(qbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label)

        vbox.addStretch(1)

        vbox.addLayout(hbox)

        # Menu

        # Menu Items:
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('File')
        #
        # impMenu = QMenu('Test 1', self)
        #
        # #Qactions
        #
        # impAct=QAction('Test 2', self)
        #
        # #Add Action
        #
        # impMenu.addAction(impAct)
        #
        # newAct = QAction('New', self)
        #
        # fileMenu.addAction(newAct)
        # fileMenu.addMenu(impMenu)

        # # Status Bar
        # statusbar = self.statusBar()
        # statusbar.showMessage('Ready')

        # Location and Size of window
        # self.setGeometry(300, 300, 300, 220)

        self.setLayout(vbox)

        # Maximize Screen
        self.showMaximized()
        self.setWindowTitle('Santy\'s Recipe Catalog')
        self.setWindowIcon(QIcon('chicken.JPG'))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topleft())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

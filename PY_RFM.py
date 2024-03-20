from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys

class PyRFM_LocalGui(QApplication):
    def __init__(self):
        super(PyRFM_LocalGui,self).__init__(sys.argv+['-platform','windows:darkmode=1']);
        self.win = QMainWindow();
        winGeometry=[
            round(self.primaryScreen().size().width()/1.5),
            round(self.primaryScreen().size().height()/1.5)];
        print(winGeometry)
        self.win.setGeometry(0,0,winGeometry[0],winGeometry[1]);
        self.win.setWindowTitle("PyRFM")
        self.win.setWindowIcon(QIcon('./assets/favicon.ico'))
        # self.win.setWindowFlag(Qt.FramelessWindowHint) # maybe?
        self.win.show();
        self.center();
        self.exec_();
    
    def center(self):
        frameGm = self.win.frameGeometry();
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos());
        centerPoint = QApplication.desktop().screenGeometry(screen).center();
        frameGm.moveCenter(centerPoint);
        self.win.move(frameGm.topLeft());
    
myApp = PyRFM_LocalGui();

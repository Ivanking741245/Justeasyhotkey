from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtCore import QPoint, Qt
from checkrule import pynput_keyboard_checkrule
from all import *
import subprocess
import configparser
import sys
import os
import qdarkstyle
import traceback
WIDTH = 1200
HEIGHT = 800
PATH = os.path.dirname(os.path.abspath(__file__))
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JusteasyHotkey")
        self.resize(WIDTH, HEIGHT)

        center = QGuiApplication.primaryScreen().availableGeometry().center()
        self.move(center - QPoint(self.width()//2, self.height()//2))

        self.setFixedSize(WIDTH, HEIGHT)

        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyqt6"))
        self.setupComponents()
    def setupComponents(self):
        self.combox_x = 0
        self.combox_y = 0
        self.combox_height = 30
        self.combox_width = 100
        '''
        self.make_button = QtWidgets.QPushButton(self)
        self.make_button.setText("+")
        self.make_button.setGeometry(0, 0, 60, 60)
        self.make_button.setStyleSheet("border-radius: 20; font-size:40px;")
        self.make_button.clicked.connect(self.click_make)
        '''
        self.firreadconfig = configparser.ConfigParser()
        self.firreadconfig.read(os.path.join(PATH, "setting.ini"), encoding="utf-8")
        self.firsaveset = self.firreadconfig["database"]["save"]

        self.make_combobox1 = QtWidgets.QComboBox(self)
        self.make_combobox1.addItems(key)
        self.make_combobox1.setGeometry(self.combox_x, self.combox_y, self.combox_width, self.combox_height)
        #self.make_combobox1.currentIndexChanged.connect(self.join_action)
        
        self.make_combobox_label = QtWidgets.QLabel(self)
        self.make_combobox_label.setText("+")
        self.make_combobox_label.setGeometry(self.combox_x + 110, self.combox_y - 5, 20, 40)

        self.make_combobox2 = QtWidgets.QComboBox(self)
        self.make_combobox2.setGeometry(self.combox_x + 140, self.combox_y, self.combox_width, self.combox_height)
        self.make_combobox2.addItems(key)
        #self.make_combobox2.currentIndexChanged.connect(self.join_action)

        self.setAction = QtWidgets.QLabel(self)
        self.setAction.setText(" 連接至 =>")
        self.setAction.setGeometry(self.combox_x + 250, self.combox_y - 5, 100, 40)

        self.actionbox = QtWidgets.QComboBox(self)
        self.actionbox.setGeometry(self.combox_x + 330, self.combox_y, self.combox_width + 15, self.combox_height)
        self.actionbox.addItems(action)
        self.actionbox.currentIndexChanged.connect(self.show_action)
        self.actionbox.setCurrentIndex(-1)

        self.join = QtWidgets.QPushButton(self)
        self.inputbox = QtWidgets.QLineEdit(self)
        
        self.list_wid = QtWidgets.QListWidget(self)
        self.list_wid.setGeometry(self.combox_x, self.combox_y + 50, self.combox_width + 500, self.combox_height + 500)

        self.listen_but = QtWidgets.QPushButton(self)
        self.listen_but.setGeometry(self.combox_x, self.combox_y + 620, 100, 50)
        self.listen_but.clicked.connect(self.listenevent)
        self.listen_but.setText("開啟監聽")

        self.save = QtWidgets.QCheckBox(self)
        self.save.setGeometry(self.combox_x + 110, self.combox_y + 620, 100, 50)
        self.save.clicked.connect(self.inisetting)
        self.save.setText("儲存熱鍵設定")
        self.save.setChecked(int(self.firsaveset))

        self.join.hide()
        self.inputbox.hide()
        self.listen_but.show()
        self.list_wid.show()
        self.make_combobox1.show()
        self.make_combobox_label.show()
        self.make_combobox2.show()
        self.setAction.show()
        self.actionbox.show()
        self.addlast_action()
    def addlast_action(self):
        if self.save.isChecked():
            with open(os.path.join(PATH, "hotkeylist.txt")) as f:
                hotkeytxt = f.readlines()
                hotkeyl = []
                hotkeyl.extend(hotkeytxt)
                hotkeyl = [i.strip() for i in hotkeyl]
            with open(os.path.join(PATH, "activity.txt")) as f:
                acttxt = f.readlines()
                actl = []
                actl.extend(acttxt)
                actl = [i.strip() for i in actl]
            for i in range(len(hotkeyl)):
                self.list_wid.addItem(f"{hotkeyl[i]} -> {actl[i]} :(上次所建立的熱鍵)")
    def show_action(self):
        def show_join(x):
            try:
                self.join.clicked.disconnect()
            except: pass
            self.join.setText("加入")
            self.join.setGeometry(self.combox_x + x, self.combox_y - 5, 70, 40)
            self.join.clicked.connect(self.join_action)
            self.join.show()
        if not self.actionbox.currentText() == '':
                activ = action.index(self.actionbox.currentText())
                if activ == 0:
                    self.action_combobox1 = QtWidgets.QComboBox(self)
                    self.action_combobox1.addItems(key)
                    self.action_combobox1.setGeometry(self.combox_x + 470, self.combox_y, self.combox_width, self.combox_height)
                    #self.action_combobox1.currentIndexChanged.connect(self.join_action)

                    self.action_combobox_label = QtWidgets.QLabel(self)
                    self.action_combobox_label.setText("+")
                    self.action_combobox_label.setGeometry(self.combox_x + 580, self.combox_y - 5, 20, 40)

                    self.action_combobox2 = QtWidgets.QComboBox(self)
                    self.action_combobox2.setGeometry(self.combox_x + 610, self.combox_y, self.combox_width, self.combox_height)
                    self.action_combobox2.addItems(key)
                    #self.action_combobox2.currentIndexChanged.connect(self.join_action)

                    self.action_combobox1.show()
                    self.action_combobox_label.show()
                    self.action_combobox2.show()
                    show_join(x=730)
                elif activ in (1, 2, 3, 5):
                    try:
                        self.action_combobox1.hide()
                        self.action_combobox_label.hide()
                        self.action_combobox2.hide()
                        self.join.hide()
                    except:
                        print("cant hide.")
                        pass
                    #self.inputbox.setText("輸入cmd命令")
                    #self.inputbox.textChanged.connect(self.join_action)
                    self.inputbox.setGeometry(self.combox_x + 470, self.combox_y, self.combox_width, self.combox_height)
                    if activ == 1:
                        self.inputbox.setPlaceholderText("輸入cmd命令") #提示而非文字
                    elif activ == 2:
                        self.inputbox.setPlaceholderText("輸入點擊次數")
                    elif activ == 3:
                        self.inputbox.setPlaceholderText("輸入點擊時間(s)")
                    elif activ == 5:
                        self.inputbox.setPlaceholderText("輸入文字")
                    self.inputbox.show()
                    show_join(x=590)
                elif activ == 4: #####非####
                    self.click_x = QtWidgets.QLineEdit(self)
                    self.click_y = QtWidgets.QLineEdit(self)
                    self.click_x.setGeometry(self.combox_x + 470, self.combox_y, self.combox_width, self.combox_height)
                    self.click_y.setGeometry(self.combox_x + 600, self.combox_y, self.combox_width, self.combox_height)
                    self.click_x.setPlaceholderText("輸入x座標")
                    self.click_y.setPlaceholderText("輸入y座標")
                    self.click_x.show()
                    self.click_y.show()
                    show_join(x=720)
    def join_action(self):
        def writehotkey():
            global hotkey
            with open(os.path.join(PATH, "hotkeylist.txt"), "a") as f:
                firhotkey = self.make_combobox1.currentText()
                sechotkey = self.make_combobox2.currentText()
                try:
                    f.write(f"{firhotkey}+{sechotkey}\n")
                    hotkey = f"{firhotkey}+{sechotkey}"
                except EOFError: pass
        def writeactiv():
            #if
            global activ, war
            war = 0
            cmtype = {1: "cmd", 2: "mouse", 3: "mouse", 4: "mouse", 5:"print"}
            mousetype = {2: "cl", 3: "cl_sp", 4: "mv"}
            with open(os.path.join(PATH, "activity.txt"), "a") as f:
                doactiv = action.index(self.actionbox.currentText())
                print(doactiv)
                if doactiv == 0:
                    #try:
                    dokey1 = self.action_combobox1.currentText()
                    dokey2 = self.action_combobox2.currentText()
                    print(f"{dokey1}, {dokey2}")
                    f.write(f"{dokey1}+{dokey2}\n")
                    activ = f"{dokey1}+{dokey2}"
                    #except EOFError: pass
                elif doactiv in(1, 2, 3, 5):
                    if self.inputbox.text():
                        f.write(f"CMCM+{cmtype[doactiv]}+")
                        if list(cmtype.values()).index(cmtype[doactiv]) == 1:
                            f.write(f"{mousetype[doactiv]}+{self.inputbox.text()}\n")
                            activ = f"{mousetype[doactiv]}+{self.inputbox.text()}"
                        else:
                            f.write(f"{self.inputbox.text()}\n")
                            activ = f"{self.inputbox.text()}"
                    else:
                        warmsg = QtWidgets.QMessageBox()
                        warmsg.warning(self, "警告", "未輸入內容")
                        war = 1
                elif doactiv == 4:
                    try:
                        int(self.click_x.text())
                        int(self.click_y.text())
                        f.write(f"CMCM+{cmtype[doactiv]}+mv+{self.click_x.text()},{self.click_y.text()}")
                        self.list_wid.addItem(f"CMCM+{cmtype[doactiv]}+mv+{self.click_x.text()},{self.click_y.text()}")
                        activ = f"CMCM+{cmtype[doactiv]}+mv+{self.click_x.text()},{self.click_y.text()}"
                    except:
                        war1msg = QtWidgets.QMessageBox()
                        war1msg.warning(self, "警告", "未輸入內容或輸入非數字")
        writehotkey()
        writeactiv()
        if not war: self.list_wid.addItem(f"{hotkey} -> {activ}: {self.actionbox.currentText()}")
        print(f"text:{self.actionbox.currentText()}\n index:{self.actionbox.currentIndex()}")
    def listenevent(self):
        warnnsg = QtWidgets.QMessageBox()
        warnnsg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        warnnsg.setWindowTitle("警告")
        warnnsg.setText("啟用監聽後將無法使用增加熱鍵等功能!確定啟用嗎?")
        warnnsg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        if warnnsg.exec() == QtWidgets.QMessageBox.StandardButton.Ok:
            lispath = os.path.join(PATH, "listenkeyboard.py")
            try: 
                pynput_keyboard_checkrule()
                subprocess.Popen(["python", lispath], check=True)
            except: 
                warnnsg.setText({traceback.print_exc()})
                app.quit()
            self.join.setDisabled(True)
            self.listen_but.setDisabled(True)
    def inisetting(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(PATH, "setting.ini"), encoding="utf-8")
        save = int(config["database"]["save"])
        if self.save.isChecked():
            if save:
                pass
            else:
                with open(os.path.join(PATH, "setting.ini"), "w") as f:
                    config["database"] = {"save": "1"}
                    config.write(f)
        else:
            if save:
                with open(os.path.join(PATH, "setting.ini"), "w") as f:
                    config["database"] = {"save": "0"}
                    config.write(f)
            else:
                pass
    def closeEvent(self, event):
        super().closeEvent(event)
        if not self.save.isChecked():
            with open(os.path.join(PATH, "hotkeylist.txt"), "w") as f:
                pass
            with open(os.path.join(PATH, "activity.txt"), "w") as f:
                pass
        return sys.exit(0)
app = QApplication([*sys.argv, "--ignore-gpu-blocklist"]) #主app及系統
#create all your widgets.........
window = Mainwindow()
window.show()
sys.exit(app.exec())
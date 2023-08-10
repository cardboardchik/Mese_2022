
from PyQt6 import QtCore, QtGui, QtWidgets

from functools import partial
import sqlite3 as sq
from ast import literal_eval

from U2P_main import Ui_u2p



class Ui_Dialog_saved_games(object):
    def setupUi(self, Dialog_saved_games):
        self.Dialog_saved_games = Dialog_saved_games
        Dialog_saved_games.setObjectName("Dialog_saved_games")
        Dialog_saved_games.resize(650, 700)
        Dialog_saved_games.setMinimumSize(QtCore.QSize(650, 700))
        Dialog_saved_games.setMaximumSize(QtCore.QSize(650, 700))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog_saved_games.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../../../../../Pictures/Лого_u2p/vector (svg)/icon_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_saved_games.setWindowIcon(icon)
        Dialog_saved_games.setStyleSheet("background:#fff;")
        Dialog_saved_games.setSizeGripEnabled(False)
        Dialog_saved_games.setModal(False)
        self.frame_saved_games = QtWidgets.QFrame(Dialog_saved_games)
        self.frame_saved_games.setGeometry(QtCore.QRect(16, 60, 618, 558))
        self.frame_saved_games.setStyleSheet("border-radius: 20px;\n"
"background:#DCDCDC;")
        self.frame_saved_games.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_saved_games.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_saved_games.setObjectName("frame_saved_games")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_saved_games)
        self.tableWidget.setGeometry(QtCore.QRect(16, 16, 585, 526)) #if count games > 25 then its = 593
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableView {\n"
"    font: 81 16pt \"Montserrat ExtraBold\";\n"
"    selection-background-color: rgba(255, 255, 255, 0);\n"
"    color:#000;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color:#000;\n"
"border: 1px solid #000;\n"
"font: 81 16pt \"Montserrat ExtraBold\";\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item {\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar:vertical {\n"
"     background:  rgba(0, 0, 0, 0);\n"
"     border-top-right-radius: 4px;\n"
"     border-bottom-right-radius: 4px;\n"
"     width: 12px;\n"
"     margin: 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:vertical {\n"
"    background-color: black;\n"
"     border-radius: 4px;\n"
"     min-height: 20px;\n"
"     margin: 0px 2px 0px 2px;\n"
" }\n"
"")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setIconSize(QtCore.QSize(20, 22))
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        
        # connect to db
        with sq.connect("db.sqlite3") as con_db:
                cur_db = con_db.cursor()
                cur_db.execute("select rowid, * from games")
                
                self.result = cur_db.fetchall()
                result_len = len(self.result)
                
                
                self.tableWidget.setRowCount(result_len)

                for row in range(result_len):
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.result[row][1])) #name
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(self.result[row][2])) #date
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(len(literal_eval(self.result[row][3]))))) #len(periods)
                    
                    pb_delete = QtWidgets.QPushButton()
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(QtGui.QPixmap("UI\\../Images/delete_button.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    pb_delete.setIcon(icon1)
                    pb_delete.setIconSize(QtCore.QSize(23, 23))
                    pb_delete.clicked.connect(partial(self.delete_button, n=row))
                    self.tableWidget.setCellWidget(row, 3, pb_delete)
                    
                    pb_start = QtWidgets.QPushButton()
                    icon2 = QtGui.QIcon()
                    icon2.addPixmap(QtGui.QPixmap("UI\\../Images/play_button.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    pb_start.setIcon(icon2)
                    pb_start.setIconSize(QtCore.QSize(23, 23))
                    pb_start.clicked.connect(partial(self.start_button, n=row))
                    self.tableWidget.setCellWidget(row, 4, pb_start)
                    
                    
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        # item.setForeground(brush)
        
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        
        
        
        
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 2, item)
        
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        # self.tableWidget.setItem(0, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        # self.tableWidget.setItem(0, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        
        
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        # self.tableWidget.setItem(1, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # item.setIcon(icon)
        # self.tableWidget.setItem(1, 4, item)
        
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.label_chose_one_saved_game = QtWidgets.QLabel(Dialog_saved_games)
        self.label_chose_one_saved_game.setGeometry(QtCore.QRect(0, 0, 650, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_chose_one_saved_game.setFont(font)
        self.label_chose_one_saved_game.setStyleSheet("color:#000;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_chose_one_saved_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_chose_one_saved_game.setObjectName("label_chose_one_saved_game")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_saved_games)
        self.pushButton_cancel.setGeometry(QtCore.QRect(182, 628, 271, 62))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_cancel.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"letter-spacing: -1px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(239, 0, 9, 1);\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        
        self.tableWidget.setColumnWidth(4, 12)
        header = self.tableWidget.horizontalHeader()
        
        header.setDefaultSectionSize(165)
        
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        
    
        #connections
        self.pushButton_cancel.clicked.connect(Dialog_saved_games.reject)

        self.retranslateUi(Dialog_saved_games)
        QtCore.QMetaObject.connectSlotsByName(Dialog_saved_games)

    def retranslateUi(self, Dialog_saved_games):
        _translate = QtCore.QCoreApplication.translate
        Dialog_saved_games.setWindowTitle(_translate("Dialog_saved_games", "U2P Simulator - Saved Games"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_saved_games", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_saved_games", "Дата сохраненения"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_saved_games", "Период"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_chose_one_saved_game.setText(_translate("Dialog_saved_games", "Выберете сохраненную игру"))
        self.pushButton_cancel.setText(_translate("Dialog_saved_games", "Отмена"))
        
        
    def delete_button(self, n): #n=row
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setText("Вы точно хотите безвозратно удалить эту игру?") #add current name game
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        returnValue = msgBox.exec()
        
        if returnValue == QtWidgets.QMessageBox.StandardButton.Yes:

            with sq.connect("db.sqlite3") as con_db:
                cur_db = con_db.cursor()
                cur_db.execute(f"DELETE from games where rowid={self.result[n][0]}")
                self.tableWidget.removeRow(n)
        
        
    def start_button(self, n): #n=row
        self.Game_MainWindow = QtWidgets.QMainWindow()
        self.Game_MainWindow_ui = Ui_u2p()
        self.Game_MainWindow_ui.setupUi(self.Game_MainWindow)
        self.Dialog_saved_games.hide()
        self.Game_MainWindow.show()
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_saved_games = QtWidgets.QDialog()
    ui = Ui_Dialog_saved_games()
    ui.setupUi(Dialog_saved_games)
    Dialog_saved_games.show()
    sys.exit(app.exec())

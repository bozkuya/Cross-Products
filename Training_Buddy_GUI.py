# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Training_Buddy_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import op_modes


class TabBar(QtWidgets.QTabBar):
    def __init__(self, parent):
        super().__init__(parent)
        self._editor = QtWidgets.QLineEdit(self)
        self._editor.setWindowFlags(QtCore.Qt.Popup)
        self._editor.setFocusProxy(self)
        self._editor.editingFinished.connect(self.handleEditingFinished)
        self._editor.installEventFilter(self)

    def eventFilter(self, widget, event):
        if ((event.type() == QtCore.QEvent.MouseButtonPress and
             not self._editor.geometry().contains(event.globalPos())) or
            (event.type() == QtCore.QEvent.KeyPress and
             event.key() == QtCore.Qt.Key_Escape)):
            self._editor.hide()
            return True
        return super().eventFilter(widget, event)

    def mouseDoubleClickEvent(self, event):
        index = self.tabAt(event.pos())

        rect = self.tabRect(index)
        self._editor.setFixedSize(rect.size())
        self._editor.move(self.parent().mapToGlobal(rect.topLeft()))
        self._editor.setText(self.tabText(index))
        if not self._editor.isVisible():
            self._editor.show()

    def handleEditingFinished(self):
        index = self.currentIndex()
        if index >= 0:
            self._editor.hide()
            self.setTabText(index, self._editor.text())


class Ui_MainWindow(object):

    mode_tabwidgets = []

    combobox_contents = [op_modes.speed_translate.keys(),
                         op_modes.spin_type_translate.keys(),
                         op_modes.spin_intensity_translate.keys(),
                         op_modes.direction_translate.keys(),
                         op_modes.height_translate.keys(),
                         op_modes.loader_translate.keys()]

    sequence_tables = []
    random_sequence_tables = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1100, 720)
        #MainWindow.setMaximumSize(QtCore.QSize(16777215, 1000))
        MainWindow.setStyleSheet(
        "QMainWindow {\n"
        "    background: #90A0B0;\n"
        "}\n"
        
        "QPushButton {\n"
        "    background: #404040;\n"
        "    border-style: outset;\n"
        "    border-width: 2px;\n"
        "    border-color: gray;\n"
        "    border-radius: 4px;\n"
        "    color: white;\n"
        "   font-size: 16px;\n" 
        "}\n"
        
        "QPushButton:hover {\n"
        "    background: #606060;\n"
        "    border-style: outset;\n"
        "    border-width: 4px;\n"
        "    border-color: #7090B0;\n"
        "    border-radius: 4px;\n"
        "    color: white;\n"
        "   font-size: 18px;\n" 
        "}\n"
        
        "QPushButton:pressed {\n"
        "    background: #80A0C0;\n"
        "    border-style: outset;\n"
        "    border-width: 4px;\n"
        "    border-color: #404070;\n"
        "    border-radius: 4px;\n"
        "    color: white;\n"
        "}\n"
        
        "QComboBox {\n"
        "   font-size: 18px;\n" 
        "}\n"
        
        "QLabel {\n"
        "    font-weight: bold;\n"
        "   font-size: 16px;\n" 
        "}\n"
        
        "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.overall_layout = QtWidgets.QVBoxLayout()
        self.overall_layout.setObjectName("overall_layout")

        self.mode_buttons_layout = QtWidgets.QHBoxLayout()
        self.mode_buttons_layout.setObjectName("mode_buttons_layout")

        self.button_repetition = QtWidgets.QPushButton(self.centralwidget)
        self.button_repetition.setObjectName("button_repetition")
        self.mode_buttons_layout.addWidget(self.button_repetition)
        self.button_repetition.setFixedHeight(50)

        self.button_random_repetition = QtWidgets.QPushButton(self.centralwidget)
        self.button_random_repetition.setObjectName("button_random_repetition")
        self.mode_buttons_layout.addWidget(self.button_random_repetition)
        self.button_random_repetition.setFixedHeight(50)

        self.button_sequence = QtWidgets.QPushButton(self.centralwidget)
        self.button_sequence.setObjectName("button_sequence")
        self.mode_buttons_layout.addWidget(self.button_sequence)
        self.button_sequence.setFixedHeight(50)

        self.button_random_sequence = QtWidgets.QPushButton(self.centralwidget)
        self.button_random_sequence.setObjectName("button_random_sequence")
        self.mode_buttons_layout.addWidget(self.button_random_sequence)
        self.button_random_sequence.setFixedHeight(50)

        self.button_game = QtWidgets.QPushButton(self.centralwidget)
        self.button_game.setObjectName("button_game")
        self.mode_buttons_layout.addWidget(self.button_game)
        self.button_game.setFixedHeight(50)

        self.overall_layout.addLayout(self.mode_buttons_layout)

# repetition tabs
        self.rep_mode_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.rep_mode_tabs.setObjectName("rep_mode_tabs")
        self.rep_mode_tabs.setTabBar(TabBar(self.rep_mode_tabs))
        self.mode_tabwidgets.append(self.rep_mode_tabs)
        self.rep_mode_tabs.hide()

        self.rep_mode_tabs.setMovable(True)
        self.rep_mode_tabs.setTabsClosable(True)
        self.rep_mode_tabs.tabCloseRequested.connect(lambda index: self.rep_mode_tabs.removeTab(index))
        self.button_repetition.clicked.connect(lambda: self.mode_toggle(0))

        self.add_repetition(0)

# random repetition tabs
        self.random_rep_mode_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.random_rep_mode_tabs.setObjectName("rep_mode_tabs")
        self.random_rep_mode_tabs.setTabBar(TabBar(self.random_rep_mode_tabs))
        self.mode_tabwidgets.append(self.random_rep_mode_tabs)
        self.random_rep_mode_tabs.hide()

        self.random_rep_mode_tabs.setMovable(True)
        self.random_rep_mode_tabs.setTabsClosable(True)
        self.random_rep_mode_tabs.tabCloseRequested.connect(lambda index: self.random_rep_mode_tabs.removeTab(index))
        self.button_random_repetition.clicked.connect(lambda: self.mode_toggle(1))

        self.add_repetition(1)

# sequence tabs
        self.seq_mode_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.seq_mode_tabs.setObjectName("random_seq_mode_tabs")
        self.seq_mode_tabs.setTabBar(TabBar(self.seq_mode_tabs))
        self.mode_tabwidgets.append(self.seq_mode_tabs)
        self.seq_mode_tabs.hide()

        self.seq_mode_tabs.setMovable(True)
        self.seq_mode_tabs.setTabsClosable(True)
        self.seq_mode_tabs.tabCloseRequested.connect(lambda index: self.seq_mode_tabs.removeTab(index))
        self.button_sequence.clicked.connect(lambda: self.mode_toggle(2))

        self.add_sequence(2, False)

# random sequence tabs
        self.random_seq_mode_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.random_seq_mode_tabs.setObjectName("random_seq_mode_tabs")
        self.random_seq_mode_tabs.setTabBar(TabBar(self.random_seq_mode_tabs))
        self.mode_tabwidgets.append(self.random_seq_mode_tabs)
        self.random_seq_mode_tabs.hide()

        self.random_seq_mode_tabs.setMovable(True)
        self.random_seq_mode_tabs.setTabsClosable(True)
        self.random_seq_mode_tabs.tabCloseRequested.connect(lambda index: self.random_seq_mode_tabs.removeTab(index))
        self.button_random_sequence.clicked.connect(lambda: self.mode_toggle(3))

        self.add_sequence(3, True)

        self.overall_layout.addWidget(self.rep_mode_tabs)
        self.overall_layout.addWidget(self.random_rep_mode_tabs)
        self.overall_layout.addWidget(self.seq_mode_tabs)
        self.overall_layout.addWidget(self.random_seq_mode_tabs)
        self.gridLayout.addLayout(self.overall_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rep_mode_tabs.setCurrentIndex(0)
        self.seq_mode_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_repetition.setText(_translate("MainWindow", "Repetition"))
        self.button_random_repetition.setText(_translate("MainWindow", "Random Repetition"))
        self.button_sequence.setText(_translate("MainWindow", "Sequence"))
        self.button_random_sequence.setText(_translate("MainWindow", "Random Sequence"))
        self.button_game.setText(_translate("MainWindow", "Game Mode"))



    def mode_toggle(self, mode_index):
        for tab_window in self.mode_tabwidgets:
            if not tab_window.isHidden():
                tab_window.hide()
        self.mode_tabwidgets[mode_index].show()


    def add_throw(self, table):
        new_throw_index = table.currentRow() + 1
        table.insertRow(new_throw_index)

        for col_index in range(6):
            combo = QtWidgets.QComboBox()
            combo.addItems(self.combobox_contents[col_index])
            table.setCellWidget(new_throw_index, col_index, combo)

    def delete_throw(self, table):
        delete_throw_index = table.currentRow()
        table.removeRow(delete_throw_index)

    def add_repetition(self, mode_index):
        _translate = QtCore.QCoreApplication.translate

        self.added_repetition = QtWidgets.QWidget()
        self.added_repetition.setObjectName("added_repetition")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.added_repetition)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.rep_whole_layout = QtWidgets.QVBoxLayout()
        self.rep_whole_layout.setObjectName("rep_hold_layout")

        self.rep_hold_layout = QtWidgets.QHBoxLayout()
        self.rep_hold_layout.setObjectName("rep_hold_layout")

        self.rep_edit_layout = QtWidgets.QVBoxLayout()
        self.rep_edit_layout.setObjectName("rep_edit_layout")

        self.rep_label_op = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_op.setObjectName("rep_label_op")
        self.rep_edit_layout.addWidget(self.rep_label_op)

        self.rep_start = QtWidgets.QPushButton(self.added_repetition)
        self.rep_start.setObjectName("rep_start")
        self.rep_edit_layout.addWidget(self.rep_start)
        self.rep_start.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_stop = QtWidgets.QPushButton(self.added_repetition)
        self.rep_stop.setObjectName("rep_stop")
        self.rep_edit_layout.addWidget(self.rep_stop)
        self.rep_stop.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_new = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_new.setObjectName("rep_label_new")
        self.rep_edit_layout.addWidget(self.rep_label_new)

        self.rep_from_speech = QtWidgets.QPushButton(self.added_repetition)
        self.rep_from_speech.setObjectName("rep_from_speech")
        self.rep_edit_layout.addWidget(self.rep_from_speech)
        self.rep_from_speech.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_from_ui = QtWidgets.QPushButton(self.added_repetition)
        self.rep_from_ui.setObjectName("rep_from_ui")
        self.rep_edit_layout.addWidget(self.rep_from_ui)
        self.rep_from_ui.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.rep_from_ui.clicked.connect(lambda: self.add_repetition(mode_index))

        self.rep_lable_save_delete = QtWidgets.QLabel(self.added_repetition)
        self.rep_lable_save_delete.setObjectName("rep_lable_save_delete")
        self.rep_edit_layout.addWidget(self.rep_lable_save_delete)

        self.rep_load_existing = QtWidgets.QPushButton(self.added_repetition)
        self.rep_load_existing.setObjectName("rep_load_existing")
        self.rep_edit_layout.addWidget(self.rep_load_existing)
        self.rep_load_existing.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_save = QtWidgets.QPushButton(self.added_repetition)
        self.rep_save.setObjectName("rep_save")
        self.rep_edit_layout.addWidget(self.rep_save)
        self.rep_save.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_delete = QtWidgets.QPushButton(self.added_repetition)
        self.rep_delete.setObjectName("rep_delete")
        self.rep_edit_layout.addWidget(self.rep_delete)
        self.rep_delete.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rep_edit_layout.addItem(spacerItem)

        self.rep_hold_layout.addLayout(self.rep_edit_layout)

        self.line = QtWidgets.QFrame(self.added_repetition)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setObjectName("line")
        self.rep_hold_layout.addWidget(self.line)

        self.rep_parameter_layout = QtWidgets.QFormLayout()
        self.rep_parameter_layout.setObjectName("rep_parameter_layout")

        self.rep_label_ball_speed = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_ball_speed.setObjectName("rep_label_ball_speed")
        self.rep_parameter_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rep_label_ball_speed)

        self.combo_ball_speed = QtWidgets.QComboBox(self.added_repetition)
        self.combo_ball_speed.setObjectName("combo_ball_speed")
        self.combo_ball_speed.addItems(self.combobox_contents[0])
        self.rep_parameter_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_ball_speed)
        self.combo_ball_speed.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_spin_type = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_spin_type.setObjectName("rep_label_spin_type")
        self.rep_parameter_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rep_label_spin_type)

        self.combo_spin_type = QtWidgets.QComboBox(self.added_repetition)
        self.combo_spin_type.setObjectName("combo_spin_type")
        self.combo_spin_type.addItems(self.combobox_contents[1])
        self.rep_parameter_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_spin_type)
        self.combo_spin_type.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_spin_intensity = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_spin_intensity.setObjectName("rep_label_spin_intensity")
        self.rep_parameter_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rep_label_spin_intensity)

        self.combo_spin_intensity = QtWidgets.QComboBox(self.added_repetition)
        self.combo_spin_intensity.setObjectName("combo_spin_intensity")
        self.combo_spin_intensity.addItems(self.combobox_contents[2])
        self.rep_parameter_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.combo_spin_intensity)
        self.combo_spin_intensity.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_ball_direction = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_ball_direction.setObjectName("rep_label_ball_direction")
        self.rep_parameter_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rep_label_ball_direction)

        self.combo_direction = QtWidgets.QComboBox(self.added_repetition)
        self.combo_direction.setObjectName("combo_direction")
        self.combo_direction.addItems(self.combobox_contents[3])
        self.rep_parameter_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.combo_direction)
        self.combo_direction.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_ball_height = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_ball_height.setObjectName("rep_label_ball_height")
        self.rep_parameter_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.rep_label_ball_height)

        self.combo_height = QtWidgets.QComboBox(self.added_repetition)
        self.combo_height.setObjectName("combo_height")
        self.combo_height.addItems(self.combobox_contents[4])
        self.rep_parameter_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_height)
        self.combo_height.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_loader_speed = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_loader_speed.setObjectName("rep_label_loader_speed")
        self.rep_parameter_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.rep_label_loader_speed)

        self.combo_loader_speed = QtWidgets.QComboBox(self.added_repetition)
        self.combo_loader_speed.setObjectName("combo_loader_speed")
        self.combo_loader_speed.addItems(self.combobox_contents[5])
        self.rep_parameter_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.combo_loader_speed)
        self.combo_loader_speed.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_label_count = QtWidgets.QLabel(self.added_repetition)
        self.rep_label_count.setObjectName("rep_label_count")
        self.rep_parameter_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.rep_label_count)

        self.count_select = QtWidgets.QSpinBox(self.added_repetition)
        self.count_select.setObjectName("count_select")
        self.rep_parameter_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.count_select)
        self.count_select.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.rep_hold_layout.addLayout(self.rep_parameter_layout)
        self.rep_hold_layout.setStretch(0, 1)
        self.rep_hold_layout.setStretch(2, 3)
        self.rep_whole_layout.addLayout(self.rep_hold_layout)

        self.progress_seperate_line = QtWidgets.QFrame(self.added_repetition)
        self.progress_seperate_line.setLineWidth(2)
        self.progress_seperate_line.setMidLineWidth(2)
        self.progress_seperate_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.progress_seperate_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rep_whole_layout.addWidget(self.progress_seperate_line)

        self.progress_layout = QtWidgets.QHBoxLayout()

        self.progress_label = QtWidgets.QLabel()
        self.progress_label.setText("Current Training Mode Percentage: ")
        self.progress_layout.addWidget(self.progress_label)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(35)
        self.progress_layout.addWidget(self.progress_bar)

        self.rep_whole_layout.addLayout(self.progress_layout)


        self.gridLayout_2.addLayout(self.rep_whole_layout, 0, 0, 1, 1)

        self.rep_label_op.setText(_translate("MainWindow", "About the operation:"))
        self.rep_start.setText(_translate("MainWindow", "Start This Repetition"))
        self.rep_stop.setText(_translate("MainWindow", "Stop Device"))
        self.rep_label_new.setText(_translate("MainWindow", "New Repetition:"))
        self.rep_from_speech.setText(_translate("MainWindow", "From Speech"))
        self.rep_from_ui.setText(_translate("MainWindow", "From UI"))
        self.rep_lable_save_delete.setText(_translate("MainWindow", "About Repetition:"))
        self.rep_load_existing.setText(_translate("MainWindow", "Load Existing"))
        self.rep_save.setText(_translate("MainWindow", "Save This"))
        self.rep_delete.setText(_translate("MainWindow", "Delete This"))
        self.rep_label_ball_speed.setText(_translate("MainWindow", "Ball Speed"))
        self.rep_label_spin_type.setText(_translate("MainWindow", "Spin Type"))
        self.rep_label_spin_intensity.setText(_translate("MainWindow", "Spin Intensity"))
        self.rep_label_ball_direction.setText(_translate("MainWindow", "Direction"))
        self.rep_label_ball_height.setText(_translate("MainWindow", "Heigth"))
        self.rep_label_loader_speed.setText(_translate("MainWindow", "Loader Speed"))
        self.rep_label_count.setText(_translate("MainWindow", "Throw Count"))

        self.mode_tabwidgets[mode_index].addTab(self.added_repetition, "New Repetition")

    def add_sequence(self, mode_index, is_random):
        _translate = QtCore.QCoreApplication.translate

        self.added_sequence = QtWidgets.QWidget()
        self.added_sequence.setObjectName("added_sequence")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.added_sequence)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.seq_hold_layout = QtWidgets.QHBoxLayout()
        self.seq_hold_layout.setObjectName("seq_hold_layout")

        self.seq_edit_layout = QtWidgets.QVBoxLayout()
        self.seq_edit_layout.setObjectName("seq_edit_layout")

        self.seq_label_op = QtWidgets.QLabel(self.added_sequence)
        self.seq_label_op.setObjectName("seq_label_op")
        self.seq_edit_layout.addWidget(self.seq_label_op)

        self.seq_start = QtWidgets.QPushButton(self.added_sequence)
        self.seq_start.setObjectName("seq_start")
        self.seq_edit_layout.addWidget(self.seq_start)
        self.seq_start.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.seq_stop = QtWidgets.QPushButton(self.added_sequence)
        self.seq_stop.setObjectName("seq_stop")
        self.seq_edit_layout.addWidget(self.seq_stop)
        self.seq_stop.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.seq_label_new = QtWidgets.QLabel(self.added_sequence)
        self.seq_label_new.setObjectName("seq_label_new")
        self.seq_edit_layout.addWidget(self.seq_label_new)

        self.seq_from_speech = QtWidgets.QPushButton(self.added_sequence)
        self.seq_from_speech.setObjectName("seq_from_speech")
        self.seq_edit_layout.addWidget(self.seq_from_speech)
        self.seq_from_speech.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.seq_from_ui = QtWidgets.QPushButton(self.added_sequence)
        self.seq_from_ui.setObjectName("seq_from_ui")
        self.seq_edit_layout.addWidget(self.seq_from_ui)
        self.seq_from_ui.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.seq_from_ui.clicked.connect(lambda: self.add_sequence(mode_index))

        self.seq_label_save_delete = QtWidgets.QLabel(self.added_sequence)
        self.seq_label_save_delete.setObjectName("seq_label_save_delete")
        self.seq_edit_layout.addWidget(self.seq_label_save_delete)

        self.seq_save = QtWidgets.QPushButton(self.added_sequence)
        self.seq_save.setObjectName("seq_save")
        self.seq_edit_layout.addWidget(self.seq_save)
        self.seq_save.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.seq_delete = QtWidgets.QPushButton(self.added_sequence)
        self.seq_delete.setObjectName("seq_delete")
        self.seq_edit_layout.addWidget(self.seq_delete)
        self.seq_delete.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.seq_delete.clicked.connect(lambda: self.delete_seq())

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.seq_edit_layout.addItem(spacerItem1)

        self.seq_hold_layout.addLayout(self.seq_edit_layout)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.add_remove_throw_layout = QtWidgets.QHBoxLayout()
        self.add_remove_throw_layout.setObjectName("horizontalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_remove_throw_layout.addItem(spacerItem2)

        self.add_throw_button = QtWidgets.QPushButton(self.added_sequence)
        self.add_throw_button.setObjectName("add_throw_button")
        self.add_remove_throw_layout.addWidget(self.add_throw_button)
        self.add_throw_button.setFixedHeight(50)

        self.remove_throw_button = QtWidgets.QPushButton(self.added_sequence)
        self.remove_throw_button.setObjectName("remove_throw_button")
        self.add_remove_throw_layout.addWidget(self.remove_throw_button)
        self.remove_throw_button.setFixedHeight(50)

        self.verticalLayout_4.addLayout(self.add_remove_throw_layout)

        self.sequence_throws_table = QtWidgets.QTableWidget(self.added_sequence)
        self.sequence_throws_table.setObjectName("sequence_throws_table")
        self.sequence_throws_table.setColumnCount(6)

        if is_random is False:
            self.sequence_tables.append(self.sequence_throws_table)
            index_of_sequence = len(self.sequence_tables) - 1
            self.add_throw_button.clicked.connect(lambda: self.add_throw(self.sequence_tables[index_of_sequence]))
            self.remove_throw_button.clicked.connect(lambda: self.delete_throw(self.sequence_tables[index_of_sequence]))

        else:
            self.random_sequence_tables.append(self.sequence_throws_table)
            index_of_sequence = len(self.random_sequence_tables) - 1
            self.add_throw_button.clicked.connect(lambda: self.add_throw(self.random_sequence_tables[index_of_sequence]))
            self.remove_throw_button.clicked.connect(lambda: self.delete_throw(self.random_sequence_tables[index_of_sequence]))

        for t in range(6):
            item = QtWidgets.QTableWidgetItem()
            self.sequence_throws_table.setHorizontalHeaderItem(t, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.sequence_throws_table.setItem(0, 0, item)

        self.verticalLayout_4.addWidget(self.sequence_throws_table)

        self.seq_hold_layout.addLayout(self.verticalLayout_4)

        self.seq_hold_layout.setStretch(0, 1)
        self.seq_hold_layout.setStretch(1, 3)

        self.gridLayout_4.addLayout(self.seq_hold_layout, 0, 0, 1, 1)

        self.mode_tabwidgets[mode_index].addTab(self.added_sequence, "New Sequence")

        self.seq_label_op.setText(_translate("MainWindow", "About the operation:"))
        self.seq_start.setText(_translate("MainWindow", "Start This Repetition"))
        self.seq_stop.setText(_translate("MainWindow", "Stop Device"))
        self.seq_label_new.setText(_translate("MainWindow", "New Sequence:"))
        self.seq_from_speech.setText(_translate("MainWindow", "From Speech"))
        self.seq_from_ui.setText(_translate("MainWindow", "From UI"))
        self.seq_label_save_delete.setText(_translate("MainWindow", "About Sequence:"))
        self.seq_save.setText(_translate("MainWindow", "Save This"))
        self.seq_delete.setText(_translate("MainWindow", "Delete This"))
        self.add_throw_button.setText(_translate("MainWindow", "Add Throw"))
        self.remove_throw_button.setText(_translate("MainWindow", "Remove Throw"))

        item = self.sequence_throws_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ball Speed"))
        item = self.sequence_throws_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Spin Type"))
        item = self.sequence_throws_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Spin Intensity"))
        item = self.sequence_throws_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Direction"))
        item = self.sequence_throws_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Height"))
        item = self.sequence_throws_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Loader Speed"))

    def delete_seq(self):
        self.overall_layout.removeWidget(self.seq_mode_tabs)
        self.seq_mode_tabs = None






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

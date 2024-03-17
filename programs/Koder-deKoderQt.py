import time

from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget,
                             QToolBar, QTextEdit, QPushButton, QSpinBox, QLabel)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Koder-deKoder')
        self.setFixedSize(255,150)

        self.layout = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QVBoxLayout()

        self.line_code = QLineEdit()
        self.line_code.setPlaceholderText('Code')
        self.line_code.returnPressed.connect(self.code_edit)

        self.label_win1 = QLabel()
        self.label_win1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_win1.hide()

        self.line_decode = QLineEdit()
        self.line_decode.setPlaceholderText('deCode')
        self.line_decode.returnPressed.connect(self.decode_edit)

        self.label_of_settings = QLabel()
        self.label_of_settings.setText('Keys for crypting')
        self.label_of_settings.hide()

        self.settings = QTextEdit()
        self.usual_text = 'АаБбВвГгДдЕеЁёЖжЗзИиКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtVvWwXxYyZz /*!()-_=+@#"$%^><&:;~`{}[]'
        self.settings.setText(self.usual_text)
        self.settings.setReadOnly(True)
        self.settings.hide()

        self.slider_of_move = QSpinBox()
        self.slider_of_move.setMaximum(len(self.usual_text))
        self.slider_of_move.setMinimum(0)
        self.slider_of_move.setValue(2)
        self.slider_of_move.hide()

        self.label_of_slider = QLabel()
        self.label_of_slider.setText("Move on Cesar")
        self.label_of_slider.hide()

        self.button_settings_edit = QPushButton()
        self.button_settings_edit.setText('Edit')
        self.button_settings_edit.pressed.connect(self.edit_true)
        self.button_settings_edit.hide()

        self.button_save_settings_edit = QPushButton()
        self.button_save_settings_edit.setText('Save')
        self.button_save_settings_edit.pressed.connect(self.edit_save)
        self.button_save_settings_edit.hide()

        self.action = QAction('Crypting Settings', self)
        self.action.triggered.connect(self.new_win)

        self.action2 = QAction("Crypting")
        self.action2.triggered.connect(self.old_win)

        self.tool_bar = QToolBar('Tools')
        self.addToolBar(self.tool_bar)
        self.tool_bar.setMovable(False)
        self.tool_bar.addAction(self.action)

        self.layout.addWidget(self.line_code)
        self.layout.addWidget(self.label_win1)
        self.layout.addWidget(self.line_decode)
        self.layout.addWidget(self.label_of_settings)
        self.layout.addWidget(self.settings)
        self.layout.addWidget(self.label_of_slider)
        self.layout.addWidget(self.slider_of_move)
        self.layout.addWidget(self.button_settings_edit)
        self.layout.addWidget(self.button_save_settings_edit)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

    def get_wordlist(self) -> dict:
        word_list = self.dict_gen()[1]
        return word_list

    def get_desh_wordlist(self) -> dict:
        word_list_desh = self.dict_gen()[0]
        return word_list_desh

    def dict_gen(self) -> list:
        spisok = self.settings.toPlainText()
        move = self.slider_of_move.value()
        keys = list(spisok)
        k = 0
        values_1 = []
        for i in range(len(spisok)):
            values_1.append(spisok[k - move])
            k += 1
        end = [dict(zip(keys, values_1)), dict(zip(values_1, keys))]
        return end

    def code_edit(self):
        try:
            self.label_win1.hide()
            cout = self.line_code.text()
            word = []
            k = 0
            for i in range(len(cout)):
                wl = self.get_wordlist()[cout[k]]
                word += wl
                k += 1
            word.reverse()
            self.line_decode.setText(''.join(word))
            self.line_code.clear()
        except Exception:
            self.label_win1.show()
            self.label_win1.setText('Unknown key!')

    def decode_edit(self):
        try:
            self.label_win1.hide()
            cout = self.line_decode.text()
            word = []
            k = 0
            for i in range(len(cout)):
                wl = self.get_desh_wordlist()[cout[k]]
                word += wl
                k += 1
            word.reverse()
            self.line_code.setText(''.join(word))
            self.line_decode.clear()
        except Exception:
            self.label_win1.show()
            self.label_win1.setText('Unknown key!')
            self.label_win1.hide()

    def edit_true(self):
        self.settings.setReadOnly(False)

    def edit_save(self):
        self.settings.setReadOnly(True)

    def new_win(self):
        h_win_1 = [self.line_code,
                   self.line_decode,
                   self.label_win1]
        sh_win_1 = [self.settings,
                    self.button_settings_edit,
                    self.button_save_settings_edit,
                    self.slider_of_move,
                    self.label_of_slider,
                    self.label_of_settings]
        for i in h_win_1:
            i.hide()
        for i in sh_win_1:
            i.show()
        self.tool_bar.removeAction(self.action)
        self.tool_bar.addAction(self.action2)
        self.setFixedSize(255 * 2,150 * 2)

    def old_win(self):
        sh_win = [self.line_code,
                  self.line_decode,
                  self.label_win1]
        h_win = [self.settings,
                 self.button_settings_edit,
                 self.button_save_settings_edit,
                 self.slider_of_move,
                 self.label_of_slider,
                 self.label_of_settings]
        for i in sh_win:
            i.show()
        for i in h_win:
            i.hide()
        self.tool_bar.removeAction(self.action2)
        self.tool_bar.addAction(self.action)
        self.setFixedSize(255, 150)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()


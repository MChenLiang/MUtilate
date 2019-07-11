#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2019/7/12 0012 0:17
# @File  : warning_dlg.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import existUI as exUI
import baseFunction as bFc

# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# get dirname
thisFolder = bFc.getScriptPath()


def icon_path(in_name):
    """
    get icons path
    :param in_name:
    :return:
    """
    return os.path.join(thisFolder, 'icons', in_name).replace('\\', '/')


# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class warning_ui(exUI.QDialog):
    all_x = 570
    all_y = 180

    def __init__(self, obj_name, title="Please enter something!", conf='w', parent=None):
        super(warning_ui, self).__init__(parent)
        self.conf = conf
        # 设置 窗口透明
        # self.setMouseTracking(True)
        # self.setWindowFlags(exUI.Qt.FramelessWindowHint | exUI.Qt.WindowStaysOnTopHint)
        # 设置 窗口名称
        obj_name = obj_name or "Dialog"
        self.setObjectName(obj_name)
        self.setWindowTitle(obj_name)

        self.mainLay = exUI.QVBoxLayout(self)

        iconLay = exUI.QHBoxLayout()
        self.mainLay.addLayout(iconLay)

        spacerItem = exUI.QSpacerItem(40, 20, exUI.QSizePolicy.Expanding, exUI.QSizePolicy.Minimum)
        iconLay.addItem(spacerItem)

        self.label_icon = exUI.QLabel(self)
        sizePolicy = exUI.QSizePolicy(exUI.QSizePolicy.Fixed, exUI.QSizePolicy.Fixed)
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setFixedSize(60, 60)
        self.label_icon.setScaledContents(True)
        iconLay.addWidget(self.label_icon)

        spacerItem = exUI.QSpacerItem(40, 20, exUI.QSizePolicy.Expanding, exUI.QSizePolicy.Minimum)
        iconLay.addItem(spacerItem)

        self.label_message = exUI.QLabel(title, self)
        sizePolicy = exUI.QSizePolicy(exUI.QSizePolicy.Expanding, exUI.QSizePolicy.Expanding)
        self.label_message.setSizePolicy(sizePolicy)
        self.label_message.setTextFormat(exUI.Qt.AutoText)
        self.label_message.setAlignment(exUI.Qt.AlignLeading | exUI.Qt.AlignLeft | exUI.Qt.AlignTop)
        self.mainLay.addWidget(self.label_message)

        self.button_box = exUI.QDialogButtonBox(self)
        self.button_box.setOrientation(exUI.Qt.Horizontal)
        self.mainLay.addWidget(self.button_box)

        self.__init__UI()
        self.bt_clicked()

        self.resize(self.all_x, self.all_y)

    def __init__UI(self):
        new_cc = self.conf.upper().strip()
        if new_cc == 'E':
            self.button_box.setStandardButtons(exUI.QDialogButtonBox.Close)
            pixmap = exUI.QPixmap(icon_path('dlg/dialog_error.png'))
            pass

        elif new_cc == 'S':
            self.button_box.setStandardButtons(exUI.QDialogButtonBox.Ok)
            pixmap = exUI.QPixmap(icon_path('dlg/dialog_success.png'))
            pass

        elif new_cc == 'A':
            self.button_box.setStandardButtons(exUI.QDialogButtonBox.Yes | exUI.QDialogButtonBox.No)
            pixmap = exUI.QPixmap(icon_path('dlg/dialog_ask.png'))
            pass

        else:
            # if new_cc == 'w':
            self.button_box.setStandardButtons(exUI.QDialogButtonBox.Ok | exUI.QDialogButtonBox.Cancel)
            pixmap = exUI.QPixmap(icon_path('dlg/dialog_warning.png'))

        of_x, of_y = pixmap.width(), pixmap.height()
        self.label_icon.setPixmap(pixmap)
        self.label_icon.setGeometry((self.all_x - of_x) / 2, 10, of_x, of_y)

    def bt_clicked(self):
        """
        所有的按钮信号槽链接
        :return:
        """
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

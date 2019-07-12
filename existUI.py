#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2019/7/12 0012 0:16
# @File  : existUI.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
"""
UI库信息
"""
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import re
import xml
import cStringIO

import maya.OpenMayaUI as mui
import maya.cmds as cmds

maya_qt_ver = int(re.match('\d', cmds.about(qt=True)).group())

# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

if maya_qt_ver == 4:
    try:
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *
        from PyQt4 import uic
        import sip
        from PyQt4.QtCore import pyqtSignal as signal

        USE_PYQT_MODULE = True
    except ImportError:
        from PySide.QtCore import *
        from PySide.QtGui import *
        import shiboken
        from PySide.QtCore import Signal as signal
        import pysideuic as uic

        USE_PYQT_MODULE = False

if maya_qt_ver == 5:
    try:
        from PyQt5.QtGui import *
        from PyQt5.QtCore import *
        from PyQt5.QtWidgets import *
        from PyQt5 import uic
        import sip
        from PyQt5.QtCore import pyqtSignal as signal

        USE_PYQT_MODULE = True

    except ImportError:
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        from PySide2.QtWidgets import *
        import shiboken2 as shiboken
        from PySide2.QtCore import Signal as signal
        import pyside2uic as uic

        USE_PYQT_MODULE = False


# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
def GetMayaLayout(layoutString):
    ptr = mui.MQtUtil.findLayout(layoutString)
    if ptr:
        return wrapInstance(long(ptr))


def GetWindow(windowName):
    ptr = mui.MQtUtil.findWindow(windowName)
    if ptr:
        return wrapInstance(long(ptr))


def GetFullName(qObj):
    if USE_PYQT_MODULE:
        pointer = sip.unwrapinstance(qObj)
    else:
        pointer = long(shiboken.getCppPointer(qObj)[0])
    if type(pointer) == long:
        windowString = mui.MQtUtil.fullName(pointer)
        if windowString:
            return windowString
        else:
            return ''
    else:
        return GetQtWidget(qObj.objectName(), LongName=True)[-1]


def wrapInstance(widget):
    if isinstance(widget, basestring):
        widget = mui.MQtUtil.findWindow(widget)
    if USE_PYQT_MODULE:
        return sip.wrapinstance(long(widget), QObject)
    else:
        return shiboken.wrapInstance(long(widget), QWidget)


def GetMayaMainWindow():
    maya_window = mui.MQtUtil.mainWindow()
    return wrapInstance(maya_window)


def GetQtWidget(QWidgetName, LongName=False):
    RootName = str(GetMayaMainWindow().objectName())
    Name = QWidgetName.split('|')[-1]
    for w in QApplication.topLevelWidgets():
        try:
            if w.objectName() == Name:
                if LongName:
                    return w, '|' + '|'.join([RootName, QWidgetName])
                else:
                    return w
        except:
            pass

    try:
        for w in QApplication.topLevelWidgets():
            for c in w.children():
                if c.objectName() == Name:
                    if LongName:
                        return c, '|' + '|'.join([str(w.objectName()), str(c.objectName())])
                    else:
                        return c

    except:
        pass


def UIExists(Name, AsBool=True):
    """
    exists ui by QObject name
    :param Name:  object name
    :param AsBool:  is bool
    :return:
    """
    QObject = GetQtWidget(Name)
    if QObject:
        if AsBool:
            return bool(QObject)
        return QObject
    elif AsBool:
        return False
    else:
        return None


def deleteUI(Name):
    """

    :param Name:  QObject name
    :return:
    """
    qObject = UIExists(Name, AsBool=False)
    if not qObject:
        return
    if USE_PYQT_MODULE:
        sip.delete(qObject)
    else:
        cmds.deleteUI(Name)


def loadUi(uiPath):
    """
    read an ui file, get two classes to return..
    """
    if USE_PYQT_MODULE:
        form_class, base_class = __pyqtLoadUi(uiPath)
    else:
        form_class, base_class = __pysideLoadUi(uiPath)
    return form_class, base_class


def __pyqtLoadUi(uiPath):
    """
    read an ui file, use PyQt4 method get two classes to return..
    """
    return uic.loadUiType(uiPath)


def __pysideLoadUi(uiPath):
    """
    read an ui file, use PySide method get two classes to return..
    """
    parsed = xml.etree.ElementTree.parse(uiPath)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiPath, 'r') as f:
        o = cStringIO.StringIO()
        frame = dict()

        uic.compileUi(f, o, indent=0)

        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        form_class = frame['Ui_%s' % form_class]
        base_class = eval(widget_class)

    return form_class, base_class


# start gif --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#

class mSplashScreen(QSplashScreen):
    def __init__(self, animation, flag):
        super(mSplashScreen, self).__init__(QPixmap(), flag)
        self.move = QMovie(animation)
        self.move.frameChanged.connect(self.onNextFrame)

    def onNextFrame(self):
        pixmap = self.move.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

    def showEvent(self, *args):
        self.move.start()

    def finish(self, widget):
        widget.show()
        deleteUI(self.movie.objectName())
        deleteUI(self.objectName())


class mSplashScreen_new(QSplashScreen):
    """
    start movie once
    """

    def __init__(self, animation, flag, widget):
        super(mSplashScreen_new, self).__init__(QPixmap(), flag)
        self.movie = QMovie(animation)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.count = self.movie.frameCount()
        self.step = 0
        self.widget = widget

    def onNextFrame(self):
        if self.step < self.count:
            pixmap = self.movie.currentPixmap()
            self.setPixmap(pixmap)
            self.setMask(pixmap.mask())
            self.step += 1
        else:
            self.finish(self.widget)

    def showEvent(self, *args):
        self.movie.start()

    def finish(self, widget):
        widget.show()
        deleteUI(self.movie.objectName())
        deleteUI(self.objectName())

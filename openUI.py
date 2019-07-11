#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2019/7/12 0012 0:17
# @File  : openUI.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

import time
from functools import partial

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import pg_conf
import progress_bar
import warning_dlg

reload(progress_bar)
reload(warning_dlg)


# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def show_progress(*args, **kwargs):
    return progress_bar.show(*args, **kwargs)


def warning(title, conf='w', parent=None, objectName=None):
    ui_warning = warning_dlg.warning_ui(objectName, title, conf, parent)
    ui_warning.exec_()
    return ui_warning.result()


def _pro():
    pg_conf.progress_title = 'Start'
    for i in range(101):
        time.sleep(0.1)
        pg_conf.progress_current_val = i
        pg_conf.progress_label = "Had Finished {}%!!".format(i)
        print pg_conf.progress_current_val


def testPro():
    partial(show_progress, "txt_", None, _pro)()


"""
import sys
in_path = ''

in_path in sys.path or sys.path.append(in_path)

from MUtils import openUI
reload(openUI)
openUI.testPro()
"""

# MUtil
Qt界面:（在maya中编写，如果用到其他的当中需要修改一下）

包含: 
  进度条
  提示窗口

调用方案
"""
import sys
in_path = ''

in_path in sys.path or sys.path.append(in_path)

from MUtils import openUI
reload(openUI)
if openUI.warning('aaa', 'a'):
    openUI.testPro()
"""


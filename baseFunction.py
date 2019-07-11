#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2019/7/12 0012 0:30
# @File  : baseFunction.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import inspect


# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

def getParentClasses(obj):
    """
    Get object's all of parent class...
    """
    if type(obj) == type:
        return inspect.getmro(obj)
    else:
        return inspect.getmro(obj.__class__)


def getModulesPath(moudle):
    """
    return dir for imported moudle..
    """
    moduleFile = inspect.getfile(moudle)
    modulePath = os.path.dirname(moduleFile)
    return modulePath


def getScriptPath():
    """
    return dir path for used script..
    """
    scriptPath = getModulesPath(inspect.currentframe().f_back)
    return scriptPath

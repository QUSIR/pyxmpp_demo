#!/usr/bin/python -u
# -*- coding:cp936 -*-
from distutils.core import setup
import py2exe
import sys
'''
import im_tcp_tunneler
import logging
#本地化字符编码
import locale
#编码处理
import codecs
import pdb
import threading
import time
#获取ID库
import uuid
#异常库
import traceback
import socket
import struct
import pprint
from pyxmpp.all import JID,Iq,Presence,Message,StreamError
from pyxmpp.jabber.client import JabberClient
from pyxmpp.interface import implements
from pyxmpp.interfaces import *
from pyxmpp.streamtls import TLSSettings
from PyQt4 import QtCore, QtGui
from decimal import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *


from project_sever import Ui_Form
'''

#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip","pyxmpp","M2Crypto","dns","Skype4Py","libxmlmods","PyQt4",],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }
 
setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows = [{'script':'tunneler_client.py','icon_resources':[(1,"icon.ico")]}],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )
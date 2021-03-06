# -*- coding: utf-8-*-
from distutils.core import setup
import py2exe,sys,os
includes = ["encodings", "encodings.*","pyxmpp","M2Crypto","dns","Skype4Py","libxmlmods","PyQt4"]
origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
        if os.path.basename(pathname).lower() in ("QtSvg4.dll"):
                return 0
        return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
setup(windows=[{'script':'tunneler_sever.py','icon_resources':[(1,"icon.ico")]}],
       options={'py2exe': {'includes':['sip','PyQt4._qt','PyQt4.QtCore','PyQt4.QtSvg','PyQwt'],
                "optimize": 0,
                "includes": includes
                #,"bundle_files": 1
                          }},
      data_files=["icon.ico"])
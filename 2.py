# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#0430作業1
#101_AI班林建名

import webbrowser as web
import sys

if len(sys.argv) == 2:
    web.get('windows-default').open_new(sys.argv[1])
else:
    print("請輸入網址!!")
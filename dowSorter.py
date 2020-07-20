# -*- coding: utf-8 -*-
# dowSort.py
#   by Pixel
import os
import datetime
import re
import shutil

# Move to download's folder (needy, if script inside Downloads)
# ROOT = "C:\\Users\\pikse\\Downloads"
# os.chdir(ROOT)

DATE = datetime.datetime.now().strftime("%Y-%m-%d")
REGEX = re.compile(r'\d\d\d\d-((0\d)|(1[0-2]))-(([0-2]\d)|(3[0-1]))')

# Create DATEDIR folder, if exsistn't
try:
  os.stat(DATE)
except:
  os.mkdir(DATE)

# move all dirs except other date's (except by date format YYYY-MM-DD)
for file in os.listdir():
  if bool(REGEX.match(file)) or file in ('dowSort.exe', 'dowSort.py', '$RECYCLE.BIN'):
    pass
  else:
    try:
      shutil.move(file, DATE)
    except:
      pass


# cleanup empty folders
for file in os.listdir():
  if os.path.isdir(file) and file not in ('System Volume Information'):
    if not bool(os.listdir(file)): os.rmdir(file)

# -*- coding: utf-8 -*-
# dowSort.py
#   by Pixel
import os
import sys
import datetime
import re
import shutil
import time
import platform

MOD = sys.argv[1:] != []
MONTHS = {
  'Jan': '01',
  'Feb': '02',
  'Mar': '03',
  'Apt': '04',
  'May': '05',
  'Jun': '06',
  'Jul': '07',
  'Aug': '08',
  'Sep': '09',
  'Oct': '10',
  'Nov': '11',
  'Dec': '12',
}

REGEX = re.compile(r'\d\d\d\d-((0\d)|(1[0-2]))-(([0-2]\d)|(3[0-1]))')

def theDate(pathToFile, mDate): # get file creation/modyfication date
  if platform.system() == 'Windows':
    if mDate: complexDate = time.ctime(os.path.getmtime(pathToFile)).split()
    else: complexDate = time.ctime(os.path.getctime(pathToFile)).split()
    daydate = complexDate[2]
    if len(daydate) == 1: daydate = '0' + daydate
    return complexDate[4] + '-' + MONTHS.get(complexDate[1], '00') + '-' + daydate
  else: # if can't, use today's date
    return datetime.datetime.now().strftime("%Y-%m-%d")

for file in os.listdir(): # move all stuff into date folder
  thedate = theDate(file, MOD)
  try: # Create DATE folder, if exsistn't
    os.stat(thedate)
  except:
    os.mkdir(thedate)
  if (bool(REGEX.match(file))) or (file in ('dowSort.exe', 'dowSort.py', '$RECYCLE.BIN',)): # except folders with date format YYYY-MM-DD and protected files
    pass
  else:
    try:
      shutil.move(file, thedate)
    except:
      pass

for file in os.listdir(): # cleanup empty folders
  if os.path.isdir(file) and file not in ('System Volume Information',):
    if not bool(os.listdir(file)): os.rmdir(file)

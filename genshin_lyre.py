import ctypes, sys
import os
import time
import win32api
import win32con
import win32gui
import threading
import time
import argparse

letter = {'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90}

def press(note):
    note = note.lower()
    win32api.keybd_event(letter[note], 0, 0, 0)
    print("Press: ", letter[note])

def release(note):
    note = note.lower()
    win32api.keybd_event(letter[note], 0, win32con.KEYEVENTF_KEYUP, 0)

def play_lyre(filename, key_text):
    stime = int(input("Sleep time(seconds):"))
    print("Play will start in " + str(stime) + " seconds")
    time.sleep(stime) 
    print('Playing:', filename)
    for i in range(len(key_text)):
        if key_text[i] == normal_pause:
            time.sleep(1)
        elif key_text[i] == quick_pause:
            time.sleep(0.5)
        elif key_text[i] == dash:
            time.sleep(0.2)
        elif key_text[i] == new_line:
            time.sleep(1.2)
        else:
            press(key_text[i])
            release(key_text[i])
    print('Finished playing.')

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

if is_admin():
	pass
else:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	exit(0)

# delay types
new_line = '\n'         # 1.2 sec
normal_pause = ' '      # 1.0 sec
quick_pause = '>'       # 0.5 sec 
dash = '-'              # 0.2 sec

# read file
filename = str(input("filename:"))
fileObject = open(filename, 'r')
data = list(fileObject.read())

# auto-play
play_lyre(filename, data)
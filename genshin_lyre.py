import ctypes, sys
import os
import time
import win32api
import win32con
import win32gui
import threading
import time

# key-value mapping
letter = {'a': 65, 'b': 66, 'c': 67, 
          'd': 68, 'e': 69, 'f': 70, 
          'g': 71, 'h': 72, 'i': 73, 
          'j': 74, 'k': 75, 'l': 76, 
          'm': 77, 'n': 78, 'o': 79, 
          'p': 80, 'q': 81, 'r': 82, 
          's': 83, 't': 84, 'u': 85, 
          'v': 86, 'w': 87, 'x': 88, 
          'y': 89, 'z': 90
        }

# this will make or break the ability for the keypress to register in the game
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

# helper function 1
def read_directory(directory):
    script_list = os.listdir(directory)
    print('\n')
    for count in range(0, len(script_list)):
        print(str(count) + "：" + script_list[count])
    filename = script_list[int(input('\nPlease enter the song number: '))]
    fileObject = open(directory+filename, 'r')
    return list(fileObject.read()), filename

# helper function 2
def press(note):
    note = note.lower()
    win32api.keybd_event(letter[note], 0, 0, 0)
    print("Press:", note)

# helper function 3
def release(note):
    note = note.lower()
    win32api.keybd_event(letter[note], 0, win32con.KEYEVENTF_KEYUP, 0)

# delay types
new_line = '\n'         # 0.0 sec (just to make it look nice)
normal_pause = ' '      # 0.8 sec (normal)
quick_pause = '>'       # 0.4 sec (slow tempo)
normal_dash = '-'       # 0.2 sec (quick tap)
quick_dash = '.'        # 0.1 sec (extra quick tap)

# auto_play function
def play_lyre():
    # read file as list
    data, song_name = read_directory('songscript/')
    # delay start
    buffer_time = int(input("Buffer time(seconds): "))
    print("Play will start in...")
    time.sleep(0.5)
    while buffer_time > 0:
        print(buffer_time)
        time.sleep(1)
        buffer_time -= 1
    print('Playing:', os.path.splitext(song_name)[0])
    # play logic
    for i in range(len(data)):
        if data[i] == normal_pause:
            time.sleep(0.8)
        elif data[i] == quick_pause:
            time.sleep(0.4)
        elif data[i] == normal_dash:
            time.sleep(0.2)
        elif data[i] == quick_dash:
            time.sleep(0.1)
        elif data[i] == new_line:
            time.sleep(0.0)
        else:
            press(data[i])
            release(data[i])
    print('Finished playing:', os.path.splitext(song_name)[0])
    # play continue?
    playnext = str(input("Continue? (y/n): ")).lower()
    while playnext != 'y' or playnext != 'n':
        print('Please enter a valid response!')
        playnext = str(input("Continue? (y/n): ")).lower()
        if playnext == 'y':
            play_lyre()
        elif playnext == 'n':
            exit(0)

def main():
    # this will make or break the ability for the keypress to register in the game
    if is_admin():
	    pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit(0)
    # start auto-play
    play_lyre()

if __name__ == '__main__':
    main()

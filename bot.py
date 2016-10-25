#!/usr/bin/python
import sys
import time
import gtk
import pyautogui

def get_pixel():
    rw = gtk.gdk.get_default_root_window()
    pix1 = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
    center = pix1.get_from_drawable(rw, rw.get_colormap(), 698, 542, 0, 0, 1, 1)
    return pix1.pixel_array[0, 0][0]

def main():
    died = False
    level = 1
    delay = 0.0001
    game_pix_color = 182
    dead_pix_color = 211

    time.sleep(3)

    pyautogui.press(' ')

    time.sleep(0.5)
    pyautogui.press('left', 3)

    center = get_pixel()
    prev_center = center
    while died == False:
        center = get_pixel()
        print (center)
        print (prev_center)
        if (abs(prev_center - center) > 20):
            time.sleep(3)
            center = get_pixel()
            if (center == prev_center):
                pyautogui.press('left', 3)
                level += 1
            else:
                died = True
                continue

        prev_center = center
        pyautogui.press('left', 2)
        time.sleep(delay/level)

    print (level)
    print ('END')

if __name__ == "__main__":
    main()

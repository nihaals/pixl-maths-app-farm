"""
MIT License

Copyright (c) 2018 Nihaal Sangha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import copy
import math
import re
import time
import typing
from pathlib import Path

import keyboard
import pyautogui
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
PATH = Path(r"C:\Users\Nihaal\Pictures\tmp\PMA")


def ocr(file_name: str):
    return pytesseract.image_to_string(Image.open(PATH.joinpath(file_name)), lang='eng')


def screen_shot(file_name: str, run_ocr: bool = True):
    pic = pyautogui.screenshot()
    pic.save(PATH.joinpath(file_name))
    if not run_ocr:
        return PATH.joinpath(file_name)

    return ocr(file_name)


def click(x: int, y: int):
    pyautogui.click(x, y)


def typek(text, x = None, y = None):
    text = str(copy.copy(text))
    x = int(copy.copy(x))
    y = int(copy.copy(y))

    if x and y:
        click(x, y)

    keyboard.write(text)


def test_screen_shot_ocr(file_name: str):
    print('Waiting 5 seconds')
    time.sleep(5)
    print(screen_shot(file_name))


def test_question(func: typing.Callable):
    print('Waiting 5 seconds')
    time.sleep(5)

    func()


def round_sigfigs(num, sig_figs):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0


mark_it_coords = (872, 179)
max_zoom_coords = (783, 846)
zoom_out_coords = (656, 849)
orange_rgb = (255, 83, 0)


def round_dp():
    # Zoom in
    click(*max_zoom_coords)
    time.sleep(0.5)
    click(1432, 513)
    time.sleep(2)

    r = screen_shot(r'rounddp.png')

    rer = re.findall(r"(\d+\.\d+).+ ([1-9])", r)

    assert len(rer) >= 2

    a1 = round(float(rer[-2][0]), int(rer[-2][1]))
    a2 = round(float(rer[-1][0]), int(rer[-1][1]))

    # Zoom out
    click(*zoom_out_coords)
    time.sleep(0.5)

    typek(a1, 806, 410)
    typek(a2, 806, 473)

    time.sleep(0.2)
    click(*mark_it_coords)


def round_sf():
    # Zoom in
    click(*max_zoom_coords)
    time.sleep(0.5)
    click(1432, 513)
    time.sleep(2)

    r = screen_shot(r'roundsf.png')

    rer = re.findall(r"(\d+\.\d+).+ ([1-9])", r)

    assert len(rer) >= 2

    a1 = round_sigfigs(float(rer[-2][0]), int(rer[-2][1]))
    a2 = round_sigfigs(float(rer[-1][0]), int(rer[-1][1]))

    # Zoom out
    click(*zoom_out_coords)
    time.sleep(0.5)

    typek(a1, 806, 410)
    typek(a2, 806, 473)

    time.sleep(0.2)
    click(*mark_it_coords)


def qone():
    round_dp()


def qtwo():
    round_sf()


def wait_for_save():
    time.sleep(0.5)
    pyautogui.moveTo(26, 134)  # Move mouse off button

    while True:
        time.sleep(0.1)
        img = Image.open(screen_shot(r'check_saving.png', False)).load()

        # Check if orange mark it button
        if img[mark_it_coords[0], mark_it_coords[1]] == orange_rgb:
            return

        # Check if orange cycle through button
        if img[611, 506] == orange_rgb:
            # Click button
            click(611, 506)


def setup():
    print('Waiting 5 seconds')
    time.sleep(5)

    click(545, 169)
    time.sleep(0.5)
    click(708, 611)
    time.sleep(0.5)
    click(915, 783)
    time.sleep(0.5)
    click(707, 643)
    time.sleep(0.5)
    click(696, 369)
    click(696, 432)
    time.sleep(0.5)
    click(707, 810)


def main_app(score: int = 10, wait: bool = True):
    score = copy.copy(score)
    assert score > 0

    if wait:
        print('Waiting 5 seconds')
        time.sleep(5)

    while True:
        wait_for_save()

        qone()
        score -= 1

        if score <= 0:
            return

        # Wait for saving
        wait_for_save()

        qtwo()

        score -= 1

        if score <= 0:
            return

        wait_for_save()
        time.sleep(1)

def main():
    score = input('Score: ')
    try:
        score = int(score)
    except ValueError:
        print('Enter a number.')
        return

    if score < 1:
        print('Score must be at least 1')
        return

    setup()
    main_app(score, False)

if __name__ == '__main__':
    main()

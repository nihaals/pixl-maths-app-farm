# def qone():
#     screen_shot(r"C:\Users\Nihaal\Pictures\tmp\mems0.png")
#     r = ocr(r"C:\Users\Nihaal\Pictures\tmp\mems0.png")
#
#     if '3/4' in r:
#         # Click unlikely
#         click(624, 474)
#     elif '2/4' in r:
#         # Click even
#         click(711, 474)
#     elif '1/4' in r:
#         # Click likely
#         click(798, 474)
#
#     time.sleep(0.5)
#
#     # Click mark it
#     click(*mark_it_coords)
#
#
# def qtwo():
#     screen_shot(r"C:\Users\Nihaal\Pictures\tmp\mems1.png")
#     r = ocr(r"C:\Users\Nihaal\Pictures\tmp\mems1.png")
#
#     rer = re.findall(r".*?(\d{2,4}\.\d{3}).+", r)
#
#     try:
#         n1, n2, n3, n4 = [float(i) for i in rer]
#     except ValueError:
#         print(r)
#         print(rer)
#         exit()
#
#     a1 = str(round(n1, 0))
#     a2 = str(round(n2 / 10, 0) * 10)
#     a3 = str(round(n3 / 100, 0) * 100)
#     a4 = str(round(n4 / 1000, 0) * 1000)
#
#     # Click first answer box
#     click(805, 409)
#     # Enter answer
#     keyboard.write(a1)
#
#     # Click second answer box
#     click(805, 469)
#     # Enter answer
#     keyboard.write(a2)
#
#     # Click third answer box
#     click(805, 535)
#     # Enter answer
#     keyboard.write(a3)
#
#     # Click fourth answer box
#     click(805, 599)
#     # Enter answer
#     keyboard.write(a4)
#
#     click(*mark_it_coords)
#     time.sleep(1)
#     click(*mark_it_coords)

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


def main(score: int = 10, wait: bool = True):
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


setup()
main(5, False)

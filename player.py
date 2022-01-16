import pyautogui
import time

pyautogui.PAUSE = 0.0
DELAY = 0.00
BG = (211, 247, 255)
REGION_OLD = (851, 500, 217, 1)
REGION = (868, 454, 188, 1)
LEFT = (0, 0)
RIGHT = (187, 0)


def start():
    print("starting...")
    time.sleep(1)

    pyautogui.press("space")
    time.sleep(0.5)

    pyautogui.press("left")
    pyautogui.press("right")
    # time.sleep(DELAY)


def main():
    start()
    curr = ""
    stopcount = 0
    while True:
        im = pyautogui.screenshot(region=REGION)
        colorL = im.getpixel(LEFT)
        colorR = im.getpixel(RIGHT)

        if colorR == BG and colorL == BG:
            curr = ""
            stopcount += 1
            if stopcount > 10:
                stopcount = 0
                start()
            continue
        elif colorR == BG:
            curr = "right"
        elif colorL == BG:
            curr = "left"
        if curr:
            pyautogui.press(curr)
            pyautogui.press(curr)
            stopcount = 0
            time.sleep(DELAY)


if __name__ == "__main__":
    main()

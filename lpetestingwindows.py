import pyautogui
import pillow

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
while True:
    input("Press enter to start.")
    pyautogui.click(287,998) #OC manager

    input("Please compare the part numbers to the label.") 
    input("Please insert the fiber plug or the fiber cable.")

    pyautogui.click(487,367) #add coordinates for plugged in port. Image recognition?
    pyautogui.click(979,241) #port status (click?)

    input("Please compare the port speed to the expected port speed.")

    pyautogui.click(1049,220) #diagnostics tab

    pyautogui.click(770,404) #advanced diagnostics

    pyautogui.click(283,251) #testing boxes 1,2,3
    pyautogui.click(283,290)
    pyautogui.click(283,322)

    input("Please confirm the tests passed.")
    finished = input("Please change ports or type exit if finished.")
    if finished == 'exit':
	break
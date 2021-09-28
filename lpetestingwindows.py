import pyautogui as gui
import time
import sys

gui.PAUSE = .5
gui.FAILSAFE = True

def testcycle():
    gui.alert("Plug into next port.")
    gui.click(20,66) #refresh
    time.sleep(4)
    coords = gui.locateOnScreen('./source/pluggedport.png')
    portcenter = gui.center(coords)
    
    gui.click(portcenter)
    
    gui.click(377,124) #port status 
    gui.alert("Please compare the port speed to the expected port speed.")
    time.sleep(3)
    gui.click(803,120) #diagnostics tab

    gui.click(559,278) #advanced diagnostics

    gui.click(283,251) #testing boxes 1,2,3
    gui.click(283,290)
    gui.click(283,322)
    gui.click(827,239) #start
    gui.click(598,584)
    time.sleep(13)
    gui.alert("Please confirm the tests passed.")
    gui.alert("Take a picture and mark any cards that failed.")
    gui.click(988,745) #exit

if __name__ == '__main__':
    
    while True:
        try:
            gui.click(283,1005) #OC manager
            time.sleep(5)
            totalcards = int(gui.prompt("How many cards are you testing?"))
            gui.alert("Compare Part Number to the label, then press enter:") 
            gui.click(1253,817) #click back into oc manager
            for cards in range(totalcards):
                testcycle()
            sys.exit()
                
        except KeyboardInterrupt:
            sys.exit()

#change to all image recognition.
#try, except for pluggedport.png
#ask if you want to shut down?
#16gb image recognition to exclude 3rd test
#2 port support/more testing and debugging

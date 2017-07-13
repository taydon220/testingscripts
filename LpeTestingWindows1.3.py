import pyautogui as gui
import time
import sys
import os

gui.PAUSE = .25
gui.FAILSAFE = True

def testcycle():
    gui.alert("Plug into next port.")

    gui.click(gui.locateCenterOnScreen('refresh.png',region=(0,0,550,350))) 
    
    time.sleep(4)

    gui.click(gui.locateCenterOnScreen('pluggedport.png',region=(0,0,400,700)))

    gui.click(gui.locateCenterOnScreen('portstatus.png',region=(240,90,1000,100)))
    
    gui.alert("Please compare the port speed to the expected port speed.")

    gui.click(gui.locateCenterOnScreen('diagnosticstab.png',region=(240,90,1000,100)))

    gui.click(gui.locateCenterOnScreen('advanceddiagnostics.png',region=(240,250,500,100)))
    time.sleep(1)
    
    gui.click(gui.locateCenterOnScreen('testbuttonone.png',region=(250,210,500,150)))
    gui.click(gui.locateCenterOnScreen('testbuttontwo.png',region=(250,210,500,150)))
    gui.click(gui.locateCenterOnScreen('testbuttonthree.png',region=(250,210,500,150)))
    
    gui.click(gui.locateCenterOnScreen('startbutton.png',region=(700,200,500,150)))

    gui.click(gui.locateCenterOnScreen('confirmtest.png',region=(0,400,1000,500)))
    time.sleep(14)
    
    gui.alert("Please confirm once the tests have passed.")
    gui.alert("Take a picture and mark any cards that failed.")

    gui.click(gui.locateCenterOnScreen('exitbutton.png',region=(850,630,500,150)))
    

if __name__ == '__main__':
    
    while True:
        try:
            gui.click(gui.locateCenterOnScreen('OCmanagericon.png',region=(0,900,700,200)))
            time.sleep(5)
            totalcards = int(gui.prompt("How many cards are you testing?"))
            gui.alert("Compare Part Numbers to the label, then press enter:") 
            for cards in range(totalcards):
                testcycle()
            if gui.confirm(text="Testing complete. Would you like to shutdown the machine?",buttons=['YES','NO']) == 'YES':
                if gui.confirm(text="Are you sure?",buttons=['YES','NO']) == 'YES':
                    os.system('shutdown /s /t 0')
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()

#database of correct transmission speeds?
#add stop button always running
#try, except for pluggedport.png
#16gb image recognition to exclude 3rd test
#2 port support/more testing and debugging

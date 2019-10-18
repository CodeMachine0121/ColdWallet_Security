from evdev import InputDevice, categorize, ecodes
import os

#creates object 'keyboard' to store the data
#you can call it whatever you like
keyboard = InputDevice('/dev/input/event0')

#button code variables
OneBtn,TwoBtn,ThreeBtn,FourBtn,FiveBtn,SixBtn,SevenBtn,EightBtn,NineBtn,ZeroBtn = 2,3,4,5,6,7,8,9,10,11

QBtn,WBtn,EBtn,RBtn,TBtn,YBtn,UBtn,IBtn,OBtn,PBtn = 16,17,18,19,20,21,22,23,24,25

ABtn,SBtn,DBtn,FBtn,GBtn,HBtn,JBtn,KBtn,LBtn,DelBtn = 30,31,32,33,34,35,36,37,38,14

ZBtn,XBtn,CBtn,VBtn,BBtn,NBtn,MBtn = 44,45,46,47,48,49,50

SemicolonBtn,CommaBtn,EnterBtn = 39,40,28

Shift,Alt,More,Space,Less,Cmd,Ctrl = 42,56,51,57,52,126,44

#prints out device info at start
print(keyboard)

#loop and filter by event code and print the mapped label
for event in keyboard.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:

            if event.code == OneBtn:
                print("1")
            elif event.code == TwoBtn:
                print("2")
            elif event.code == ThreeBtn:
                print("3")
            elif event.code == FourBtn:
                print("4")
            elif event.code == FiveBtn:
                print("5")
            elif event.code == SixBtn:
                print("6")
            elif event.code == SevenBtn:
                print("7")
            elif event.code == EightBtn:
                print("8")
            elif event.code == NineBtn:
                print("9")
            elif event.code == ZeroBtn:
                print("0")

            elif event.code == QBtn:
                print("Q")
            elif event.code == WBtn:
                print("W")
            elif event.code == EBtn:
                print("E")
            elif event.code == RBtn:
                print("R")
            elif event.code == TBtn:
                print("T")
            elif event.code == YBtn:
                print("Y")
            elif event.code == UBtn:
                print("U")
            elif event.code == IBtn:
                print("I")
            elif event.code == OBtn:
                print("O")
            elif event.code == PBtn:
                print("P")

            elif event.code == ABtn:
                print("A")
            elif event.code == SBtn:
                print("S")
            elif event.code == DBtn:
                print("D")
            elif event.code == FBtn:
                print("F")
            elif event.code == GBtn:
                print("G")
            elif event.code == HBtn:
                print("H")
            elif event.code == JBtn:
                print("J")
            elif event.code == KBtn:
                print("K")
            elif event.code == LBtn:
                print("L")
            elif event.code == DelBtn:
                print("Del")

            elif event.code == ZBtn:
                print("Z")
            elif event.code == XBtn:
                print("X")
            elif event.code == CBtn:
                print("C")
            elif event.code == VBtn:
                print("V")
            elif event.code == BBtn:
                print("B")
            elif event.code == NBtn:
                print("N")
            elif event.code == MBtn:
                print("M")
            elif event.code == SemicolonBtn:
                print(";")
            elif event.code == CommaBtn:
                print(",")
            elif event.code == EnterBtn:
                print("Enter")
                break


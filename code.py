from machine import Pin, PWM
from time import sleep_ms
import neopixel#neo
import random

hatalari = PWM(Pin(15), 200000)
pin = Pin(8, Pin.OUT)#neo
num= random.randint(0,15)
np = neopixel.NeoPixel(pin, 8) #neo
takki_A = Pin(10, Pin.IN, Pin.PULL_UP)
takki_B = Pin(11, Pin.IN, Pin.PULL_UP)
red   =  [ 255, 0, 0]#neo
blue= [0,0,255]#neo
off   =  [ 0, 0, 0] #neo
while True:
    if takki_A.value() ==0:
        counter=8
        spin=0
        while counter!=0:
            np[spin] = red#neo
            np.write()#neo
            sleep_ms(100)#neo
            np[spin]=off#neo
            spin+=1#neo
            if spin==16:#neo
                spin-=16#neo
                counter-=1#neo
        if num%=2:#neo
            num-1#neo
        np[num]=red#neo
        np.write()#neo
        hatalari.duty(512) # Kveikir á hátalara
        hatalari.freq(4444)
        sleep_ms(250)      # í 250 ms.
        hatalari.duty(0)
        space=num*-1
        
        
    if takki_B.value() ==0:
        counter=8#neo
        spin=0#neo
        while counter!=0:#neo
            np[spin] = blue#neo
            np.write()#neo
            sleep_ms(100)#neo
            np[spin]=off#neo
            spin+=1#neo
            if spin==16:#neo
                spin-=16#neo
                counter-=1#neo
        if num%=2:
            num-1
            if num==-1:
                num==15
        np[num]=blue#neo
        np.write()#neo
        hatalari.duty(512) # Kveikir á hátalara
        hatalari.freq(4444)
        sleep_ms(250)      # í 250 ms.
        hatalari.duty(0)
        space=num

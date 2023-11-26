from machine import Pin
from keypad import KeyPad
import time

# Pin Assignments
LED = Pin(0, Pin.OUT)
D0 = Pin(27, Pin.OUT)
D1 = Pin(26, Pin.OUT)
D2 = Pin(22, Pin.OUT)
D3 = Pin(21, Pin.OUT)
D4 = Pin(20, Pin.OUT)
D5 = Pin(19, Pin.OUT)
D6 = Pin(18, Pin.OUT)
D7 = Pin(17, Pin.OUT)
EN1 = Pin(28, Pin.OUT)
EN2 = Pin(16, Pin.OUT)
WELDER_EFFECT = Pin(1, Pin.OUT)

WELDER_STATE = 0
PINS = [LED, EN1, EN2, D0, D1, D2, D3, D4, D5, D6, D7]

CODES = { 
   '1' : [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
   '2' : [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
   '3' : [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
   '4' : [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
   '5' : [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
   '6' : [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
   '7' : [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
   '8' : [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
   '9' : [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
   'A' : [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
   'B' : [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
   'C' : [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
   'D' : [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
}

keyPad = KeyPad(9, 8, 7, 6, 2, 3, 4, 5)
def toggle_welding_effect():
    global WELDER_STATE
    if WELDER_STATE == 0:
        WELDER_STATE = 1
        WELDER_EFFECT.value(1)
    else:
        WELDER_STATE = 0
        WELDER_EFFECT.value(0)

        
def read_keypad():
    keyvalue = keyPad.scan()
    if keyvalue:
        return keyvalue
    else:
        return None
    
            
def interpret_key(key: str):
    if key:
        if key == '*':
            toggle_welding_effect()
        else:
            for pin, code in zip(PINS, CODES.get(keyvalue)):
                pin.value(code)
            LED.value(0)
        
    else:
        for pin in PINS:
            pin.value(0)
    
while True:
    keyvalue = read_keypad()
    interpret_key(keyvalue)
    time.sleep_ms(250)
           


    
    





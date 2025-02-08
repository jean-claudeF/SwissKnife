# pio_wave_sym.py - 12.09.2021
# slightly modfified
#
# Sendet eine Anzahl von symmetrischen Impulsen mit festzulegender Frequenz
# Frequenzbereich von 200 Hz bis 12.5 MHz
# Die Anzahl der zu sendenden Waves wird vor Beginn ins X-Register kopiert.
# Soll die Anzahl nicht begrenzt werden, dann muss die letzte asm-Instruktion
# auf jmp("next") geändert werden. 

import time
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

out_pin = 22
statmach = 4
    
class Pulsetrain(object):
    
    @asm_pio(set_init=PIO.OUT_LOW, in_shiftdir=PIO.SHIFT_RIGHT)
    def _pulse_train():
              
        pull(block)              #   wait for input from system to OSR
        mov(x, osr)              #   count from OSR to X
        
        label("next")            #   loop = 10 cycles
        set(pins, 1)         [4] #   5 cycles
        set(pins, 0)         [3] #   4 cycles
        jmp(x_dec, "next")       #   1 cycle
        #jmp("next")             #   for endless wave
    
    def __init__(self, statemachine, output_pin, wave_freq):
       self.sm = StateMachine(statemachine,
                        self._pulse_train,
                        freq=wave_freq*10,
                        set_base=Pin(output_pin))
       self.sm.restart()
       
    def transmit(self, cnt):
        self.sm.active(1)
        self.sm.put(cnt - 1)

    def activate(self, state=1):
        self.sm.active(1 if state else 0)

def pulsetrain(freq, cnt):
        
    wav = Pulsetrain(statmach, output_pin=out_pin, wave_freq=freq)
    wav.activate()
    wav.transmit(cnt)
    
    waittime = (1/freq)*cnt + 0.01 
    time.sleep(waittime)
    wav.activate(0)
    print("READY")

if __name__ == "__main__":
    pulsetrain(1000, 300)
    
    
    
    
    
    

        

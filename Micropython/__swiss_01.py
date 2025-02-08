from awg_05 import *
from pwm_01 import *
from i2cscan import *

import gc
def print_freememory():
    gc.collect()
    print( gc.mem_free())
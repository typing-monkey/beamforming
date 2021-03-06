import os

import numpy as np
import time

import phase_solver_code as pc

time_yesterday = time.time() - 24 * 3600.0

src = CasA

# Run script daily
sleep_time = 24 * 3600.0

while True:
     # Find previous day's transit file for CasA
     fn = pc.find_transit(time_yesterday)

     os.system('python ph_solver_script.py %s %s' % (fn, src))

     time.sleep(sleep_time)
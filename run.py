#!/usr/bin/env python

import sys
import os
import subprocess
import argparse
import time
from machinekit import launcher

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#parser = argparse.ArgumentParser(description='Chip Hello World')

def check_mklaucher():
    try:
        subprocess.check_output(['pgrep', 'mklauncher'])
        return True
    except subprocess.CalledProcessError:
        return False

try:
    launcher.check_installation()
    launcher.cleanup_session()
    launcher.start_realtime()
    launcher.load_hal_file('chip.py')
    launcher.register_exit_handler()  # needs to executed after HAL files

#    if not check_mklaucher():  # start mklauncher if not running to make things easier
#        launcher.start_process('mklauncher .')

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

sys.exit(0)

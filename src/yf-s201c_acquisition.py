import os
import serial
import logging
import pandas as pd
from datetime import datetime
from get_git_root import get_git_root


def readserial(comport, baudrate):
    now = datetime.now()
    ser = serial.Serial(comport, baudrate, timeout=0.1)

    fname = os.path.join(get_git_root(os.getcwd()),
                         "data",
                         "raw_data",
                         "yf-s201c",
                         f"{now.strftime('%Y-%m-%d_%H%M%S')}.csv")
    with open(fname, "w") as fh:
        fh.write("Datetime,Pulse count,Flow (lpm)\n")
    
    logging.basicConfig(filename = fname,
                        encoding = "utf-8",
                        filemode = "a",
                        format = "{asctime},{message}",
                        level = logging.INFO,
                        style = "{",
                        datefmt = "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
        pulse_count = ser.readline().decode().strip()
        
        if pulse_count:
            pulse_count = float(pulse_count)
            flow_lpm = (pulse_count / 7.5); # L/min
            print(f"{nowstr},{flow_lpm}")
            logging.info(f"{pulse_count},{flow_lpm}")


def main():
    readserial(comport='/dev/cu.usbmodem101', baudrate=9600)


if __name__ == '__main__':
    main()

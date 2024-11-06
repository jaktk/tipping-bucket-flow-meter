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
                         f"rnd-yf-{now.strftime('%Y-%m-%d_%H%M%S')}.csv")
    with open(fname, "w") as fh:
        fh.write("Datetime,Flow,Tip\n")
    
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
        msg = ser.readline().decode().strip()
    
        if msg:
            flow, tip = msg.split(",")
            flow = float(flow)
            tip = int(tip)
            print(f"{nowstr},{flow},{tip}")
            logging.info(f"{flow},{tip}")


def main():
    readserial(comport='/dev/cu.usbmodem101', baudrate=9600)


if __name__ == '__main__':
    main()

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
        fh.write("Datetime,Flow (lpm),Error (%)\n")
    
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
        flow_lpm = ser.readline().decode().strip()
        if flow_lpm:
            flow_lpm = float(flow_lpm) # [l/min]
            err_p = 0.01 * flow_lpm + 1 if flow_lpm <= 6 else 0.1 * flow_lpm + 2.41 # [%]
            print(f"{nowstr},{flow_lpm}")
            logging.info(f"{flow_lpm},{err_p}")


def main():
    readserial(comport='/dev/cu.usbmodem101', baudrate=9600)


if __name__ == '__main__':
    main()

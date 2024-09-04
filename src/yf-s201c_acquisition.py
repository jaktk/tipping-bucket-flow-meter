import os
import serial
import logging
import pandas as pd
from datetime import datetime
from get_git_root import get_git_root


def readserial(comport, baudrate):
    now = datetime.now()
    ser = serial.Serial(comport, baudrate, timeout=0.1)

    df = pd.read_csv("pulse-to-flow.csv", sep=",")
    fname = os.path.join(get_git_root(os.getcwd()),
                         "data",
                         "raw_data",
                         "yf-s201c",
                         f"{now.strftime('%Y-%m-%d_%H%M%S')}.csv")
    with open(fname, "w") as fh:
        fh.write("Datetime,Pulse count,Flow (lpm),Error (%)\n")
    
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
        pulse_count = round(float(pulse_count), 1)

        if pulse_count:
            _df = df[(df.pulse_min <= pulse_count) & (df.pulse_max >= pulse_count)].copy()
            print(f"{nowstr},{float(_df.flow_lpm)}")
            logging.info(f"{pulse_count},{float(_df.flow_lpm)},{float(_df.error_percent)}")


def main():
    readserial(comport='COM5', baudrate=9600)


if __name__ == '__main__':
    main()

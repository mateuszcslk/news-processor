import datetime
import os


def get_current_ts():
    dt = datetime.datetime.now()
    return int(datetime.datetime.timestamp(dt))


def abs_listdir(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
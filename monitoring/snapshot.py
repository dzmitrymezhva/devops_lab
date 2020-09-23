#! /usr/bin/env python

from datetime import datetime
import psutil
import time
import argparse
import json

cpu_i = 1


def cpu():
    value = psutil.cpu_percent(interval=cpu_i)
    return value


def memory():
    value = psutil.virtual_memory().percent
    return value


def virtual_memory():
    value = psutil.swap_memory().percent
    return value


class PlainText:
    def __init__(self, seconds):
        self.seconds = seconds

    def write_file(self):
        i = 1
        while True:
            log = open("snapshot.txt", "a")
            print("SNAPSHOT ", i, ": ", datetime.now(), " : CPU load - ",
                  cpu(),"%, memory usage - ", memory(),"%, virtual memory usage - ",
                  virtual_memory(), "%.", sep="", file=log)
            i += 1
            time.sleep(self.seconds - cpu_i)


class JSON:
    def __init__(self, seconds):
        self.seconds = seconds

    def write_file(self):
        i = 1
        while True:
            data = {'monitoring': []}
            data['monitoring'].append({
                'SNAPSHOT': i,
                'TIMESTAMP': str(datetime.now()),
                'CPU load': str(cpu()) + "%",
                'memory usage': str(memory()) + "%",
                'virtual memory usage': str(virtual_memory()) + "%"
            })
            with open('snapshot.json', 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            i += 1
            time.sleep(self.seconds - cpu_i)


parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()

if args.t == "txt":
    PlainText(args.i).write_file()
elif args.t == "json":
    JSON(args.i).write_file()
else:
    print("Sorry, you must to enter only json or txt!")

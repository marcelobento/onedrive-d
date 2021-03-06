#!/usr/bin/python

import os
import threading
import Queue
import yaml

APP_CREDS = ("000000004010C916", "PimIrUibJfsKsMcd0SqwPBwMTV7NDgYi")

LOCAL_USER = os.getenv("SUDO_USER")
if LOCAL_USER == None or LOCAL_USER == "":
	LOCAL_USER = os.getenv("USER")

HOME_PATH = os.path.expanduser("~" + LOCAL_USER)

f = open(HOME_PATH + "/.onedrive/user.conf", "r")
CONF = yaml.safe_load(f)
f.close()

QUOTA = {"free": 0, "total": 0}

AUTHENTICATED = False

NUM_OF_WORKERS = 2
NUM_OF_SCANNERS = 4
TASK_QUEUE = Queue.Queue()
SCANNER_QUEUE = Queue.Queue()
WORKER_THREADS = []
SCANNER_SEMA = threading.BoundedSemaphore(value = NUM_OF_SCANNERS)
EVENT_STOP = threading.Event()

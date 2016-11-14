import threading
import os

# Calls worker_func every interval seconds for interations times (0 is eternal loop)
def do_every(lockname, interval, worker_func, iterations=0):
    if os.environ[lockname] == 'STOP':
        os.environ[lockname] = 'FALSE'
        return
    if iterations != 1:
        threading.Timer(
            interval,
            do_every, [lockname, interval, worker_func, 0 if iterations == 0 else iterations - 1]
        ).start()
    elif iterations == 1:
        os.environ[lockname] = 'FALSE'

    worker_func()

#Start running iterations only if environment value [lockname] is 'FALSE' or doesn't exist
def start_do_every(lockname, interval, worker_func, iterations=0):
    if os.getenv(lockname, 'FALSE') == 'FALSE':
        os.environ[lockname] = 'TRUE'
        do_every(lockname, interval, worker_func, iterations)


def stop_do_every(lockname):
    os.environ[lockname] = 'STOP'
import threading
import os


def do_every(lockname, interval, worker_func, iterations=0):
    """
    Calls worker_func every interval seconds for interations times (0 is eternal loop) or until envinroment variable
    named after lockname is STOP.

    :param lockname: name of envinroment variable which specifies if certain worker is running and when to stop
    :param interval: interval the worker is run in seconds
    :param worker_func: worker function
    :param iterations: number of iterations, 0 means infinite
    """
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


def start_do_every(lockname, interval, worker_func, iterations=0):
    """
    Starts function do_every with parameters given to it unless environment variable specified by lockname is already
    TRUE, in which case it's already running.

    :param lockname: name of envinroment variable which specifies if certain worker is running and when to stop
    :param interval: interval the worker is run in seconds
    :param worker_func: worker function
    :param iterations: number of iterations, 0 means infinite
    """
    if os.getenv(lockname, 'FALSE') == 'FALSE':
        os.environ[lockname] = 'TRUE'
        do_every(lockname, interval, worker_func, iterations)


def stop_do_every(lockname):
    os.environ[lockname] = 'STOP'
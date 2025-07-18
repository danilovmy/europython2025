
def counter():
    n = 0
    while True:
        yield n          # <- thread A pauses here
        n += 1           # thread B now calls next() -> ValueError

c = counter()
next(c)                 # prime

from threading import Thread, RLock
Thread(target=next, args=(c,)).start()
Thread(target=next, args=(c,)).start()


lock = RLock()

def safe_next(gen):
    with lock:                 # SINGLE entry
        return next(gen)

def safe_send(gen, value):
    with lock:
        return gen.send(value)
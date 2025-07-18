from contextlib import contextmanager

@contextmanager
def resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = open("sample.txt")
    try:
        yield resource  # used as return
    finally:
        # Code to release resource, e.g.:
        resource.close()

...
with resource() as source:
    lines = source.readlines

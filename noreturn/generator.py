# to run examples: `python -m memory_profiler check_bytecode.py`
import dis
import timeit
from line_profiler import LineProfiler
from memory_profiler import memory_usage, profile


def test_1(*args):
    if args:
        yield sum(args)
    value = None
    return value

def test_2(*args):
    if args:
        yield sum(args)
    value = 'as exception'
    raise StopIteration(value)


def test_3(*args):
    try:
        for bit in test_1(*args):
            a = bit
    except RuntimeError as stop:
        if stop.__cause__ is StopIteration:
            pass


def test_4(*args):
    try:
        for bit in test_2(*args):
            a = bit
    except RuntimeError as stop:
        if stop.__cause__ is StopIteration:
            pass

def not_test_5(*args):
    try:
        gen = test_1(*args)
        for bit in gen:
            print(bit)
    except Exception as stop:
        pass

def not_test_6(*args):
    try:
        gen = test_2(*args)
        for bit in gen:
            print(bit)
    except Exception as stop:
        print(stop.__cause__.value)
        pass
    # print(gen.value)

def not_test_7(*args):
    value = yield from test_1(*args)
    print('nt 7 returned:', value)

def not_test_8(*args):
    try:
        yield from test_2(*args)
    except Exception as stop:
        print('nt 8 returned:', stop.__cause__.value)

def not_test_9(*args):
    try:
        print(*test_1(1))
    except Exception as stop:
        print('nt 9 returned:', stop.__cause__.value)

def not_test_10(*args):
    try:
        print(*test_2(1))
    except Exception as stop:
        print('nt 10 returned:', stop.__cause__.value)

def not_test_11(*args):
    gen = test_1(*args)
    while gen:
        try:
            print(next(gen))
        except Exception as stop:
            print('nt 11 returned:', stop.value)
            break

def not_test_12(*args):
    gen = test_2(*args)
    while gen:
        try:
            print(next(gen))
        except Exception as stop:
            print('nt 12 returned:', stop.__cause__.value)
            break

def not_test_13(*args):
    next(test_1())

def not_test_14(*args):
    next(test_2())


args = (202234, 342334545, 234567890)

functions = [val for key, val in globals().items() if key.startswith('test_')]

if __name__ == '__main__':

    for fun in functions:
        print(dis.dis(fun))
        print(dis.code_info(fun))

    for fun in functions:
        lp = LineProfiler()
        lp_wrapper = lp(fun)
        lp_wrapper(*args)
        lp.print_stats()

    for fun in functions:
        fun_str = f'{str(fun.__name__)}{args}'
        print(timeit.timeit(fun_str, globals=globals(), number=1000000))

    for fun in functions:
        print(memory_usage((fun, args, {})))

    for fun in functions:
        profile(fun)(*args)

    not_test_5(*args)
    not_test_6(*args)
    print('nt 7', *not_test_7(*args))
    print('nt 8', *not_test_8(*args))

    not_test_9(*args)
    not_test_10(*args)
    not_test_11(*args)
    not_test_12(*args)
    try:
        not_test_13()
    except Exception as err:
        print('nt 13', repr(err))

    try:
        not_test_14()
    except Exception as err:
        print('nt 14', repr(err))


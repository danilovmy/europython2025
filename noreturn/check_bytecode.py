# to run examples: `python -m memory_profiler check_bytecode.py`
import dis
import timeit
from line_profiler import LineProfiler
from memory_profiler import memory_usage, profile

def test_1(a, b, c):
    return a + b

def test_2(a, b, c):
    a + b

def test_3(a, b, c):
    a + b
    return None

def test_4(a, b, c):

    c = a + b
    return c

def test_5(a, b, c):
    c = a+b


def test_6(a, b, c):
    c = test_1(a, b, c)

def test_7(a, b, c):
    test_2(a, b, c)

args = (202234, 342334545, 'hello world!')

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
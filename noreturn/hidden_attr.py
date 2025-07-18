
class Coroutined:

    def __init__(self, attr=None):
        self._attr = self._attr(attr).send
        self.attr

    def _attr(self, attr = None, *args, **kwargs):
        while True:
            val = yield attr
            if isinstance(val, tuple):
                attr = val[0]

    attr = property(lambda self: self._attr(None), lambda self, value: self._attr((value, )))

    def coroutined_method(self, data, *args, **kwargs):
        ... #prepeare something based on args and kwargs
        response = None
        while True:
            val = yield response
            response = val * data  # calculate result with val

    def yielded_method(self, data, *args, **kwargs):
        yield data * 2

initial_data = 8
new_val = 9


coro = Coroutined(initial_data)
print(coro.attr)
coro.attr = new_val
print(coro.attr)


calc = coro.yielded_method(initial_data).send  # closure with delayed calculation
print(calc(None)) # perform calculation

calc = coro.coroutined_method(initial_data).send # closure
calc(None)  # run generator
print(calc(new_val))  # perform calculation
